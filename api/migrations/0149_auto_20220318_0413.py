# Generated by Django 2.2.27 on 2022-03-18 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0148_auto_20220314_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='average_household_size',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Average Household Size'),
        ),
    ]