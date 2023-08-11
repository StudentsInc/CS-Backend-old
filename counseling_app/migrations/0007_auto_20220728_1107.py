# Generated by Django 3.2.8 on 2022-07-28 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counseling_app', '0006_rename_session_date_session_unavailable_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='language_code',
            field=models.CharField(choices=[('English', 'en'), ('Arabic', 'ar')], default='English', max_length=35),
        ),
        migrations.AddField(
            model_name='counselingheadline',
            name='language_code',
            field=models.CharField(choices=[('English', 'en'), ('Arabic', 'ar')], default='English', max_length=35),
        ),
    ]
