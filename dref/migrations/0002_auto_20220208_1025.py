# Generated by Django 2.2.26 on 2022-02-08 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dref', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dref',
            name='total_targeted_population',
        ),
        migrations.AddField(
            model_name='dref',
            name='total_targeted_population',
            field=models.IntegerField(blank=True, help_text='Estimated number of targeted people', null=True, verbose_name='total targeted population'),
        ),
        migrations.AlterField(
            model_name='dref',
            name='anticipatory_actions',
            field=models.TextField(blank=True, help_text='Description of anticipatory actions or imminent disaster', null=True, verbose_name='anticipatory actions'),
        ),
        migrations.AlterField(
            model_name='identifiedneed',
            name='title',
            field=models.CharField(choices=[('shelter_and_basic_household_items', 'Shelter And Basic Household Items'), ('livelihoods_and_basic_needs', 'Livelihoods And Basic Needs'), ('health', 'Health'), ('water_sanitation_and_hygiene', 'Water, Sanitation And Hygiene'), ('protection_gender_and_inclusion', 'Protection, Gender And Inclusion'), ('education', 'Education'), ('migration', 'Migration'), ('risk_reduction_climate_adaptation_and_recovery', 'Risk Reduction, Climate Adaptation And Recovery'), ('community_engagement_and _accountability', 'Community Engagement And Accountability'), ('environment_sustainability ', 'Environment Sustainability'), ('shelter_cluster_coordination', 'Shelter Cluster Coordination')], max_length=255, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='nationalsocietyaction',
            name='title',
            field=models.CharField(choices=[('national_society_readiness', 'National Society Readiness'), ('assessment', 'Assessment'), ('coordination', 'Coordination'), ('resource_mobilization', 'Resource Mobilization'), ('activation_of_contingency_plans', 'Activation Of Contingency Plans'), ('national_society_eoc', 'National Society EOC'), ('shelter_and_basic_household_items', 'Shelter And Basic Household Items'), ('livelihoods_and_basic_needs', 'Livelihoods And Basic Needs'), ('health', 'Health'), ('water_sanitation_and_hygiene', 'Water, Sanitation And Hygiene'), ('protection_gender_and_inclusion', 'Protection, Gender And Inclusion'), ('education', 'Education'), ('migration', 'Migration'), ('risk_reduction_climate_adaptation_and_recovery', 'Risk Reduction, Climate Adaptation And Recovery'), ('community_engagement_and _accountability', 'Community Engagement And Accountability'), ('environment_sustainability ', 'Environment Sustainability'), ('other', 'Other')], max_length=255, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='plannedintervention',
            name='title',
            field=models.CharField(choices=[('shelter_and_basic_household_items', 'Shelter And Basic Household Items'), ('livelihoods_and_basic_needs', 'Livelihoods And Basic Needs'), ('health', 'Health'), ('water_sanitation_and_hygiene', 'Water, Sanitation And Hygiene'), ('protection_gender_and_inclusion', 'Protection, Gender And Inclusion'), ('education', 'Education'), ('migration', 'Migration'), ('risk_reduction_climate_adaptation_and_recovery_', 'Risk Reduction, Climate Adaptation And Recovery'), ('secretariat_services', 'Secretariat Services'), ('national_society_strengthening', 'National Society Strengthening')], max_length=255, verbose_name='title'),
        ),
    ]
