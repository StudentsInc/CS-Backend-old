# Generated by Django 3.2.8 on 2021-12-16 07:11

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
            name='Conscientious',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(blank=True, choices=[('male', 'male'), ('female', 'female'), ('other', 'other')], max_length=100, null=True)),
                ('age', models.CharField(blank=True, choices=[(12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27), (28, 28), (29, 29), (30, 30), (31, 31), (32, 32), (33, 33), (34, 34), (35, 35), (36, 36), (37, 37), (38, 38), (39, 39), (40, 40), (41, 41), (42, 42), (43, 43), (44, 44), (45, 45), (46, 46), (47, 47), (48, 48), (49, 49), (50, 50), (51, 51), (52, 52), (53, 53), (54, 54), (55, 55), (56, 56), (57, 57), (58, 58), (59, 59)], max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EducationLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('education', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PersonalityDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(default='The Big Five Assessment', max_length=300)),
                ('short_description', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.FileField(blank=True, null=True, upload_to='')),
                ('assesment_button', models.CharField(default='The Big Five Assessment', max_length=300)),
                ('duration', models.IntegerField(blank=True, null=True)),
                ('total_question', models.IntegerField(help_text='Total No of Question', verbose_name='Total No of Question')),
            ],
        ),
        migrations.CreateModel(
            name='PersonalityQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_type', models.CharField(blank=True, choices=[('extravert', 'extravert'), ('adventurous', 'adventurous'), ('agreeable', 'agreeable'), ('neurotic', 'neurotic'), ('conscientious', 'conscientious')], max_length=100, null=True)),
                ('question', models.TextField(blank=True, null=True)),
                ('personality_detail', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='personality_test.personalitydetail')),
            ],
        ),
        migrations.CreateModel(
            name='Reason',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PersonalityTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive'), ('blocked', 'Blocked')], default='active', help_text='Status', max_length=10)),
                ('start_time', models.DateTimeField(blank=True, null=True)),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('time_left', models.CharField(blank=True, max_length=100, null=True)),
                ('exam_status', models.CharField(choices=[('InProgress', 'InProgress'), ('Complete', 'Complete')], default='InProgress', max_length=30)),
                ('conscientious', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='personality_test.conscientious')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='personality_test_personalitytest_created', to=settings.AUTH_USER_MODEL)),
                ('personality_test', models.ManyToManyField(blank=True, to='personality_test.PersonalityQuestion')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='personality_test_personalitytest_updated', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PersonalityAnswerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive'), ('blocked', 'Blocked')], default='active', help_text='Status', max_length=10)),
                ('answer_type', models.CharField(blank=True, choices=[('strongly_agree', 'strongly_agree'), ('agree', 'agree'), ('neutral', 'neutral'), ('disagree', 'disagree'), ('strongly_disagree', 'strongly_disagree')], max_length=100, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='personality_test_personalityanswermodel_created', to=settings.AUTH_USER_MODEL)),
                ('personality_question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personality_test.personalityquestion')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='personality_test_personalityanswermodel_updated', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='conscientious',
            name='educational_level',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='personality_test.educationlevel'),
        ),
        migrations.AddField(
            model_name='conscientious',
            name='reason',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='personality_test.reason'),
        ),
    ]
