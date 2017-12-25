# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
from django.http.response import HttpResponseRedirect
from django.views.generic import FormView

# from bos.apps.users.forms import UserForm
from django.views.generic.base import TemplateView

from bos.apps.users.forms import UserForm
from bos.apps.users.models import UserProfile
from bos.apps.users.utils import add_user_to_group


class CreateUser(FormView):
    # context_object_name = 'profiles'
    form_class = UserForm
    success_url = "/"
    template_name = 'edit_user.html'

    def form_valid(self, form):
        """
        If the form is valid, redirect to the supplied URL.
        """

        form_data = form.cleaned_data

        profile_id = form_data.pop('profile')
        # Create user
        user = form.save()
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


class Faltu(TemplateView):
    template_name = 'success.html'
