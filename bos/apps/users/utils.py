from bos.apps.users.models import UserProfile
from django.contrib.auth.models import Group


def add_user_to_group(user_obj, profile_choice):
    """
    Add user to the group
    :param user_obj: user object
    :param profile_choice: 1/2/3/4 choice of the profile
    """
    group_name = UserProfile.PROFILE_GROUP_DICT.get(profile_choice)
    try:
        my_group = Group.objects.get(name=group_name)
        my_group.user_set.add(user_obj)
    except Exception as exception:
        print "Some error occurred: ", exception
