from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['id', 'skill_name', 'skill_type', 'status', 'created_by']


@admin.register(AlternativeTitles)
class AlternativeTitleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'status', 'created_by']


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['id', 'country_name', 'country_code']


@admin.register(CareerProfile)
class CareerProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'profile_type', 'name', 'created_by']


@admin.register(CareerProfileGlance)
class CareerProfileGlanceAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_by']


@admin.register(AverageSalary)
class AverageSalaryAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_by']


@admin.register(CareerEducationRequirement)
class CareerEducationRequirementAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_by']


@admin.register(CareerCommonIndustries)
class CareerCommonIndustriesAdmin(admin.ModelAdmin):
    list_display = ['id', 'private', 'government', 'created_by']


@admin.register(CareerCommonIndustriesBreakup)
class CareerCommonIndustriesBreakupAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'type', 'percentage', 'created_by']


@admin.register(AssessmentCategory)
class AssessmentCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'category_name', 'created_by']


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'type_name', 'created_by']


@admin.register(Assessment)
class AssessmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_by']


@admin.register(UserAssessment)
class UserAssessmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_by']


@admin.register(MajorSetup)
class MajorSetupAdmin(admin.ModelAdmin):
    list_display = ['id', 'major_name', 'major_type']


@admin.register(SchoolProfile)
class SchoolProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'school_name', 'created_by']


@admin.register(SchoolGallery)
class SchoolGalleryAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_by']


@admin.register(SchoolMajor)
class SchoolMajorAdmin(admin.ModelAdmin):
    list_display = ['id', 'school', 'major']


@admin.register(SchoolMajorSubject)
class SchoolMajorSubjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject_name', 'created_by']


