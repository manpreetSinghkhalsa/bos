from django import forms

# from bos_management.bos.apps.users.models import User
from bos.apps.users.models import User, UserProfile


PROFILES_WITH_EMPTY_CHOICE = [('', '--------')] + list(UserProfile.PROFILE_CHOICES)


class UserForm(forms.ModelForm):
    profile = forms.ChoiceField(choices=PROFILES_WITH_EMPTY_CHOICE, required=True)

    class Meta:
        model = User
        # model = models.User
        fields = ['email', 'username', 'first_name', 'last_name', 'profile']
