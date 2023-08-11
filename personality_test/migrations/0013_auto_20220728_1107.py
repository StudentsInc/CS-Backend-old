# Generated by Django 3.2.8 on 2022-07-28 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personality_test', '0012_auto_20220120_1107'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalityanswermodel',
            name='language_code',
            field=models.CharField(choices=[('English', 'en'), ('Arabic', 'ar')], default='English', max_length=35),
        ),
        migrations.AddField(
            model_name='personalitydashboard',
            name='language_code',
            field=models.CharField(choices=[('English', 'en'), ('Arabic', 'ar')], default='English', max_length=35),
        ),
        migrations.AddField(
            model_name='personalitytest',
            name='language_code',
            field=models.CharField(choices=[('English', 'en'), ('Arabic', 'ar')], default='English', max_length=35),
        ),
        migrations.AddField(
            model_name='userassesmentstats',
            name='language_code',
            field=models.CharField(choices=[('English', 'en'), ('Arabic', 'ar')], default='English', max_length=35),
        ),
    ]