# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-01 15:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_remove_sporthalladdress_sport_hall'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='futsal_team',
        ),
    ]
