# Generated by Django 3.2.8 on 2022-06-30 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counseling_app', '0004_auto_20220630_0643'),
    ]

    operations = [
        migrations.CreateModel(
            name='SessionTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='session',
            name='session_time',
        ),
        migrations.AddField(
            model_name='session',
            name='session_time',
            field=models.ManyToManyField(blank=True, to='counseling_app.SessionTime'),
        ),
    ]
