# Generated by Django 3.2.8 on 2022-04-22 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('career', '0008_auto_20220421_0617'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schoolprofile',
            name='location',
        ),
        migrations.AddField(
            model_name='schoolprofile',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='career.country'),
        ),
    ]
