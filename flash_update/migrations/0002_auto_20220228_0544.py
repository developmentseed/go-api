# Generated by Django 2.2.27 on 2022-02-28 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flash_update', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DonorGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
            ],
        ),
        migrations.AddField(
            model_name='donors',
            name='groups',
            field=models.ManyToManyField(blank=True, to='flash_update.DonorGroup', verbose_name='donor group'),
        ),
    ]
