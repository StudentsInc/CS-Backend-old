# Generated by Django 3.2.8 on 2022-03-04 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms_app', '0018_workvalueitems_workvaluesscores'),
    ]

    operations = [
        migrations.AddField(
            model_name='workvalueitems',
            name='category_type',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
