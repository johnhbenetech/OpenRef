# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-02-13 20:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20170213_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provider',
            name='updated_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]