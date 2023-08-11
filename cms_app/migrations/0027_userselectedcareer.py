# Generated by Django 3.2.8 on 2022-04-07 10:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cms_app', '0026_userselectedmajor'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSelectedCareer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive'), ('blocked', 'Blocked')], default='active', help_text='Status', max_length=10)),
                ('values', models.CharField(blank=True, max_length=100, null=True)),
                ('career', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms_app.selectcareer')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cms_app_userselectedcareer_created', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cms_app_userselectedcareer_updated', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]