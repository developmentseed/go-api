# Generated by Django 2.2.13 on 2021-03-02 11:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0124_merge_20210414_0714'),
    ]

    operations = [
        migrations.CreateModel(
            name='ERPGUID',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('api_guid', models.CharField(help_text='Can be used to do a GET request to check on the microservice API side.', max_length=200)),
                ('field_report', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.FieldReport', verbose_name='field report')),
            ],
        ),
    ]
