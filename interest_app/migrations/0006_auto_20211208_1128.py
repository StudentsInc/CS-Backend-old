# Generated by Django 3.2.8 on 2021-12-08 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interest_app', '0005_alter_answermodel_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinteresttest',
            name='end_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userinteresttest',
            name='start_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]