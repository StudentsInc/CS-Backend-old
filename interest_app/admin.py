from django.contrib import admin
from interest_app.models import *


# Register your models here.
@admin.register(InterestDetail)
class InterestDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'heading', 'duration', 'total_question')


@admin.register(InterestQuestion)
class InterestQuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'interest_detail', 'question_no', 'question')


@admin.register(AnswerModel)
class AnswerModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'question_detail', 'answer')


@admin.register(UserInterestTest)
class UserInterestTestAdmin(admin.ModelAdmin):
    list_display = ('id', 'start_time', 'end_time', 'time_left', 'created_by')


@admin.register(UserScores)
class UserInterestTestAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_by')


@admin.register(InterestReportMaster)
class UserInterestTestAdmin(admin.ModelAdmin):
    list_display = ('id', 'report_category')


@admin.register(InterestAnswerData)
class InterestAnswerDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'exam_status', 'created_by')


@admin.register(FavoriteCareer)
class FavoriteCareerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_by')