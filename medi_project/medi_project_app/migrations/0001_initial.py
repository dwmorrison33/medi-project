# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-03-21 15:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('code', models.CharField(max_length=254)),
                ('product_type', models.CharField(max_length=254)),
                ('cost', models.IntegerField()),
                ('description', models.CharField(max_length=254)),
                ('pushed_product', models.BooleanField(default=False)),
                ('callback', models.CharField(max_length=254)),
                ('category', models.CharField(max_length=254)),
                ('inventory_on_hand', models.IntegerField(default=1)),
                ('photo', models.FileField(upload_to=b'products')),
            ],
        ),
    ]
