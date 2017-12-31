import hashlib

from django.conf import settings
from django.contrib.auth.models import Group

from bos.apps.users.models import UserProfile


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


def generate_hash(str_data):
    """
    Generate hash for the string data
    :param str_data: str_data should not be None
    :return: hashed data
    """
    if str_data is None:
        return ''
    return hashlib.sha256(str_data).hexdigest()


def get_profile(user_obj):
    """

    :param user_obj:
    :return:
    """
    # Only one entry will be in the UserProfile model
    return UserProfile.objects.filter(user=user_obj).first().profile


def generate_permission_dict(main_dict, user_profile):
    """

    :param main_dict:
    :param user_profile:
    :return:
    """
    main_dict['role'] = {}
    main_dict['role']['is_admin'] = user_profile == settings.ADMIN
    main_dict['role']['is_co_admin'] = user_profile == settings.CO_ADMIN
    main_dict['role']['is_volunteer'] = user_profile == settings.VOLUNTEER
    main_dict['role']['is_participant'] = user_profile == settings.PARTICIPANT

    return main_dict
