from django import forms
from django.contrib.auth.hashers import make_password

from bos.apps.users.models import User, UserProfile


PROFILES_WITH_EMPTY_CHOICE = [('', '--------')] + list(UserProfile.PROFILE_CHOICES)


class UserForm(forms.ModelForm):
    profile = forms.ChoiceField(choices=PROFILES_WITH_EMPTY_CHOICE)
    # password = forms.PasswordInput()

    class Meta:
        model = User
        fields = '__all__'
        widgets = {
            'password': forms.PasswordInput(),
        }

    def clean_password(self):
        # password = super(UserForm, self).clean_password()
        password = self.cleaned_data['password']
        if not password:
            raise forms.ValidationError('Password field is empty')
        return make_password(password)


class LoginForm(forms.ModelForm):
    email = forms.EmailField()
    password = forms.PasswordInput()

    class Meta:
        model = User
        fields = ('email', 'password', )
