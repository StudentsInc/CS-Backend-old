# Generated by Django 3.2.8 on 2022-07-20 08:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('counseling_app', '0005_auto_20220630_0651'),
    ]

    operations = [
        migrations.RenameField(
            model_name='session',
            old_name='session_date',
            new_name='unavailable_date',
        ),
    ]