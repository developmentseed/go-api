# Generated by Django 2.0.12 on 2019-12-19 11:15

import django.contrib.postgres.fields.jsonb
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('api', '0036_auto_20191215_0615'),
    ]

    operations = [
        migrations.CreateModel(
            name='CountryOverview',
            fields=[
                ('country', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='api.Country')),
                ('script_modified_at', models.DateTimeField(blank=True, null=True)),
                ('population', models.IntegerField(blank=True, null=True)),
                ('gdp', models.FloatField(blank=True, null=True, verbose_name='GDP')),
                ('gnipc', models.IntegerField(blank=True, null=True, verbose_name='GNI/CAPITA')),
                ('life_expectancy', models.IntegerField(blank=True, null=True)),
                ('urban_population', models.FloatField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)], verbose_name='Urban POP (%)')),
                ('poverty', models.FloatField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)], verbose_name='Poverty (%)')),
                ('literacy', models.FloatField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)], verbose_name='Literacy (%)')),
                ('income', models.FloatField(blank=True, null=True, verbose_name='Income (CHF)')),
                ('expenditures', models.FloatField(blank=True, null=True, verbose_name='Expenditures (CHF)')),
                ('volunteers', models.IntegerField(blank=True, null=True)),
                ('trained_in_first_aid', models.IntegerField(blank=True, null=True)),
                ('avg_temperature', models.FloatField(blank=True, null=True)),
                ('avg_rainfall_precipitation', models.FloatField(blank=True, null=True)),
                ('rainy_season', models.CharField(blank=True, choices=[('active', 'Active'), ('not_active', 'Not Active')], max_length=20, null=True)),
                ('fts_data', django.contrib.postgres.fields.jsonb.JSONField(default=list)),
                ('start_network_data', django.contrib.postgres.fields.jsonb.JSONField(default=list)),
                ('past_crises_events', django.contrib.postgres.fields.jsonb.JSONField(default=list)),
                ('past_epidemics', django.contrib.postgres.fields.jsonb.JSONField(default=list)),
                ('inform_indicators', django.contrib.postgres.fields.jsonb.JSONField(default=list)),
            ],
        ),
        migrations.CreateModel(
            name='KeyClimateEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('month', models.PositiveSmallIntegerField(choices=[(1, 'January'), (2, 'February'), (3, 'March'), (4, 'April'), (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'), (9, 'September'), (10, 'October'), (11, 'November'), (12, 'December')])),
                ('avg_max_temperature', models.FloatField()),
                ('avg_min_temperature', models.FloatField()),
                ('avg_rainfall_precipitation', models.FloatField()),
                ('overview', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='databank.CountryOverview')),
            ],
        ),
        migrations.CreateModel(
            name='SeasonalCalender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=20)),
                ('sector', models.CharField(max_length=20)),
                ('date_start', models.DateField()),
                ('date_end', models.DateField()),
                ('overview', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='databank.CountryOverview')),
            ],
        ),
        migrations.CreateModel(
            name='SocialEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=255)),
                ('value', models.CharField(max_length=255)),
                ('overview', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='databank.CountryOverview')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='socialevent',
            unique_together={('overview', 'label')},
        ),
        migrations.AlterUniqueTogether(
            name='seasonalcalender',
            unique_together={('overview', 'sector', 'title')},
        ),
        migrations.AlterUniqueTogether(
            name='keyclimateevent',
            unique_together={('overview', 'month')},
        ),
    ]
