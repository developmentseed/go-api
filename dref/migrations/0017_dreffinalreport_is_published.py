# Generated by Django 2.2.27 on 2022-06-27 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dref', '0016_dref_is_final_report_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='dreffinalreport',
            name='is_published',
            field=models.BooleanField(default=False, verbose_name='Is Published'),
        ),
    ]
