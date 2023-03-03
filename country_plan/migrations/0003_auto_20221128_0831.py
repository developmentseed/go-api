# Generated by Django 3.2.16 on 2022-11-28 08:31

import country_plan.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('country_plan', '0002_alter_countryplan_is_publish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='countryplan',
            name='internal_plan_file',
            field=models.FileField(blank=True, null=True, upload_to=country_plan.models.pdf_upload_to, validators=[django.core.validators.FileExtensionValidator(['pdf'])], verbose_name='Internal Plan'),
        ),
        migrations.AlterField(
            model_name='countryplan',
            name='public_plan_file',
            field=models.FileField(blank=True, null=True, upload_to=country_plan.models.pdf_upload_to, validators=[django.core.validators.FileExtensionValidator(['pdf'])], verbose_name='Country Plan'),
        ),
        migrations.AlterField(
            model_name='strategicpriority',
            name='type',
            field=models.CharField(choices=[('ongoing_emergency_operations', 'Ongoing emergency operations'), ('climate_and_environmental_crisis', 'Climate and environmental crisis'), ('evolving_crisis_and_disasters', 'Evolving crisis and disasters'), ('growing_gaps_in_health_and_wellbeing', 'Growing gaps in health and wellbeing'), ('migration_and_identity', 'Migration and Identity'), ('value_power_and_inclusion', 'Value power and inclusion')], max_length=100, verbose_name='Type'),
        ),
    ]