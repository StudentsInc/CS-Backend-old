# Generated by Django 3.2.8 on 2021-12-06 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('career', '0006_schoolmajor_schoolmajorsubject'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alternativetitles',
            old_name='updated_at',
            new_name='created_on',
        ),
        migrations.RenameField(
            model_name='assessment',
            old_name='updated_at',
            new_name='created_on',
        ),
        migrations.RenameField(
            model_name='assessmentcategory',
            old_name='updated_at',
            new_name='created_on',
        ),
        migrations.RenameField(
            model_name='averagesalary',
            old_name='updated_at',
            new_name='created_on',
        ),
        migrations.RenameField(
            model_name='careercommonindustries',
            old_name='updated_at',
            new_name='created_on',
        ),
        migrations.RenameField(
            model_name='careercommonindustriesbreakup',
            old_name='updated_at',
            new_name='created_on',
        ),
        migrations.RenameField(
            model_name='careereducationrequirement',
            old_name='updated_at',
            new_name='created_on',
        ),
        migrations.RenameField(
            model_name='careerprofile',
            old_name='updated_at',
            new_name='created_on',
        ),
        migrations.RenameField(
            model_name='careerprofileglance',
            old_name='updated_at',
            new_name='created_on',
        ),
        migrations.RenameField(
            model_name='country',
            old_name='updated_at',
            new_name='created_on',
        ),
        migrations.RenameField(
            model_name='majorsetup',
            old_name='updated_at',
            new_name='created_on',
        ),
        migrations.RenameField(
            model_name='schoolgallery',
            old_name='updated_at',
            new_name='created_on',
        ),
        migrations.RenameField(
            model_name='schoolmajor',
            old_name='updated_at',
            new_name='created_on',
        ),
        migrations.RenameField(
            model_name='schoolmajorsubject',
            old_name='updated_at',
            new_name='created_on',
        ),
        migrations.RenameField(
            model_name='schoolprofile',
            old_name='updated_at',
            new_name='created_on',
        ),
        migrations.RenameField(
            model_name='skill',
            old_name='updated_at',
            new_name='created_on',
        ),
        migrations.RenameField(
            model_name='type',
            old_name='updated_at',
            new_name='created_on',
        ),
        migrations.RenameField(
            model_name='userassessment',
            old_name='updated_at',
            new_name='created_on',
        ),
        migrations.RemoveField(
            model_name='alternativetitles',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='assessment',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='assessmentcategory',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='averagesalary',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='careercommonindustries',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='careercommonindustriesbreakup',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='careereducationrequirement',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='careerprofile',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='careerprofileglance',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='country',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='majorsetup',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='schoolgallery',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='schoolmajor',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='schoolmajorsubject',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='schoolprofile',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='skill',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='type',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='userassessment',
            name='created_at',
        ),
        migrations.AddField(
            model_name='alternativetitles',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='assessment',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='assessmentcategory',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='averagesalary',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='careercommonindustries',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='careercommonindustriesbreakup',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='careereducationrequirement',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='careerprofile',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='careerprofileglance',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='country',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='majorsetup',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='schoolgallery',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='schoolmajor',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='schoolmajorsubject',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='schoolprofile',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='skill',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='type',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='userassessment',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
