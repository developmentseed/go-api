# Generated by Django 2.2.13 on 2020-11-23 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('per', '0035_overview_assessment_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formdata',
            name='form',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='form_data', to='per.Form', verbose_name='form'),
        ),
    ]
