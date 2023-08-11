# Generated by Django 3.2.8 on 2022-07-28 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20211206_1354'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='language_code',
            field=models.CharField(choices=[('English', 'en'), ('Arabic', 'ar')], default='English', max_length=35),
        ),
    ]
