from rest_framework import serializers
from .models import *


class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = SurveyQuestion
        fields = '__all__'


class UserSurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSurvey
        fields = '__all__'


class UserSurveyListSerializer(serializers.ModelSerializer):
    question = SurveySerializer()

    class Meta:
        model = UserSurvey
        fields = '__all__'
