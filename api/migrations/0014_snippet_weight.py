# Generated by Django 2.0.12 on 2019-02-25 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_auto_20181120_1038'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='weight',
            field=models.IntegerField(default=10),
        ),
    ]