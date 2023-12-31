# Generated by Django 3.2.8 on 2022-02-15 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms_app', '0013_careervotes'),
    ]

    operations = [
        migrations.AddField(
            model_name='selectcareer',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='career_image'),
        ),
        migrations.AlterField(
            model_name='selectcareer',
            name='votes',
            field=models.PositiveIntegerField(blank=True, default=0, max_length=256, null=True),
        ),
    ]
