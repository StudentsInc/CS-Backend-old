# Generated by Django 3.2.8 on 2022-07-28 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_app', '0003_guestuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='otp',
            name='language_code',
            field=models.CharField(choices=[('English', 'en'), ('Arabic', 'ar')], default='English', max_length=35),
        ),
        migrations.AddField(
            model_name='profile',
            name='language_code',
            field=models.CharField(choices=[('English', 'en'), ('Arabic', 'ar')], default='English', max_length=35),
        ),
    ]
