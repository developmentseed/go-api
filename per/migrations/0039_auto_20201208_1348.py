# Generated by Django 2.2.13 on 2020-12-08 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('per', '0038_auto_20201130_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='overview',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='forms', to='per.Overview', verbose_name='overview'),
        ),
    ]