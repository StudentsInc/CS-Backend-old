# Generated by Django 3.2.8 on 2021-11-23 08:05

import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0003_alter_brand_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='background_image',
            field=models.ImageField(blank=True, null=True, upload_to='career-studio/home/about/'),
        ),
        migrations.AddField(
            model_name='about',
            name='button_background',
            field=colorfield.fields.ColorField(default='#FFFFFF', max_length=18),
        ),
        migrations.AddField(
            model_name='about',
            name='button_color',
            field=colorfield.fields.ColorField(default='#FFFFFF', max_length=18),
        ),
        migrations.AddField(
            model_name='about',
            name='button_url',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='banner',
            name='banner_background_image',
            field=models.ImageField(blank=True, null=True, upload_to='career-studio/home/banner/'),
        ),
        migrations.AddField(
            model_name='banner',
            name='button_background2',
            field=colorfield.fields.ColorField(default='#FFFFFF', max_length=18),
        ),
        migrations.AddField(
            model_name='banner',
            name='button_text2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='banner',
            name='button_text_color2',
            field=colorfield.fields.ColorField(default='#FFFFFF', max_length=18),
        ),
        migrations.AddField(
            model_name='banner',
            name='button_url1',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='banner',
            name='button_url2',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='about',
            name='button_text',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
