# Generated by Django 2.2.27 on 2022-03-23 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deployments', '0058_auto_20220322_1056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emergencyprojectactivity',
            name='is_disaggregated_for_disabled',
            field=models.NullBooleanField(verbose_name='is_disaggregated_for_disabled'),
        ),
    ]