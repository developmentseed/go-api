# Generated by Django 2.2.27 on 2022-07-27 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dref', '0022_auto_20220727_0536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='risksecurity',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Title'),
        ),
    ]
