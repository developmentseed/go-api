# Generated by Django 2.2.13 on 2020-11-23 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('per', '0034_auto_20201119_1502'),
    ]

    operations = [
        migrations.AddField(
            model_name='overview',
            name='assessment_number',
            field=models.IntegerField(default=1, verbose_name='assessment number'),
        ),
    ]