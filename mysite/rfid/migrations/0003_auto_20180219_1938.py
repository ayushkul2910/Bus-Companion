# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-02-19 14:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rfid', '0002_auto_20180219_1936'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cost',
            name='ID',
        ),
        migrations.AddField(
            model_name='cost',
            name='id',
            field=models.AutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
