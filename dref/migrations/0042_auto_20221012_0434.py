# Generated by Django 3.2.15 on 2022-10-12 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dref', '0041_auto_20221010_0650'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drefoperationalupdate',
            name='has_event_occured',
        ),
        migrations.AddField(
            model_name='drefoperationalupdate',
            name='has_event_occurred',
            field=models.BooleanField(blank=True, help_text='Has Event occurred', null=True),
        ),
    ]