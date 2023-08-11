from django.contrib import admin
from educator_app.models import *


@admin.register(Educator)
class EducatorAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_by']


@admin.register(HighSchoolTabItems)
class HighSchoolTabItemsAdmin(admin.ModelAdmin):
    list_display = ['id', 'heading', 'created_by']


@admin.register(CollegeLifeItems)
class CollegeLifeItemsAdmin(admin.ModelAdmin):
    list_display = ['id', 'heading', 'created_by']


@admin.register(HighSchool)
class HighSchoolAdmin(admin.ModelAdmin):
    list_display = ['id', 'heading', 'created_by']


@admin.register(PostSecondaryTabImages)
class PostSecondaryTabImagesAdmin(admin.ModelAdmin):
    list_display = ['id', 'file', 'align']


@admin.register(PostSecondaryTabItems)
class PostSecondaryTabItemsAdmin(admin.ModelAdmin):
    list_display = ['id', 'heading', 'subheading', 'align']


@admin.register(PostSecondary)
class PostSecondaryAdmin(admin.ModelAdmin):
    list_display = ['id', 'heading', 'created_by']
