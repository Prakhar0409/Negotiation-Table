# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-20 19:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netIITD', '0005_auto_20160920_1827'),
    ]

    operations = [
        migrations.AddField(
            model_name='nation',
            name='prod_units',
            field=models.IntegerField(default=3),
        ),
    ]
