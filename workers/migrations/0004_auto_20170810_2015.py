# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-10 17:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0003_auto_20170810_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='timeout',
            field=models.IntegerField(default=5, verbose_name='Worker timeout, s'),
        ),
        migrations.AlterField(
            model_name='worker',
            name='worker_name',
            field=models.CharField(choices=[('grab', 'Grab worker'), ('zip', 'Zip worker'), ('report', 'Report worker')], max_length=20, unique=True, verbose_name='Worker name'),
        ),
    ]