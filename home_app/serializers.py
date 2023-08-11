from rest_framework import serializers
from .models import *


class OurSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurSkill
        fields = '__all__'


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        exclude = ('id', 'created_by', 'updated_by', 'status')


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        exclude = ('id', 'created_by', 'updated_by', 'status')


class HowItWorksSerializer(serializers.ModelSerializer):
    class Meta:
        model = HowItWorks
        exclude = ('id', 'created_by', 'updated_by', 'status')


class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonials
        exclude = ('id', 'created_by', 'updated_by', 'status')


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        exclude = ('id', 'created_by', 'updated_by', 'status')


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        exclude = ('id', 'created_by', 'updated_by', 'status')


class NewsletterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newsletter
        exclude = ('id', 'created_by', 'updated_by', 'status')


class NewsletterTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsletterText
        exclude = ('id', 'created_by', 'updated_by', 'status')
