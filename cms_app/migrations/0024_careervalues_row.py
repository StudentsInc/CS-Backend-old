# Generated by Django 3.2.8 on 2022-04-04 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms_app', '0023_careervalues'),
    ]

    operations = [
        migrations.AddField(
            model_name='careervalues',
            name='row',
            field=models.CharField(blank=True, default='first', max_length=100, null=True),
        ),
    ]
