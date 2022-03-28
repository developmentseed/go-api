# Generated by Django 2.2.27 on 2022-03-15 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deployments', '0054_auto_20220314_1059'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emergencyprojectactivity',
            old_name='disabled_female_18_29_count',
            new_name='disabled_female_18_59_count',
        ),
        migrations.RenameField(
            model_name='emergencyprojectactivity',
            old_name='disabled_male_18_29_count',
            new_name='disabled_male_18_59_count',
        ),
        migrations.RenameField(
            model_name='emergencyprojectactivity',
            old_name='disabled_other_18_29_count',
            new_name='disabled_other_18_59_count',
        ),
        migrations.RenameField(
            model_name='emergencyprojectactivity',
            old_name='female_18_29_count',
            new_name='female_18_59_count',
        ),
        migrations.RenameField(
            model_name='emergencyprojectactivity',
            old_name='male_18_29_count',
            new_name='male_18_59_count',
        ),
        migrations.RenameField(
            model_name='emergencyprojectactivity',
            old_name='other_18_29_count',
            new_name='other_18_59_count',
        ),
        migrations.RemoveField(
            model_name='emergencyprojectactivity',
            name='disabled_female_0_5_count',
        ),
        migrations.RemoveField(
            model_name='emergencyprojectactivity',
            name='disabled_female_30_39_count',
        ),
        migrations.RemoveField(
            model_name='emergencyprojectactivity',
            name='disabled_female_40_49_count',
        ),
        migrations.RemoveField(
            model_name='emergencyprojectactivity',
            name='disabled_female_50_59_count',
        ),
        migrations.RemoveField(
            model_name='emergencyprojectactivity',
            name='disabled_female_60_69_count',
        ),
        migrations.RemoveField(
            model_name='emergencyprojectactivity',
            name='disabled_female_70_plus_count',
        ),
        migrations.RemoveField(
            model_name='emergencyprojectactivity',
            name='disabled_male_0_5_count',
        ),
        migrations.RemoveField(
            model_name='emergencyprojectactivity',
            name='disabled_male_30_39_count',
        ),
        migrations.RemoveField(
            model_name='emergencyprojectactivity',
            name='disabled_male_40_49_count',
        ),
        migrations.RemoveField(
            model_name='emergencyprojectactivity',
            name='disabled_male_50_59_count',
        ),
        migrations.RemoveField(
            model_name='emergencyprojectactivity',
            name='disabled_male_60_69_count',
        ),
        migrations.RemoveField(
            model_name='emergencyprojectactivity',
            name='disabled_male_70_plus_count',
        ),
        migrations.RemoveField(
            model_name='emergencyprojectactivity',
            name='disabled_other_0_5_count',
        ),
        migrations.RemoveField(
            model_name='emergencyprojectactivity',
            name='disabled_other_30_39_count',
        ),
        migrations.RemoveField(
            model_name='emergencyprojectactivity',
            name='disabled_other_40_49_count',
        ),
        migrations.RemoveField(
            model_name='emergencyprojectactivity',
            name='disabled_other_50_59_count',
        ),
        migrations.RemoveField(
            model_name='emergencyprojectactivity',
            name='disabled_other_60_69_count',
        ),
        migrations.RemoveField(
            model_name='emergencyprojectactivity',
            name='disabled_other_70_plus_count',
        ),
        migrations.RemoveField(
            model_name='emergencyprojectactivity',
            name='female_0_5_count',
        ),
        migrations.RemoveField(
            model_name='emergencyprojectactivity',
            name='female_30_39_count',
        ),
        migrations.RemoveField(
            model_name='emergencyprojectactivity',
            name='female_40_49_count',
        ),
        migrations.RemoveField(
            model_name='emergencyprojectactivity',
            name='female_50_59_count',
        ),
        migrations.RemoveField(
            model_name='emergencyprojectactivity',
            name='female_60_69_count',
        ),
        migrations.RemoveField(
            model_name='emergencyprojectactivity',
            name='female_70_plus_count',
        ),
        migrations.RemoveField(
            model_name='emergencyprojectactivity',
            name='male_0_5_count',
        ),
        migrations.RemoveField(
            model_name='emergencyprojectactivity',
            name='male_30_39_count',
        ),
        migrations.RemoveField(
            model_name='emergencyprojectactivity',
            name='male_40_49_count',
        ),
        migrations.RemoveField(
            model_name='emergencyprojectactivity',
            name='male_50_59_count',
        ),
        migrations.RemoveField(
            model_name='emergencyprojectactivity',
            name='male_60_69_count',
        ),
        migrations.RemoveField(
            model_name='emergencyprojectactivity',
            name='male_70_plus_count',
        ),
        migrations.RemoveField(
            model_name='emergencyprojectactivity',
            name='other_0_5_count',
        ),
        migrations.RemoveField(
            model_name='emergencyprojectactivity',
            name='other_30_39_count',
        ),
        migrations.RemoveField(
            model_name='emergencyprojectactivity',
            name='other_40_49_count',
        ),
        migrations.RemoveField(
            model_name='emergencyprojectactivity',
            name='other_50_59_count',
        ),
        migrations.RemoveField(
            model_name='emergencyprojectactivity',
            name='other_60_69_count',
        ),
        migrations.RemoveField(
            model_name='emergencyprojectactivity',
            name='other_70_plus_count',
        ),
        migrations.AddField(
            model_name='emergencyprojectactivity',
            name='disabled_femal_0_1',
            field=models.IntegerField(blank=True, null=True, verbose_name='Disabled Girls 0-1'),
        ),
        migrations.AddField(
            model_name='emergencyprojectactivity',
            name='disabled_female_2_5_count',
            field=models.IntegerField(blank=True, null=True, verbose_name='Disabled Girls 2-5'),
        ),
        migrations.AddField(
            model_name='emergencyprojectactivity',
            name='disabled_female_60_plus_count',
            field=models.IntegerField(blank=True, null=True, verbose_name='Disabled Older Women 60+'),
        ),
        migrations.AddField(
            model_name='emergencyprojectactivity',
            name='disabled_male_0_1',
            field=models.IntegerField(blank=True, null=True, verbose_name='Disabled Boys 0-1'),
        ),
        migrations.AddField(
            model_name='emergencyprojectactivity',
            name='disabled_male_2_5_count',
            field=models.IntegerField(blank=True, null=True, verbose_name='Disabled Boys 2-5'),
        ),
        migrations.AddField(
            model_name='emergencyprojectactivity',
            name='disabled_male_60_plus_count',
            field=models.IntegerField(blank=True, null=True, verbose_name='Disabled Older Men 60+'),
        ),
        migrations.AddField(
            model_name='emergencyprojectactivity',
            name='disabled_other_0_1',
            field=models.IntegerField(blank=True, null=True, verbose_name='Disabled Others/Unknown 0-1'),
        ),
        migrations.AddField(
            model_name='emergencyprojectactivity',
            name='disabled_other_2_5_count',
            field=models.IntegerField(blank=True, null=True, verbose_name='Disabled Others/Unknown 2-5'),
        ),
        migrations.AddField(
            model_name='emergencyprojectactivity',
            name='disabled_other_60_plus_count',
            field=models.IntegerField(blank=True, null=True, verbose_name='Disabled Others/Unknown 60+'),
        ),
        migrations.AddField(
            model_name='emergencyprojectactivity',
            name='female_0_1',
            field=models.IntegerField(blank=True, null=True, verbose_name='Girls 0-1'),
        ),
        migrations.AddField(
            model_name='emergencyprojectactivity',
            name='female_2_5_count',
            field=models.IntegerField(blank=True, null=True, verbose_name='Girls 2-5'),
        ),
        migrations.AddField(
            model_name='emergencyprojectactivity',
            name='female_60_plus_count',
            field=models.IntegerField(blank=True, null=True, verbose_name='Older Women 60+'),
        ),
        migrations.AddField(
            model_name='emergencyprojectactivity',
            name='male_0_1',
            field=models.IntegerField(blank=True, null=True, verbose_name='Boys 0-1'),
        ),
        migrations.AddField(
            model_name='emergencyprojectactivity',
            name='male_2_5_count',
            field=models.IntegerField(blank=True, null=True, verbose_name='Boys 2-5'),
        ),
        migrations.AddField(
            model_name='emergencyprojectactivity',
            name='male_60_plus_count',
            field=models.IntegerField(blank=True, null=True, verbose_name='Older Men 60+'),
        ),
        migrations.AddField(
            model_name='emergencyprojectactivity',
            name='other_0_1',
            field=models.IntegerField(blank=True, null=True, verbose_name='Others/Unknown 0-1'),
        ),
        migrations.AddField(
            model_name='emergencyprojectactivity',
            name='other_2_5_count',
            field=models.IntegerField(blank=True, null=True, verbose_name='Others/Unknown 2-5'),
        ),
        migrations.AddField(
            model_name='emergencyprojectactivity',
            name='other_60_plus_count',
            field=models.IntegerField(blank=True, null=True, verbose_name='Others/Unknown 60+'),
        ),
    ]