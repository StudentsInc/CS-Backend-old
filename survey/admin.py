from django.contrib import admin
from survey.models import *


# Register your models here.


@admin.register(SurveyQuestion)
class SurveyAdmin(admin.ModelAdmin):
    list_display = ('id', 'question')


@admin.register(UserSurvey)
class UserSurveyAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'created_by')
