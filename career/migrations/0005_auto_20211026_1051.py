# Generated by Django 3.2.8 on 2021-10-26 10:51

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('career', '0004_careercommonindustries_careercommonindustriesbreakup_careereducationrequirement'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assessment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive'), ('blocked', 'Blocked')], default='active', help_text='Status', max_length=10)),
                ('question', models.TextField()),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='career_assessment_created', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Assessment',
                'verbose_name_plural': 'Assessments',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='AssessmentCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive'), ('blocked', 'Blocked')], default='active', help_text='Status', max_length=10)),
                ('category_name', models.CharField(max_length=100)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='career_assessmentcategory_created', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='career_assessmentcategory_updated', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Assessment Category',
                'verbose_name_plural': 'Assessment Categories',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='UserAssessment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive'), ('blocked', 'Blocked')], default='active', help_text='Status', max_length=10)),
                ('answer_type', models.CharField(choices=[('Strongly Agree', 'Strongly Agree'), ('Agree', 'Agree'), ('Neutral', 'Neutral'), ('Disagree', 'Disagree'), ('Strongly Disagree', 'Strongly Disagree')], default='Agree', max_length=100)),
                ('answer', ckeditor.fields.RichTextField()),
                ('assessment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='career.assessment')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='career_userassessment_created', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='career_userassessment_updated', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Assessment',
                'verbose_name_plural': 'User Assessments',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive'), ('blocked', 'Blocked')], default='active', help_text='Status', max_length=10)),
                ('type_name', models.CharField(max_length=100)),
                ('assessment_Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='career.assessmentcategory')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='career_type_created', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='career_type_updated', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='SchoolProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive'), ('blocked', 'Blocked')], default='active', help_text='Status', max_length=10)),
                ('school_name', models.CharField(max_length=255)),
                ('banner_image', models.ImageField(blank=True, null=True, upload_to='school-profile/banner-images/')),
                ('school_logo', models.ImageField(blank=True, null=True, upload_to='school-profile/school-logo/')),
                ('description', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('contact_no', models.CharField(max_length=17)),
                ('website', models.CharField(max_length=255)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='career_schoolprofile_created', to=settings.AUTH_USER_MODEL)),
                ('location', models.ManyToManyField(to='career.Country')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='career_schoolprofile_updated', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'School Profile',
                'verbose_name_plural': 'School Profiles',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='SchoolGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive'), ('blocked', 'Blocked')], default='active', help_text='Status', max_length=10)),
                ('images', models.URLField()),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='career_schoolgallery_created', to=settings.AUTH_USER_MODEL)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='career.schoolprofile')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='career_schoolgallery_updated', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'School Gallery',
                'verbose_name_plural': 'School Galleries',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='MajorSetup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive'), ('blocked', 'Blocked')], default='active', help_text='Status', max_length=10)),
                ('major_name', models.CharField(max_length=255)),
                ('major_description', models.TextField()),
                ('major_type', models.CharField(choices=[('Bachelor', 'Bachelor'), ('Masters', 'Masters')], default='Bachelor', max_length=50)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='career_majorsetup_created', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='career_majorsetup_updated', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.AddField(
            model_name='assessment',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='career.type'),
        ),
        migrations.AddField(
            model_name='assessment',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='career_assessment_updated', to=settings.AUTH_USER_MODEL),
        ),
    ]
