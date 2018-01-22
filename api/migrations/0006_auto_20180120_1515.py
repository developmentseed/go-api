# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-20 15:15
from __future__ import unicode_literals

import api.models
from django.db import migrations, models
import enumfields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20180117_2323'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='alert_level',
            field=enumfields.fields.EnumIntegerField(default=0, enum=api.models.AlertLevel),
        ),
        migrations.AddField(
            model_name='event',
            name='glide',
            field=models.CharField(blank=True, max_length=18),
        ),
        migrations.AlterField(
            model_name='gdacsevent',
            name='alert_level',
            field=enumfields.fields.EnumIntegerField(default=0, enum=api.models.AlertLevel),
        ),
    ]
