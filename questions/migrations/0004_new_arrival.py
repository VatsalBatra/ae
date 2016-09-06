# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-13 08:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_auto_20160727_1546'),
    ]

    operations = [
        migrations.CreateModel(
            name='New_Arrival',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100)),
                ('text', models.TextField(default='', max_length=1024)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
