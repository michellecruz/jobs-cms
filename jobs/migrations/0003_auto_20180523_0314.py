# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2018-05-23 03:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20180523_0305'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='job',
            options={'ordering': ['-date_added']},
        ),
        migrations.RenameField(
            model_name='job',
            old_name='created_at',
            new_name='date_added',
        ),
        migrations.RemoveField(
            model_name='company',
            name='website',
        ),
        migrations.AddField(
            model_name='job',
            name='link',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
    ]
