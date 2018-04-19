# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2018-04-19 20:58
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('howdy', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='description',
            new_name='short_description',
        ),
        migrations.AddField(
            model_name='job',
            name='long_description',
            field=models.CharField(default=datetime.datetime(2018, 4, 19, 20, 58, 39, 434302, tzinfo=utc), max_length=2000),
            preserve_default=False,
        ),
    ]
