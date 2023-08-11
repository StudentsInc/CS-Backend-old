# Generated by Django 3.2.8 on 2022-01-20 11:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account_app', '0003_guestuser'),
        ('personality_test', '0011_personalityreportmaster'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalityanswermodel',
            name='guest_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account_app.guestuser'),
        ),
        migrations.AddField(
            model_name='personalitydashboard',
            name='guest_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account_app.guestuser'),
        ),
        migrations.AddField(
            model_name='personalitytest',
            name='guest_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account_app.guestuser'),
        ),
        migrations.AddField(
            model_name='userassesmentstats',
            name='guest_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account_app.guestuser'),
        ),
    ]
