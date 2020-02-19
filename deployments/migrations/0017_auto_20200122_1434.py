# Generated by Django 2.2.9 on 2020-01-22 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deployments', '0016_auto_20200107_0855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personnel',
            name='type',
            field=models.CharField(choices=[('fact', 'FACT'), ('heop', 'HEOP'), ('rdrt', 'RDRT'), ('ifrc', 'IFRC'), ('eru', 'ERU HR'), ('rr', 'Rapid Response')], max_length=4),
        ),
    ]