# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-18 09:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0006_auto_20160418_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile_extended',
            name='goal',
            field=models.CharField(blank=True, choices=[('1', 'Weight Loss'), ('2', 'Mass Gain'), ('3', 'Lean Muscle Gain'), ('4', 'Stay Fit')], max_length=1, null=True),
        ),
    ]
