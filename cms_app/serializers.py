from rest_framework import serializers

from interest_app.models import FavoriteCareer
from .models import *
from rest_framework.fields import CurrentUserDefault
from cms_app.custom_method import career_values


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = '__all__'


class PrivacyPolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = PrivacyPolicy
        fields = '__all__'


class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = '__all__'


class TermsAndConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TermsAndCondition
        fields = '__all__'


class CareerLibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = CareerLibrary
        fields = '__all__'


class CareerLibraryListSerializer(serializers.ModelSerializer):
    career_library = CareerLibrarySerializer()

    class Meta:
        model = CareerLibraryUser
        fields = '__all__'
        read_only_fields = ('created_by', 'updated_by')


class CareerLibraryPostSerializer(serializers.Serializer):
    career_options = serializers.CharField(max_length=100, required=True)
    extravert_job_type = serializers.CharField(max_length=100, required=True)
    adventurous_job_type = serializers.CharField(max_length=100, required=True)
    agreeable_job_type = serializers.CharField(max_length=100, required=True)
    neurotic_job_type = serializers.CharField(max_length=100, required=True)
    conscientious_job_type = serializers.CharField(max_length=100, required=True)


class CareerLibraryUserSerializer(serializers.Serializer):
    career_library_id = serializers.IntegerField(required=True)


class CareerLibraryFavoriteSerializer(serializers.ModelSerializer):
    is_favorite = serializers.SerializerMethodField()

    def get_is_favorite(self, obj, user):
        data = CareerLibraryUser.objects.filter(career_library=obj.id, created_by=user)
        if data:
            return True
        else:
            return False

    class Meta:
        model = JobMaster
        fields = '__all__'


class JobMasterSerializer(serializers.ModelSerializer):
    is_selected = serializers.SerializerMethodField()
    is_favourite = serializers.SerializerMethodField()
    is_recommendate = serializers.SerializerMethodField()

    def get_is_selected(self, obj):
        request = self.context.get('user', None)
        if request:
            check = SelectCareer.objects.filter(name=obj.title, created_by=request)
            if check:
                return True
            else:
                return False

    def get_is_favourite(self, obj):
        request = self.context.get('user', None)
        if request:
            name = obj.title.replace('and', '&')
            check = FavoriteCareer.objects.filter(name=name, created_by=request)
            if check:
                return True
            else:
                return False

    def get_is_recommendate(self, obj):
        request = self.context.get('user', None)
        if request:
            check = RecommendationNot.objects.filter(title=obj.title, created_by=request)
            if check:
                return False
            else:
                return True

    class Meta:
        model = JobMaster
        fields = '__all__'


class SelectCareerSerializer(serializers.ModelSerializer):
    class Meta:
        model = SelectCareer
        fields = '__all__'
        read_only_fields = ('created_by', 'updated_by', 'status')


class SelectCareerDetailSerializer(serializers.ModelSerializer):
    values_result = serializers.SerializerMethodField('get_values_result')
    selected = serializers.SerializerMethodField('get_selected_career')

    def get_values_result(self, inst):
        values_ref = self.context.get('values_ref')
        keys_ref = self.context.get('keys_ref')
        result_work_test = self.context.get('result_work_test')
        if inst:
            query = CareerValues.objects.filter(title=inst.name)
            res = career_values(query, values_ref, keys_ref, result_work_test)
            return res['values']

    def get_selected_career(self, inst):
        user = self.context.get('user')
        query = UserSelectedCareer.objects.filter(created_by=user, career=inst)
        if query:
            return True
        return False

    class Meta:
        model = SelectCareer
        fields = '__all__'
        read_only_fields = ('created_by', 'updated_by', 'status')


class RecommendationNotSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecommendationNot
        fields = '__all__'
        read_only_fields = ('created_by', 'updated_by', 'status')


class CareerLibraryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CareerLibraryDetail
        fields = '__all__'


class SoftSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoftSkills
        fields = '__all__'


class HardSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = HardSkills
        fields = '__all__'


class WorkValuesItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkValueItems
        fields = '__all__'


class UserWorkValuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserWorkValues
        fields = '__all__'


class CareerValuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CareerValues
        fields = '__all__'


class MajorSerializer(serializers.ModelSerializer):
    selected = serializers.SerializerMethodField('get_selected')

    def get_selected(self, inst):
        user = self.context.get('user')
        query = UserSelectedMajor.objects.filter(created_by=user, major=inst)
        if query:
            return True
        return False

    class Meta:
        model = Major
        fields = '__all__'


class UserMajorSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSelectedMajor
        fields = '__all__'


class UserSelectedCareerSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSelectedCareer
        fields = '__all__'


class MajorSubjectSerializer(serializers.ModelSerializer):
    career = serializers.SerializerMethodField('get_career')
    major = MajorSerializer()

    def get_career(self, *args, **kwargs):
        return self.instance.first().major.typical_careers

    class Meta:
        model = MajorSubject
        fields = '__all__'
