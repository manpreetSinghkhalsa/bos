# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-01 08:11
from __future__ import unicode_literals

import bos.apps.users.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(max_length=50, verbose_name='first name')),
                ('middle_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='middle name')),
                ('last_name', models.CharField(max_length=100, verbose_name='last name')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'permissions': (('can_create_admin', 'Can create admin'), ('can_create_co_admin', 'Can create co-admin'), ('can_create_volunteer', 'Can create volunteer'), ('can_create_participant', 'Can create participant'), ('can_edit_admin', 'Can edit admin'), ('can_edit_co_admin', 'Can edit co-admin'), ('can_edit_volunteer', 'Can edit volunteer'), ('can_edit_participant', 'Can edit participant'), ('can_delete_admin', 'Can delete admin'), ('can_delete_co_admin', 'Can delete co-admin'), ('can_delete_volunteer', 'Can delete volunteer'), ('can_delete_participant', 'Can delete participant')),
            },
            managers=[
                ('objects', bos.apps.users.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.CharField(choices=[(b'1', 'Admin'), (b'2', 'Co-admin'), (b'3', 'Volunteer'), (b'4', 'Participant')], max_length=1)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.User')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='userprofile',
            unique_together=set([('user', 'profile')]),
        ),
    ]
