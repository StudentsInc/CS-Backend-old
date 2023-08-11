# Generated by Django 3.2.8 on 2021-12-06 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('educator_app', '0007_auto_20211206_0711'),
    ]

    operations = [
        migrations.RenameField(
            model_name='collegelifeitems',
            old_name='updated_at',
            new_name='created_on',
        ),
        migrations.RenameField(
            model_name='educator',
            old_name='updated_at',
            new_name='created_on',
        ),
        migrations.RenameField(
            model_name='highschool',
            old_name='updated_at',
            new_name='created_on',
        ),
        migrations.RenameField(
            model_name='highschooltabitems',
            old_name='updated_at',
            new_name='created_on',
        ),
        migrations.RenameField(
            model_name='postsecondary',
            old_name='updated_at',
            new_name='created_on',
        ),
        migrations.RenameField(
            model_name='postsecondarytabitems',
            old_name='updated_at',
            new_name='created_on',
        ),
        migrations.RemoveField(
            model_name='collegelifeitems',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='educator',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='highschool',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='highschooltabitems',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='postsecondary',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='postsecondarytabitems',
            name='created_at',
        ),
        migrations.AddField(
            model_name='collegelifeitems',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='educator',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='highschool',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='highschooltabitems',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='postsecondary',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='postsecondarytabitems',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]