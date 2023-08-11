from django.contrib import admin
from counseling_app.models import *


# Register your models here.
@admin.register(CounselingHeadline)
class CounselingHeadlineAdmin(admin.ModelAdmin):
    list_display = ('id', 'heading', 'content')


@admin.register(SessionTime)
class SessionTimeAdmin(admin.ModelAdmin):
    list_display = ('id', 'time')


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ('id', 'topics')


@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_by', 'coach', 'appointment_date', 'session_cost')
