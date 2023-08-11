from django.contrib import admin
from .models import *


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_by']


@admin.register(OurSkill)
class OurSkillAdmin(admin.ModelAdmin):
    list_display = ['id', 'skill_name', 'created_by']


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['id', 'heading', 'created_by']


@admin.register(HowItWorks)
class HowItWorksAdmin(admin.ModelAdmin):
    list_display = ['id', 'heading', 'created_by']


@admin.register(Testimonials)
class TestimonialsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'company_name', 'heading', 'designation']
    search_fields = ['name']


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_by']


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'department', 'created_by']


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'created_by']
    readonly_fields = ['email']


@admin.register(NewsletterText)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ['id', 'heading', 'content', 'status']
