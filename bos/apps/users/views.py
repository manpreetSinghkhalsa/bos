# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.contrib.auth import authenticate
# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse_lazy
from django.views.generic import FormView

from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView

from bos.apps.users.forms import UserForm, LoginForm
from bos.apps.users.models import UserProfile, User
from bos.apps.users.utils import add_user_to_group, generate_hash, get_group_name, generate_permission_dict


class Login(FormView):
    form_class = LoginForm
    success_url = "/create/"
    template_name = "login.html"

    def form_valid(self, form):
        """
        Once the
        :param form:
        :return:
        """
        print "************"
        data = form.cleaned_data

        user = authenticate(email=data.get('email'), password=data.get('password'))
        if user:
            # do something
            return HttpResponseRedirect(self.get_success_url())
        else:
            raise ValueError('Email and password did not match.')


class CreateUser(FormView):
    form_class = UserForm
    success_url = "/"
    template_name = 'edit_user.html'

    def form_valid(self, form):
        """
        If the form is valid, redirect to the supplied URL.
        """

        form_data = form.cleaned_data

        profile_id = form_data.pop('profile')
        # password = form_data.pop('password')

        print "apne form data: ", form_data, ' <<<<<'
        # print 'password assa da: ', password, ' <<<<'
        # obj = User(password=set_password(password))
        # form_data['password'] = User.set_password(password)
        # Create user
        user = User.objects.create(**form_data)

        print ">>>  bann gya user <<<<"
        # Create User Profile
        UserProfile.objects.create(**{
            'user': user,
            'profile': profile_id
        })
        # Add to the particular group
        add_user_to_group(user_obj=user, profile_choice=profile_id)

        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super(CreateUser, self).get_context_data(**kwargs)
        context['profiles'] = UserProfile.PROFILE_CHOICES
        return context


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class Dashboard(TemplateView):
    template_name = 'common/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super(Dashboard, self).get_context_data(**kwargs)
        user_group_names = get_group_name(self.request.user)
        print 'all group names: ', user_group_names, '  <<<<< user: ', self.request.user, ' <<<<'
        print generate_permission_dict(context, user_group_names), ' <<<<'
        return generate_permission_dict(context, user_group_names)
