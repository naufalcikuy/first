# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-03 06:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kelola', '0004_babybio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='babybio',
            name='headcircumference_birth',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='babybio',
            name='height_birth',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='babybio',
            name='weight_birth',
            field=models.IntegerField(),
        ),
    ]
