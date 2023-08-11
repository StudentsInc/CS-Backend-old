from rest_framework import serializers
from educator_app.models import *


class EducatorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Educator
        exclude = ('id', 'created_by', 'updated_by', 'status')


class HighSchoolTabItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HighSchoolTabItems
        exclude = ('created_by', 'updated_by', 'status')


class CollegeLifeItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollegeLifeItems
        exclude = ('created_by', 'updated_by', 'status')


class HighSchoolSerializer(serializers.ModelSerializer):
    high_school_tab_items = HighSchoolTabItemsSerializer(many=True)
    college_life_items = CollegeLifeItemsSerializer(many=True)

    class Meta:
        model = HighSchool
        exclude = ('id', 'created_by', 'updated_by', 'status')


class PostSecondaryTabImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostSecondaryTabImages
        fields = '__all__'


class PostSecondaryTabItemsSerializer(serializers.ModelSerializer):
    image = PostSecondaryTabImagesSerializer(many=True)

    class Meta:
        model = PostSecondaryTabItems
        exclude = ('id', 'created_by', 'updated_by', 'status')


class PostSecondarySerializer(serializers.ModelSerializer):
    secondary_tab_items = PostSecondaryTabItemsSerializer(many=True)

    class Meta:
        model = PostSecondary
        exclude = ('id', 'created_by', 'updated_by', 'status')
        depth = 1
