from django.contrib import admin
from .models import *


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'status', 'created_by']
    search_fields = ['title', 'slug', 'id']

