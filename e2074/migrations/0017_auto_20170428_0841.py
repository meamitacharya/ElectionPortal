# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-28 08:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e2074', '0016_auto_20170428_0411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='party',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='party',
            name='slug',
            field=models.SlugField(unique=True),
        ),
        migrations.AlterField(
            model_name='politicaldiv',
            name='name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='politicaldiv',
            name='slug',
            field=models.SlugField(max_length=40, unique=True),
        ),
    ]