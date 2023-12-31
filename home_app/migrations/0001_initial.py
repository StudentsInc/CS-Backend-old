# Generated by Django 3.2.8 on 2021-11-01 10:30

import ckeditor.fields
import ckeditor_uploader.fields
import colorfield.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive'), ('blocked', 'Blocked')], default='active', help_text='Status', max_length=10)),
                ('heading', models.CharField(max_length=200)),
                ('company_name', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=150)),
                ('designation', models.CharField(max_length=55)),
                ('image', models.ImageField(upload_to='career-studio/home/testimonials/')),
                ('content', ckeditor.fields.RichTextField()),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='home_app_testimonials_created', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='home_app_testimonials_updated', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Testimonial',
                'verbose_name_plural': 'Testimonials',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='OurSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive'), ('blocked', 'Blocked')], default='active', help_text='Status', max_length=10)),
                ('skill_name', models.CharField(max_length=100)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='home_app_ourskill_created', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='home_app_ourskill_updated', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Skill',
                'verbose_name_plural': 'Our Skills',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive'), ('blocked', 'Blocked')], default='active', help_text='Status', max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='home_app_newsletter_created', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='home_app_newsletter_updated', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HowItWorks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive'), ('blocked', 'Blocked')], default='active', help_text='Status', max_length=10)),
                ('heading', models.CharField(max_length=100)),
                ('content', ckeditor.fields.RichTextField()),
                ('step', models.IntegerField()),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='home_app_howitworks_created', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='home_app_howitworks_updated', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'How It Work',
                'verbose_name_plural': 'How It Works',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive'), ('blocked', 'Blocked')], default='active', help_text='Status', max_length=10)),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=255)),
                ('message', models.TextField()),
                ('department', models.CharField(choices=[('DEPT1', 'DEPT1'), ('DEPT2', 'DEPT2')], default='DEPT1', max_length=50)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='home_app_contactus_created', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='home_app_contactus_updated', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Contact us',
                'verbose_name_plural': 'Contact Us',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive'), ('blocked', 'Blocked')], default='active', help_text='Status', max_length=10)),
                ('name', models.CharField(max_length=100)),
                ('logo', models.ImageField(upload_to='career-studio/home/brand/')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='home_app_brand_created', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='home_app_brand_updated', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Brand',
                'verbose_name_plural': 'Brand',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive'), ('blocked', 'Blocked')], default='active', help_text='Status', max_length=10)),
                ('banner_image', models.ImageField(blank=True, null=True, upload_to='career-studio/home/banner/')),
                ('redirect_url', models.CharField(blank=True, max_length=255, null=True)),
                ('heading', models.TextField(blank=True, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('heading_color', colorfield.fields.ColorField(default='#FFFFFF', max_length=18)),
                ('content_color', colorfield.fields.ColorField(default='#FFFFFF', max_length=18)),
                ('text_style', models.CharField(choices=[('LEFT', 'LEFT'), ('RIGHT', 'RIGHT'), ('CENTER', 'CENTER')], default='"LEFT', max_length=20)),
                ('button_text', models.CharField(max_length=100)),
                ('button_background', colorfield.fields.ColorField(default='#FFFFFF', max_length=18)),
                ('button_text_color', colorfield.fields.ColorField(default='#FFFFFF', max_length=18)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='home_app_banner_created', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='home_app_banner_updated', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Banner',
                'verbose_name_plural': 'Banners',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive'), ('blocked', 'Blocked')], default='active', help_text='Status', max_length=10)),
                ('image', models.ImageField(blank=True, null=True, upload_to='career-studio/home/about/')),
                ('heading', models.CharField(max_length=200)),
                ('content', ckeditor.fields.RichTextField()),
                ('button_text', models.CharField(max_length=100)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='home_app_about_created', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='home_app_about_updated', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'About',
                'verbose_name_plural': 'About',
                'ordering': ['-id'],
            },
        ),
    ]
