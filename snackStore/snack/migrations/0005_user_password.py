# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-24 00:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snack', '0004_remove_snack_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.TextField(default='', verbose_name='Password'),
        ),
    ]
