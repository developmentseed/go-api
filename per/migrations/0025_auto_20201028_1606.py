# Generated by Django 2.2.13 on 2020-10-28 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('per', '0024_formcomponent_component_letter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='form',
            name='language',
        ),
        migrations.AddField(
            model_name='form',
            name='saved_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='saved at'),
        ),
        migrations.AddField(
            model_name='form',
            name='started_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='started at'),
        ),
        migrations.AddField(
            model_name='form',
            name='submitted_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='updated at'),
        ),
        migrations.AddField(
            model_name='overview',
            name='is_draft',
            field=models.BooleanField(default=True, verbose_name='is draft'),
        ),
    ]
