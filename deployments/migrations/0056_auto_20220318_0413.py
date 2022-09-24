# Generated by Django 2.2.27 on 2022-03-18 04:13

import deployments.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deployments', '0055_auto_20220315_0420'),
    ]

    operations = [
        migrations.AddField(
            model_name='emergencyprojectactivityaction',
            name='has_location',
            field=models.BooleanField(default=False, verbose_name='has location'),
        ),
        migrations.AlterField(
            model_name='emergencyproject',
            name='status',
            field=models.CharField(choices=[('on_going', 'Activity Ongoing'), ('complete', 'Activity Complete'), ('planned', 'Planned')], default=deployments.models.EmergencyProject.ActivityStatus('on_going'), max_length=40),
        ),
    ]
