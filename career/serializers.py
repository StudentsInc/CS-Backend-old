from rest_framework import serializers
from .models import *


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class AlternativeTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlternativeTitles
        fields = '__all__'


class CareerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CareerProfile
        fields = '__all__'


class CareerProfileGlanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CareerProfileGlance
        fields = '__all__'


class AverageSalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = AverageSalary
        fields = '__all__'


class CareerEducationRequirementSerializer(serializers.ModelSerializer):
    class Meta:
        model = CareerEducationRequirement
        fields = '__all__'


class CareerCommonIndustriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CareerCommonIndustries
        fields = '__all__'


class CareerCommonIndustriesBreakupSerializer(serializers.ModelSerializer):
    class Meta:
        model = CareerCommonIndustriesBreakup
        fields = '__all__'


class AssessmentCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = AssessmentCategory
        fields = '__all__'


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'


class AssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assessment
        fields = '__all__'


class UserAssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAssessment
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


class SchoolMajorSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolMajorSubject
        fields = '__all__'


class SelectedSchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = SelectedSchool
        fields = '__all__'
