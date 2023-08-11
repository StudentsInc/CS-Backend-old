from rest_framework import serializers
from univercity_app.models import *


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class MajorSetupSerializer(serializers.ModelSerializer):
    class Meta:
        model = MajorSetup
        fields = '__all__'


class SchoolProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolProfile
        fields = '__all__'


class SchoolGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolGallery
        fields = '__all__'


class SchoolMajorSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolMajor
        fields = '__all__'


class SelectedSchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = SelectedSchool
        fields = '__all__'
