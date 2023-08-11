from rest_framework import serializers
from learning_style.models import *


class LearningQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = LearningQuestion
        fields = '__all__'


class LearningAnswerModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = LearningAnswerModel
        fields = '__all__'


class LearningUserInterestTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = LearningUserInterestTest
        fields = '__all__'
