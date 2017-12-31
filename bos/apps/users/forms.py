from django import forms

from bos.apps.users.models import User, UserProfile


PROFILES_WITH_EMPTY_CHOICE = [('', '--------')] + list(UserProfile.PROFILE_CHOICES)


class UserForm(forms.ModelForm):
    profile = forms.ChoiceField(choices=PROFILES_WITH_EMPTY_CHOICE)

    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'last_name', 'password', 'profile', )


class LoginForm(forms.ModelForm):
    email = forms.EmailField()
    password = forms.PasswordInput()

    class Meta:
        model = User
        fields = ('email', 'password', )
