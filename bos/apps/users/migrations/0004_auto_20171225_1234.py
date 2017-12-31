# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-25 12:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20171225_0710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile',
            field=models.CharField(
                choices=[('1', 'Admin'), ('2', 'Co-admin'), ('3', 'Volunteer'), ('4', 'Participant')], max_length=1
            ),
        ),
    ]
