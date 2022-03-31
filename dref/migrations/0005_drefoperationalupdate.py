# Generated by Django 2.2.27 on 2022-03-31 08:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0151_merge_20220325_1027'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dref', '0004_dref_is_published'),
    ]

    operations = [
        migrations.CreateModel(
            name='DrefOperationalUpdate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='modified at')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('type_of_onset', models.IntegerField(blank=True, choices=[(0, 'Imminent'), (1, 'Slow'), (2, 'Sudden')], null=True, verbose_name='onset type')),
                ('disaster_category', models.IntegerField(blank=True, choices=[(0, 'Yellow'), (1, 'Orange'), (2, 'Red')], null=True, verbose_name='disaster category')),
                ('number_of_people_targated', models.IntegerField(blank=True, null=True, verbose_name='Number of people targated')),
                ('number_of_people_affected', models.IntegerField(blank=True, null=True, verbose_name='number of people affected')),
                ('dref_allocated_so_far', models.IntegerField(blank=True, null=True, verbose_name='Dref allocated so far')),
                ('additional_allocation', models.IntegerField(blank=True, null=True, verbose_name='Additional allocation')),
                ('total_dref_allocation', models.IntegerField(blank=True, null=True, verbose_name='Total dref allocation')),
                ('emergency_appeal_planned', models.BooleanField(blank=True, null=True, verbose_name='emergency appeal planned ')),
                ('operational_update_number', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Operational Update Number')),
                ('reporting_timeframe', models.DateTimeField(blank=True, null=True, verbose_name='Reporting Timeframe')),
                ('is_timeframe_extension_required', models.BooleanField(blank=True, null=True, verbose_name='Is Timeframe Extension Required')),
                ('new_operational_end_date', models.DateTimeField(blank=True, null=True, verbose_name='New Operation End Date')),
                ('total_operation_timeframe', models.IntegerField(blank=True, null=True, verbose_name='Total Operation Timeframe')),
                ('date_of_approval', models.DateField(blank=True, null=True, verbose_name='Date of Approval')),
                ('appeal_code', models.CharField(blank=True, max_length=255, null=True, verbose_name='appeal code')),
                ('glide_code', models.CharField(blank=True, max_length=255, null=True, verbose_name='glide number')),
                ('ifrc_appeal_manager_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='ifrc appeal manager name')),
                ('ifrc_appeal_manager_email', models.CharField(blank=True, max_length=255, null=True, verbose_name='ifrc appeal manager email')),
                ('ifrc_appeal_manager_title', models.CharField(blank=True, max_length=255, null=True, verbose_name='ifrc appeal manager title')),
                ('ifrc_appeal_manager_phone_number', models.CharField(blank=True, max_length=100, null=True, verbose_name='ifrc appeal manager phone number')),
                ('ifrc_project_manager_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='ifrc project manager name')),
                ('ifrc_project_manager_email', models.CharField(blank=True, max_length=255, null=True, verbose_name='ifrc project manager email')),
                ('ifrc_project_manager_title', models.CharField(blank=True, max_length=255, null=True, verbose_name='ifrc project manager title')),
                ('ifrc_project_manager_phone_number', models.CharField(blank=True, max_length=100, null=True, verbose_name='ifrc project manager phone number')),
                ('national_society_contact_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='national society contact name')),
                ('national_society_contact_email', models.CharField(blank=True, max_length=255, null=True, verbose_name='national society contact email')),
                ('national_society_contact_title', models.CharField(blank=True, max_length=255, null=True, verbose_name='national society contact title')),
                ('national_society_contact_phone_number', models.CharField(blank=True, max_length=100, null=True, verbose_name='national society contact phone number')),
                ('media_contact_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='media contact name')),
                ('media_contact_email', models.CharField(blank=True, max_length=255, null=True, verbose_name='media contact email')),
                ('media_contact_title', models.CharField(blank=True, max_length=255, null=True, verbose_name='media contact title')),
                ('media_contact_phone_number', models.CharField(blank=True, max_length=100, null=True, verbose_name='media_contact phone number')),
                ('ifrc_emergency_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='ifrc emergency name')),
                ('ifrc_emergency_email', models.CharField(blank=True, max_length=255, null=True, verbose_name='ifrc emergency email')),
                ('ifrc_emergency_title', models.CharField(blank=True, max_length=255, null=True, verbose_name='ifrc emergency title')),
                ('ifrc_emergency_phone_number', models.CharField(blank=True, max_length=100, null=True, verbose_name='ifrc emergency phone number')),
                ('changing_timeframe_operation', models.BooleanField(blank=True, null=True, verbose_name='Changing time operation')),
                ('changing_operation_strategy', models.BooleanField(blank=True, null=True, verbose_name='Changing operation strategy')),
                ('changing_target_population_of_operation', models.BooleanField(blank=True, null=True, verbose_name='Changing target population of operation')),
                ('changing_geographic_location', models.BooleanField(blank=True, null=True, verbose_name='Changing geographic location')),
                ('changing_budget', models.BooleanField(blank=True, null=True, verbose_name='Changing budget')),
                ('request_for_second_allocation', models.BooleanField(blank=True, null=True, verbose_name='Request for second allocation')),
                ('summary_of_change', models.TextField(blank=True, null=True, verbose_name='Summary of change')),
                ('change_since_request', models.TextField(blank=True, null=True, verbose_name='Change since request')),
                ('ifrc', models.TextField(blank=True, null=True, verbose_name='ifrc')),
                ('icrc', models.TextField(blank=True, null=True, verbose_name='icrc')),
                ('partner_national_society', models.TextField(blank=True, null=True, verbose_name='partner national society')),
                ('government_requested_assistance', models.BooleanField(blank=True, help_text='Has government requested assistance', null=True)),
                ('national_authorities', models.TextField(blank=True, null=True, verbose_name='national authorities')),
                ('un_or_other_actor', models.TextField(blank=True, null=True, verbose_name='un or other')),
                ('major_coordination_mechanism', models.TextField(blank=True, null=True, verbose_name='major coordination mechanism')),
                ('people_assisted', models.TextField(blank=True, null=True, verbose_name='people assisted')),
                ('selection_criteria', models.TextField(blank=True, help_text='Selection criteria for affected people', null=True, verbose_name='selection criteria')),
                ('community_involved', models.TextField(blank=True, help_text='Community been involved in the analysis of the process', null=True, verbose_name='community involved')),
                ('women', models.IntegerField(blank=True, null=True, verbose_name='women')),
                ('men', models.IntegerField(blank=True, null=True, verbose_name='men')),
                ('girls', models.IntegerField(blank=True, help_text='Girls under 18', null=True, verbose_name='girls')),
                ('boys', models.IntegerField(blank=True, help_text='Boys under 18', null=True, verbose_name='boys')),
                ('disability_people_per', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='disability people per')),
                ('people_per_urban', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='people per urban')),
                ('people_per_local', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='people per local')),
                ('people_targeted_with_early_actions', models.IntegerField(blank=True, null=True, verbose_name='people targeted with early actions')),
                ('displaced_people', models.IntegerField(blank=True, null=True, verbose_name='displaced people')),
                ('operation_objective', models.TextField(blank=True, null=True, verbose_name='operation objective')),
                ('response_strategy', models.TextField(blank=True, null=True, verbose_name='response strategy')),
                ('country', models.ForeignKey(help_text='Affected County', on_delete=django.db.models.deletion.CASCADE, to='api.Country', verbose_name='country')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_by_dref_operational_update', to=settings.AUTH_USER_MODEL, verbose_name='created by')),
                ('disaster_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.DisasterType', verbose_name='disaster type')),
                ('district', models.ManyToManyField(blank=True, to='api.District', verbose_name='district')),
                ('dref', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dref.Dref', verbose_name='Dref')),
                ('images', models.ManyToManyField(blank=True, related_name='image_dref_operational_update', to='dref.DrefFile', verbose_name='images')),
                ('modified_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='modified_by_dref_operational_update', to=settings.AUTH_USER_MODEL, verbose_name='modified by')),
                ('national_society', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='national_society_operational_update', to='api.Country', verbose_name='national_society')),
                ('national_society_actions', models.ManyToManyField(blank=True, to='dref.NationalSocietyAction', verbose_name='national society actions')),
                ('needs_identified', models.ManyToManyField(blank=True, to='dref.IdentifiedNeed', verbose_name='needs identified')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dref.DrefOperationalUpdate')),
                ('planned_interventions', models.ManyToManyField(blank=True, to='dref.PlannedIntervention', verbose_name='planned intervention')),
            ],
            options={
                'verbose_name': 'Dref Operational Update',
                'verbose_name_plural': 'Dref Operational Updates',
            },
        ),
    ]
