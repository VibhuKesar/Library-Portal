# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-10-31 15:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acelibraryapp', '0002_auto_20161030_0246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='author',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='problem',
            name='solution',
            field=models.TextField(null=True),
        ),
    ]
