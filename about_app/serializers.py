from rest_framework import serializers
from about_app.models import *


class OurAchievementItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurAchievementItems
        exclude = ('created_on', 'updated_on', 'created_by', 'updated_by', 'status')


class OurAchievementSerializer(serializers.ModelSerializer):
    our_achivement_items = OurAchievementItemsSerializer(many=True)

    class Meta:
        model = OurAchievement
        fields = ('heading', 'subheading', 'our_achivement_items')


class OurTeamItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurTeamItems
        exclude = ('created_on', 'updated_on', 'created_by', 'updated_by', 'status')


class OurTeamSerializer(serializers.ModelSerializer):
    our_teams = OurTeamItemsSerializer(many=True)

    class Meta:
        model = OurTeam
        fields = ('heading', 'subheading', 'our_teams')
