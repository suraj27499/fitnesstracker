# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-23 17:45
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0019_auto_20160526_2201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='backtracker',
            name='back',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='basictracker',
            name='weight',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='bisceptracker',
            name='biscep',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='chesttracker',
            name='chest',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='hiptracker',
            name='hip',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='shouldertracker',
            name='shoulder',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='subscription_startdate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2016, 6, 23, 23, 15, 23, 708544)),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='subscription_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='thightracker',
            name='thigh',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='userprofile_extended',
            name='contact',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]