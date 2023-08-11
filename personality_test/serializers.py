from django_countries import countries
from rest_framework import serializers

# local import
from personality_test.models import *


class ReasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reason
        fields = '__all__'


class EducationLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationLevel
        fields = '__all__'


class PersonalityDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalityDetail
        fields = '__all__'


class PersonalityQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalityQuestion
        fields = ('id', 'question_type', 'personality_detail', 'question', 'key_type')


class PersonalityQuestionListSerializer(serializers.Serializer):
    personality_id = serializers.IntegerField(required=True)
    question_type = serializers.CharField(required=True)

    class Meta:
        model = PersonalityQuestion
        fields = ('id', 'question_type', 'personality_id')


class PersonalityAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalityAnswerModel
        fields = '__all__'


class PersonalityTestPostSerializer(serializers.Serializer):
    personality_id = serializers.IntegerField(required=True)
    question_id = serializers.IntegerField(required=True)
    answer = serializers.CharField(max_length=200, required=True)
    score = serializers.IntegerField(required=True)
    guest_token = serializers.CharField(max_length=255, required=False)


class PersonalityTestTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalityTest
        fields = ('id', 'start_time', 'end_time', 'time_left', 'created_by')


class TestTimeSerializer(serializers.Serializer):
    personality_detail = serializers.IntegerField(required=True)


class EndTimeSerializer(serializers.Serializer):
    personality_test_id = serializers.IntegerField(required=True)
    user_detail_id = serializers.IntegerField(required=True)
    guest_token = serializers.CharField(max_length=255, required=False)


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetail
        fields = '__all__'


class GetReportSerializer(serializers.Serializer):
    personality_test_id = serializers.IntegerField(required=True)


class UserAssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAssesmentStats
        fields = '__all__'


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobMaster
        fields = '__all__'


class GuestTokenInputSerializer(serializers.Serializer):
    guest_token = serializers.CharField(max_length=255, required=False)


class PersonalityDashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalityDashboard
        fields = '__all__'


class PersonalityReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalityReportMaster
        fields = '__all__'
