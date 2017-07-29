# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-29 18:35
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=512, unique=True, validators=[django.core.validators.RegexValidator(code='invalid_username', message='Username must be Alpahnumeric or contain any of the following: ". @ + -" ', regex='^[a-zA-Z0-9.+-]*$')]),
        ),
    ]
