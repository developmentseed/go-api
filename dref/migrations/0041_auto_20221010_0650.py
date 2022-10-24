# Generated by Django 3.2.15 on 2022-10-10 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dref', '0040_auto_20221010_0621'),
    ]

    operations = [
        migrations.AddField(
            model_name='drefoperationalupdate',
            name='communication',
            field=models.TextField(blank=True, help_text='Does the NS have Communications capacity?', null=True, verbose_name='organization'),
        ),
        migrations.AddField(
            model_name='drefoperationalupdate',
            name='human_resource',
            field=models.TextField(blank=True, help_text='how many volunteers and staff involved in the response?', null=True, verbose_name='human resource'),
        ),
        migrations.AddField(
            model_name='drefoperationalupdate',
            name='is_surge_personnel_deployed',
            field=models.BooleanField(blank=True, null=True, verbose_name='Is surge personnel deployed'),
        ),
        migrations.AddField(
            model_name='drefoperationalupdate',
            name='logistic_capacity_of_ns',
            field=models.TextField(blank=True, help_text='what is the logistics capacity of the National Society?', null=True, verbose_name='logistic capacity of ns'),
        ),
        migrations.AddField(
            model_name='drefoperationalupdate',
            name='pmer',
            field=models.TextField(blank=True, help_text='Does the NS have PMER capacity?', null=True, verbose_name='pmer'),
        ),
        migrations.AddField(
            model_name='drefoperationalupdate',
            name='safety_concerns',
            field=models.TextField(blank=True, help_text='Are there any safety/security concerns which may impact the implementation of this operation?', null=True, verbose_name='safety concerns'),
        ),
        migrations.AddField(
            model_name='drefoperationalupdate',
            name='surge_personnel_deployed',
            field=models.TextField(blank=True, help_text='Will a Surge personnel be deployed?', null=True, verbose_name='surge personnel deployed'),
        ),
        migrations.AlterField(
            model_name='drefoperationalupdate',
            name='event_date',
            field=models.DateField(blank=True, null=True, verbose_name='event date'),
        ),
        migrations.AlterField(
            model_name='drefoperationalupdate',
            name='ns_respond_date',
            field=models.DateField(blank=True, null=True, verbose_name='ns respond date'),
        ),
        migrations.AlterField(
            model_name='drefoperationalupdate',
            name='total_targeted_population',
            field=models.IntegerField(blank=True, null=True, verbose_name='total targeted population'),
        ),
    ]