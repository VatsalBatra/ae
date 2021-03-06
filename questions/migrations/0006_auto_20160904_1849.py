# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-04 13:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0005_popper_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='balloon',
            name='rate',
            field=models.TextField(default='', max_length=1024),
        ),
        migrations.AddField(
            model_name='candle',
            name='rate',
            field=models.TextField(default='', max_length=1024),
        ),
        migrations.AddField(
            model_name='cap',
            name='rate',
            field=models.TextField(default='', max_length=1024),
        ),
        migrations.AddField(
            model_name='crown',
            name='rate',
            field=models.TextField(default='', max_length=1024),
        ),
        migrations.AddField(
            model_name='knife_caketag',
            name='rate',
            field=models.TextField(default='', max_length=1024),
        ),
        migrations.AddField(
            model_name='new_arrival',
            name='rate',
            field=models.TextField(default='', max_length=1024),
        ),
        migrations.AddField(
            model_name='prop_decoration',
            name='rate',
            field=models.TextField(default='', max_length=1024),
        ),
    ]
