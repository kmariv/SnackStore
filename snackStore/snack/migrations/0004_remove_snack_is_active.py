# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-24 00:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snack', '0003_snack_popularity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='snack',
            name='is_active',
        ),
    ]
