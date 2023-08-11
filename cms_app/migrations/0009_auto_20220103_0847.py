# Generated by Django 3.2.8 on 2022-01-03 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms_app', '0008_auto_20211227_0840'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='careerlibrary',
            name='job_category',
        ),
        migrations.AlterField(
            model_name='careerlibrary',
            name='career_options',
            field=models.CharField(blank=True, choices=[('artistic', 'artistic'), ('social', 'social'), ('enterprising', 'enterprising'), ('investigative', 'investigative'), ('conventional', 'conventional'), ('realistic', 'realistic')], max_length=100, null=True),
        ),
    ]