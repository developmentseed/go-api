# Generated by Django 2.2.13 on 2020-07-21 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0077_auto_20200721_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='district',
            name='country_iso',
            field=models.CharField(max_length=2, null=True, verbose_name='country ISO2'),
        ),
    ]