# Generated by Django 3.2.9 on 2021-11-27 08:30

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about_app', '0004_auto_20211127_0719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ourachievement',
            name='subheading',
            field=ckeditor.fields.RichTextField(blank=True, default='', null=True),
        ),
    ]
