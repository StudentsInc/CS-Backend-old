from django.contrib import admin
from learning_style.models import *


# Register your models here.
@admin.register(LearningQuestion)
class LearningQuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'heading', 'question_no', 'question')


@admin.register(LearningAnswerModel)
class LearningAnswerModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'question_detail', 'answer')


@admin.register(LearningUserInterestTest)
class LearningUserInterestTestTest(admin.ModelAdmin):
    list_display = ('id', 'start_time', 'end_time', 'exam_status', 'created_by')
