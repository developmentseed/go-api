# Generated by Django 2.2.27 on 2022-02-28 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0145_auto_20220218_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generaldocument',
            name='created_at',
            field=models.DateTimeField(blank=True, verbose_name='created at'),
        ),
    ]
