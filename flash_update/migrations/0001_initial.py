# Generated by Django 2.2.27 on 2022-02-24 07:55

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import flash_update.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0011_update_proxy_permissions'),
        ('api', '0145_auto_20220218_1338'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization_name', models.CharField(blank=True, max_length=500, null=True)),
                ('first_name', models.CharField(blank=True, max_length=300, null=True)),
                ('last_name', models.CharField(blank=True, max_length=300, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('position', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FlashAction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400, verbose_name='name')),
                ('organizations', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('NTLS', 'National Society'), ('PNS', 'Foreign Society'), ('FDRN', 'Federation'), ('GOV', 'Government')], max_length=4), blank=True, default=list, size=None, verbose_name='organizations')),
                ('flash_update_types', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('EVT', 'Event'), ('EW', 'Early Warning'), ('EPI', 'Epidemic'), ('COVID', 'COVID-19')], max_length=16), default=list, size=None, verbose_name='flash update types')),
                ('category', models.CharField(choices=[('General', 'General'), ('Health', 'Health'), ('NS Institutional Strengthening', 'NS Institutional Strengthening'), ('Socioeconomic Interventions', 'Socioeconomic Interventions')], default='General', max_length=255, verbose_name='category')),
                ('is_disabled', models.BooleanField(default=False, help_text='Disable in form', verbose_name='is disabled?')),
                ('tooltip_text', models.TextField(blank='true', null=True, verbose_name='tooltip text')),
                ('client_id', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'verbose_name': 'flash action',
                'verbose_name_plural': 'flash actions',
            },
        ),
        migrations.CreateModel(
            name='FlashGraphicMap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='flash_update/images/', verbose_name='file')),
                ('caption', models.CharField(blank=True, max_length=225, null=True)),
                ('client_id', models.CharField(blank=True, max_length=50, null=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='created_by')),
            ],
            options={
                'verbose_name': 'flash graphic map',
                'verbose_name_plural': 'flash graphic maps',
            },
        ),
        migrations.CreateModel(
            name='FlashReferences',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, verbose_name='date')),
                ('source_description', models.CharField(blank=True, max_length=225, verbose_name='Name or Source Description')),
                ('url', models.TextField(blank=True)),
                ('client_id', models.CharField(blank=True, max_length=50, null=True)),
                ('document', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='flash_document', to='flash_update.FlashGraphicMap', verbose_name='document')),
            ],
            options={
                'verbose_name': 'flash reference',
                'verbose_name_plural': 'flash references',
            },
        ),
        migrations.CreateModel(
            name='FlashUpdate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('title', models.CharField(max_length=300)),
                ('title_en', models.CharField(max_length=300, null=True)),
                ('title_es', models.CharField(max_length=300, null=True)),
                ('title_fr', models.CharField(max_length=300, null=True)),
                ('title_ar', models.CharField(max_length=300, null=True)),
                ('situational_overview', models.TextField(verbose_name='Situational Overview')),
                ('situational_overview_en', models.TextField(null=True, verbose_name='Situational Overview')),
                ('situational_overview_es', models.TextField(null=True, verbose_name='Situational Overview')),
                ('situational_overview_fr', models.TextField(null=True, verbose_name='Situational Overview')),
                ('situational_overview_ar', models.TextField(null=True, verbose_name='Situational Overview')),
                ('originator_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='originator_name')),
                ('originator_title', models.CharField(blank=True, max_length=300, null=True, verbose_name='originator_title')),
                ('originator_email', models.CharField(blank=True, max_length=300, null=True, verbose_name='originator_email')),
                ('originator_phone', models.CharField(blank=True, max_length=50, null=True, verbose_name='originator_phone')),
                ('ifrc_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='ifrc_name')),
                ('ifrc_title', models.CharField(blank=True, max_length=300, null=True, verbose_name='ifrc_title')),
                ('ifrc_email', models.CharField(blank=True, max_length=300, null=True, verbose_name='ifrc_email')),
                ('ifrc_phone', models.CharField(blank=True, max_length=50, null=True, verbose_name='ifrc_phone')),
                ('share_with', models.CharField(blank=True, choices=[('ifrc_secretariat', 'IFRC Secretariat'), ('rcrc_network', 'RCRC Network'), ('rcrc_network_and_donors', 'RCRC Network and Donors')], max_length=50, null=True, verbose_name='share with')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='flash_update_created_by', to=settings.AUTH_USER_MODEL, verbose_name='created by')),
                ('graphics', models.ManyToManyField(blank=True, related_name='flash_graphics', to='flash_update.FlashGraphicMap', verbose_name='graphics')),
                ('hazard_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='flash_update_hazard_type', to='api.DisasterType', verbose_name='hazard type')),
                ('map', models.ManyToManyField(blank=True, related_name='flash_map', to='flash_update.FlashGraphicMap', verbose_name='map')),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='flash_update_modified_by', to=settings.AUTH_USER_MODEL, verbose_name='modified by')),
                ('references', models.ManyToManyField(blank=True, to='flash_update.FlashReferences', verbose_name='references')),
            ],
            options={
                'verbose_name': 'Flash update',
                'verbose_name_plural': 'Flash updates',
            },
        ),
        migrations.CreateModel(
            name='FlashEmailSubscriptions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('share_with', models.CharField(choices=[('ifrc_secretariat', 'IFRC Secretariat'), ('rcrc_network', 'RCRC Network'), ('rcrc_network_and_donors', 'RCRC Network and Donors')], default=flash_update.models.FlashUpdate.FlashShareWith('ifrc_secretariat'), max_length=50, verbose_name='share with')),
                ('group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='flash_email_subscription', to='auth.Group')),
            ],
        ),
        migrations.CreateModel(
            name='FlashActionsTaken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization', models.CharField(choices=[('NTLS', 'National Society'), ('PNS', 'Foreign Society'), ('FDRN', 'Federation'), ('GOV', 'Government')], max_length=16, verbose_name='organization')),
                ('summary', models.TextField(blank=True, null=True, verbose_name='summary')),
                ('client_id', models.CharField(blank=True, max_length=50, null=True)),
                ('actions', models.ManyToManyField(blank=True, to='flash_update.FlashAction', verbose_name='actions')),
                ('flash_update', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actions_taken_flash', to='flash_update.FlashUpdate', verbose_name='flash update')),
            ],
            options={
                'verbose_name': 'actions taken flash',
                'verbose_name_plural': 'all actions taken flash',
            },
        ),
        migrations.CreateModel(
            name='FlashCountryDistrict',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_id', models.CharField(blank=True, max_length=50, null=True)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flash_country', to='api.Country', verbose_name='country')),
                ('district', models.ManyToManyField(related_name='flash_district', to='api.District', verbose_name='district')),
                ('flash_update', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flash_update.FlashUpdate', verbose_name='Flash update')),
            ],
            options={
                'verbose_name': 'flash country district',
                'verbose_name_plural': 'flash countries districts',
                'unique_together': {('flash_update', 'country')},
            },
        ),
    ]