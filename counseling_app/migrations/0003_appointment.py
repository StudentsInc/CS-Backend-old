# Generated by Django 3.2.8 on 2022-06-28 11:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('counseling_app', '0002_auto_20211206_1354'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive'), ('blocked', 'Blocked')], default='active', help_text='Status', max_length=10)),
                ('appointment_date', models.DateField(blank=True, null=True)),
                ('appointment_time', models.TimeField(blank=True, null=True)),
                ('session_cost', models.CharField(default='200', max_length=150)),
                ('payment_method', models.CharField(choices=[('stripe', 'stripe'), ('paypal', 'paypal')], default='stripe', max_length=150)),
                ('charge_id', models.CharField(blank=True, max_length=400, null=True)),
                ('coach', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='counseling_app.coach')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='counseling_app_appointment_created', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='counseling_app_appointment_updated', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
