# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-07 19:00
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180208_0029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 7, 19, 0, 30, 529981, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 7, 19, 0, 30, 528480, tzinfo=utc)),
        ),
    ]
