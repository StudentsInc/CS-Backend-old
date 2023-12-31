# Generated by Django 3.2.8 on 2021-12-09 10:13

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
            name='AnswerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive'), ('blocked', 'Blocked')], default='active', help_text='Status', max_length=10)),
                ('answer', models.CharField(help_text='like(1) to dislike(5)', max_length=10)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='learning_style_answermodel_created', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LearningQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(blank=True, max_length=300, null=True)),
                ('question_no', models.IntegerField(verbose_name='Question No')),
                ('image', models.FileField(blank=True, null=True, upload_to='')),
                ('question', models.TextField(default='')),
                ('option_1', models.CharField(blank=True, max_length=150, null=True)),
                ('option_2', models.CharField(blank=True, max_length=150, null=True)),
                ('option_3', models.CharField(blank=True, max_length=150, null=True)),
                ('option_4', models.CharField(blank=True, max_length=150, null=True)),
                ('option_5', models.CharField(blank=True, max_length=150, null=True)),
            ],
            options={
                'ordering': ['question_no'],
            },
        ),
        migrations.CreateModel(
            name='UserInterestTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive'), ('blocked', 'Blocked')], default='active', help_text='Status', max_length=10)),
                ('start_time', models.DateTimeField(blank=True, null=True)),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('exam_status', models.CharField(choices=[('InProgress', 'InProgress'), ('Complete', 'Complete')], default='InProgress', max_length=30)),
                ('answer', models.ManyToManyField(blank=True, to='learning_style.AnswerModel')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='learning_style_userinteresttest_created', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='learning_style_userinteresttest_updated', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='answermodel',
            name='question_detail',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learning_style.learningquestion'),
        ),
        migrations.AddField(
            model_name='answermodel',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='learning_style_answermodel_updated', to=settings.AUTH_USER_MODEL),
        ),
    ]
