# third party import
from rest_framework import views, permissions
from rest_framework.response import Response

# local import
from home_app.serializers import *
from about_app.serializers import *


# Create your views here.
class AboutView(views.APIView):
    """
    this class merge 4 models for ui/ux
    """
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        about_query = About.objects.filter(status='active').last()
        our_achievement_query = OurAchievement.objects.last()
        team_query = OurTeam.objects.filter(status='active').last()
        brand_query = Brand.objects.filter(status='active').last()

        ctx = {
            "about_us": AboutSerializer(about_query).data,
            "achievement": OurAchievementSerializer(our_achievement_query).data,
            "teams": OurTeamSerializer(team_query).data,
            "brand": BrandSerializer(brand_query).data,
        }
        return Response(ctx)
