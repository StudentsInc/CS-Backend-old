from rest_framework import serializers

# local import
from interest_app.models import *


class InterestDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterestDetail
        fields = '__all__'


class InterestAnswerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterestAnswerData
        fields = '__all__'


class TestTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInterestTest
        fields = ('id', 'start_time', 'end_time', 'time_left', 'created_by')


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerModel
        fields = '__all__'


class UserInterestTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInterestTest
        fields = '__all__'
        depth = 1


class UserInterestTestPostSerializer(serializers.Serializer):
    interest_id = serializers.IntegerField(required=True)
    question_id = serializers.IntegerField(required=True)
    answer = serializers.CharField(max_length=200, required=True)


class UserInterestTestDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInterestTest
        exclude = ('created_by', 'updated_by')
        depth = 1


class InterestQuestionSerializer(serializers.ModelSerializer):
    # time_management = serializers.SerializerMethodField('get_time')
    # answer_management = serializers.SerializerMethodField('get_answer')

    # def get_time(self, inst):
    #     user_test = UserInterestTest.objects.last()
    #     time_schedule = TestTimeSerializer(user_test).data
    #     # time_schedule['time_left_seconds'] = int(float(time_schedule['time_left']) * 60)
    #     time_schedule['test_id'] = user_test.id
    #     return time_schedule

    # def get_answer(self, inst):
    #     user_answer = AnswerModel.objects.filter(question_detail=inst)
    #     answer_detail = AnswerSerializer(user_answer, many=True).data
    #     return answer_detail

    class Meta:
        model = InterestQuestion
        fields = ('id', 'question_no', 'image', 'question',)
        # depth = 1


class InterestReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterestReportMaster
        fields = '__all__'


class FavoriteCareerSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteCareer
        fields = '__all__'
        read_only_fields = ('created_by', 'updated_by')


class CareerLibraryListSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=256)
    code = serializers.CharField(max_length=256)
    href = serializers.CharField(max_length=256)
    is_favourite = serializers.SerializerMethodField()

    def get_is_favourite(self, obj):
        request = self.context.get('user', None)
        if request:
            check = FavoriteCareer.objects.filter(name=obj['title'],
                                                  created_by=request)
            if check:
                return True
            else:
                return False
