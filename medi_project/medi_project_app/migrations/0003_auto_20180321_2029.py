# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-03-21 20:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medi_project_app', '0002_auto_20180321_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerpurchase',
            name='confirmation_code',
            field=models.CharField(max_length=254),
        ),
    ]