# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-02-11 10:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('From', models.CharField(max_length=200)),
                ('To', models.CharField(max_length=200)),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
