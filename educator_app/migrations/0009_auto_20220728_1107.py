# Generated by Django 3.2.8 on 2022-07-28 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('educator_app', '0008_auto_20211206_1354'),
    ]

    operations = [
        migrations.AddField(
            model_name='collegelifeitems',
            name='language_code',
            field=models.CharField(choices=[('English', 'en'), ('Arabic', 'ar')], default='English', max_length=35),
        ),
        migrations.AddField(
            model_name='educator',
            name='language_code',
            field=models.CharField(choices=[('English', 'en'), ('Arabic', 'ar')], default='English', max_length=35),
        ),
        migrations.AddField(
            model_name='highschool',
            name='language_code',
            field=models.CharField(choices=[('English', 'en'), ('Arabic', 'ar')], default='English', max_length=35),
        ),
        migrations.AddField(
            model_name='highschooltabitems',
            name='language_code',
            field=models.CharField(choices=[('English', 'en'), ('Arabic', 'ar')], default='English', max_length=35),
        ),
        migrations.AddField(
            model_name='postsecondary',
            name='language_code',
            field=models.CharField(choices=[('English', 'en'), ('Arabic', 'ar')], default='English', max_length=35),
        ),
        migrations.AddField(
            model_name='postsecondarytabitems',
            name='language_code',
            field=models.CharField(choices=[('English', 'en'), ('Arabic', 'ar')], default='English', max_length=35),
        ),
    ]
