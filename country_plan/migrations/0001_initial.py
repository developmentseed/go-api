# Generated by Django 3.2.16 on 2022-11-24 05:11

import country_plan.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('api', '0160_merge_0159_auto_20221022_1542_0159_auto_20221028_0940'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CountryPlan',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('country', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='country_plan', serialize=False, to='api.country')),
                ('internal_plan_file', models.FileField(blank=True, null=True, upload_to=country_plan.models.pdf_upload_to, verbose_name='Internal Plan')),
                ('public_plan_file', models.FileField(blank=True, null=True, upload_to=country_plan.models.pdf_upload_to, verbose_name='Country Plan')),
                ('requested_amount', models.FloatField(blank=True, null=True, verbose_name='Requested Amount')),
                ('people_targeted', models.IntegerField(blank=True, null=True, verbose_name='People Targeted')),
                ('is_publish', models.BooleanField(default=False)),
                ('created_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='countryplan_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Created By')),
                ('updated_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='countryplan_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='Updated by')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DataImport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('file', models.FileField(upload_to=country_plan.models.file_upload_to, verbose_name='EXCEL file')),
                ('errors', models.JSONField(blank=True, null=True)),
                ('created_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dataimport_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Created By')),
                ('updated_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dataimport_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='Updated by')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StrategicPriority',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('climate_and_environmental_crisis', 'Climate and environmental crisis'), ('evolving_crisis_and_disasters', 'Evolving crisis and disasters'), ('growing_gaps_in_health_and_wellbeing', 'Growing gaps in health and wellbeing'), ('migration_and_identity', 'Migration and Identity'), ('value_power_and_inclusion', 'Value power and inclusion')], max_length=100, verbose_name='Type')),
                ('funding_requirement', models.FloatField(blank=True, null=True, verbose_name='Funding Requirement')),
                ('people_targeted', models.IntegerField(blank=True, null=True, verbose_name='People Targeted')),
                ('country_plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='country_plan_sp', to='country_plan.countryplan', verbose_name='Country Plan')),
            ],
            options={
                'unique_together': {('country_plan', 'type')},
            },
        ),
        migrations.CreateModel(
            name='MembershipCoordination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sector', models.CharField(choices=[('climate', 'Climate'), ('crisis', 'Crisis'), ('health', 'Health'), ('migration', 'Migration'), ('inclusion', 'Inclusion'), ('engaged', 'Engaged'), ('accountable', 'Accountable'), ('trusted', 'Trusted')], max_length=100, verbose_name='Sector')),
                ('has_coordination', models.BooleanField(default=False)),
                ('country_plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='country_plan_mc', to='country_plan.countryplan', verbose_name='Country Plan')),
                ('national_society', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='national_society_mc', to='api.country')),
            ],
            options={
                'unique_together': {('country_plan', 'national_society', 'sector')},
            },
        ),
    ]