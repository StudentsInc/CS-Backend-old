from django.contrib import admin
from about_app.models import *


@admin.register(OurAchievement)
class OurAchievementAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_by']


@admin.register(OurAchievementItems)
class OurAchievementItemsAdmin(admin.ModelAdmin):
    list_display = ['id', 'text', 'created_by']


@admin.register(OurTeam)
class OurAchievementAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_by']


@admin.register(OurTeamItems)
class OurAchievementItemsAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_by']
