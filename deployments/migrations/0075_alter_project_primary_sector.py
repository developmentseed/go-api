# Generated by Django 3.2.18 on 2023-03-07 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('deployments', '0074_alter_molnixtag_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='primary_sector',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='deployments.sector', verbose_name='sector'),
        ),
    ]