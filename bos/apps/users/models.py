# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User as django_user
from django.utils.translation import ugettext_lazy as _


class User(django_user, models.Model):
    # phone_number = models.CharField(max_length=10, unique=True)
    # # TODO: Need to take a decision on this.
    # # username = models.CharField(
    # #     _('username'),
    # #     max_length=150,
    # #     help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
    # #     validators=[django_user.username_validator],
    # #     error_messages={
    # #         'unique': _("A user with that username already exists."),
    # #     }
    # # )
    # email = models.EmailField(_('email address'), unique=True)
    # django_user.first_name = models.CharField(_('first name'), max_length=100)
    # last_name = models.CharField(_('last name'), max_length=300)

    REQUIRED_FIELDS = ['email', 'username', 'first_name', 'last_name']

    class Meta:
        permissions = (
            ("can_create_admin", "Can create admin"),
            ("can_create_co_admin", "Can create co-admin"),
            ("can_create_volunteer", "Can create volunteer"),
            ("can_create_participant", "Can create participant"),

            ("can_edit_admin", "Can edit admin"),
            ("can_edit_co_admin", "Can edit co-admin"),
            ("can_edit_volunteer", "Can edit volunteer"),
            ("can_edit_participant", "Can edit participant"),

            ("can_delete_admin", "Can delete admin"),
            ("can_delete_co_admin", "Can delete co-admin"),
            ("can_delete_volunteer", "Can delete volunteer"),
            ("can_delete_participant", "Can delete participant"),
        )


class UserProfile(models.Model):
    """
    Defines the user-profile
    """
    ADMIN = '1'
    CO_ADMIN = '2'
    VOLUNTEER = '3'
    PARTICIPANT = '4'

    PROFILE_CHOICES = (
        (ADMIN, 'Admin'),
        (CO_ADMIN, 'Co-admin'),
        (VOLUNTEER, 'Volunteer'),
        (PARTICIPANT, 'Participant'),
    )

    PROFILE_GROUP_DICT = {
        ADMIN: 'admin',
        CO_ADMIN: 'co-admin',
        VOLUNTEER: 'volunteer',
        PARTICIPANT: 'participant'
    }

    profile = models.CharField(max_length=1, choices=PROFILE_CHOICES)
    user = models.OneToOneField(User)

    class Meta:
        unique_together = (('user', 'profile'), )

    def __unicode__(self):
        return "{} {}".format(self.user, self.profile)
