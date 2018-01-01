# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(_('first name'), max_length=50)
    middle_name = models.CharField(_('middle name'), max_length=50, blank=True, null=True)
    last_name = models.CharField(_('last name'), max_length=100)
    email = models.EmailField(_('email address'), unique=True)

    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    location = models.ForeignKey(Location)

    # System fields
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'password']

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

    def clean(self):
        super(User, self).clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '{} {}'.format(self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Returns the short name for the user."""
        return self.first_name


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


class Location(models.Model):
    """

    """
    country = models.CharField(max_length=200, unique=True)
    state = models.CharField(max_length=200, unique=True)
    city = models.CharField(max_length=200, unique=True)
    pincode = models.CharField(max_length=6, unique=True)

    def __unicode__(self):
        return u'state: {}, city: {}, pincode: {}, country: {}'.format(self.state, self.city, self.pincode, self.country)