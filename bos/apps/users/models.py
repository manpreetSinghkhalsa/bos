# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import hashlib

from django.conf import settings
from django.db import models
from django.contrib.auth.models import User as django_user
from django.utils.translation import ugettext_lazy as _


class User(django_user):

    django_user.email = models.EmailField(unique=True)

    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'password']
    USERNAME_FIELD = 'email'

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

    PROFILE_CHOICES = (
        (settings.ADMIN, 'Admin'),
        (settings.CO_ADMIN, 'Co-admin'),
        (settings.VOLUNTEER, 'Volunteer'),
        (settings.PARTICIPANT, 'Participant'),
    )

    PROFILE_GROUP_DICT = {
        settings.ADMIN: 'admin',
        settings.CO_ADMIN: 'co-admin',
        settings.VOLUNTEER: 'volunteer',
        settings.PARTICIPANT: 'participant'
    }

    profile = models.CharField(max_length=1, choices=PROFILE_CHOICES)
    user = models.OneToOneField(User)

    class Meta:
        unique_together = (('user', 'profile'), )

    def __unicode__(self):
        return "{} {}".format(self.user, self.profile)
