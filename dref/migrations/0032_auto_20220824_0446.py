# Generated by Django 2.2.27 on 2022-08-24 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dref', '0031_auto_20220819_0844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='risksecurity',
            name='mitigation',
            field=models.TextField(blank=True, null=True, verbose_name='Mitigation'),
        ),
        migrations.AlterField(
            model_name='risksecurity',
            name='risk',
            field=models.TextField(blank=True, null=True, verbose_name='Risk'),
        ),
    ]
