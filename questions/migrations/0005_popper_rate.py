# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-04 13:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0004_new_arrival'),
    ]

    operations = [
        migrations.AddField(
            model_name='popper',
            name='rate',
            field=models.TextField(default='', max_length=1024),
        ),
    ]
