from django.contrib import admin
from personality_test.models import *
from import_export.admin import ImportExportModelAdmin


# Register your models here.

class JobMasterAdmin(ImportExportModelAdmin):
    list_display = ('id', 'title', 'category', 'job_category')
    search_fields = ('title', 'category')


admin.site.register(JobMaster, JobMasterAdmin)


@admin.register(EducationLevel)
class EducationLevelAdmin(admin.ModelAdmin):
    list_display = ('id', 'education')


@admin.register(Reason)
class ReasonAdmin(admin.ModelAdmin):
    list_display = ('id', 'reason')


@admin.register(UserDetail)
class UserDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'gender', 'age', 'country', 'educational_level', 'reason')


@admin.register(PersonalityDetail)
class PersonalityDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'heading', 'duration', 'total_question')


@admin.register(PersonalityQuestion)
class PersonalityQuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'personality_detail', 'question_type', 'question')


@admin.register(PersonalityTest)
class PersonalityQuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'start_time', 'end_time', 'time_left')


@admin.register(PersonalityAnswerModel)
class PersonalityQuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'personality_question', 'answer_type')


@admin.register(AssessmentStats)
class AssessmentStatsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_count', 'total_score', 'age_group', 'assesment_category')


@admin.register(UserAssesmentStats)
class UserAssesmentStatsAdmin(admin.ModelAdmin):
    list_display = ('id', 'assesment', 'created_by', 'created_on')


@admin.register(PersonalityDashboard)
class PersonalityDashboardAdmin(admin.ModelAdmin):
    list_display = ('created_by', 'extravert_scale', 'adventurous_scale', 'agreeable_scale')


@admin.register(PersonalityReportMaster)
class PersonalityReportMasterAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'score')
