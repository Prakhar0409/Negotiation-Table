# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-20 20:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netIITD', '0007_loantrans'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='base_price',
            field=models.IntegerField(default=1000),
        ),
    ]
