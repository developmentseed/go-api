# Generated by Django 2.2.13 on 2020-12-14 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('per', '0039_auto_20201208_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='overview',
            name='facilitator_contact',
            field=models.CharField(blank=True, max_length=90, null=True, verbose_name='facilitator other contacts'),
        ),
        migrations.AlterField(
            model_name='overview',
            name='facilitator_email',
            field=models.CharField(blank=True, max_length=90, null=True, verbose_name='facilitator email'),
        ),
        migrations.AlterField(
            model_name='overview',
            name='facilitator_phone',
            field=models.CharField(blank=True, max_length=90, null=True, verbose_name='facilitator phone'),
        ),
    ]
