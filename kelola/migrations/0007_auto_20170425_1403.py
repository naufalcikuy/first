# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-25 07:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kelola', '0006_auto_20170425_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date_event',
            field=models.DateField(null=True),
        ),
    ]
