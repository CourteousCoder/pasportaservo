# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-07 15:50
from __future__ import unicode_literals

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosting', '0037_add_countrygroup_proxy_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='InstanceApprover',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
