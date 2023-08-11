from django.contrib import admin
from univercity_app.models import *


# Register your models here.
@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['id', 'country_name']


@admin.register(MajorSetup)
class MajorSetupAdmin(admin.ModelAdmin):
    list_display = ['id', 'major_name']


@admin.register(SchoolProfile)
class SchoolProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'school_name', 'location']


@admin.register(SchoolMajor)
class SchoolMajorAdmin(admin.ModelAdmin):
    list_display = ['id', 'school', 'major']


@admin.register(SelectedSchool)
class SelectedSchoolAdmin(admin.ModelAdmin):
    list_display = ['id']
