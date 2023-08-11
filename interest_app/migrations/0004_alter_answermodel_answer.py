# Generated by Django 3.2.8 on 2021-12-07 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interest_app', '0003_alter_interestquestion_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answermodel',
            name='answer',
            field=models.CharField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], help_text='like(1) to dislike(5)', max_length=10),
        ),
    ]
