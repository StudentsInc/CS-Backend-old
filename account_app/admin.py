from django.contrib import admin
from account_app.models import *


# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_by', 'phone']


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'messages']


@admin.register(GuestUser)
class GuestUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'token', 'user']


@admin.register(Otp)
class OtpAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_by', 'otp', 'type']
