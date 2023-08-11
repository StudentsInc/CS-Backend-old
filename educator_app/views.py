# third party import
from rest_framework import views, permissions
from rest_framework.response import Response

# local import
from educator_app.serializers import *


# Create your views here.
class EducatorView(views.APIView):
    """
    this class for educators
    """
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        high_school_query = Educator.objects.filter(educator_type="high-school").last()
        post_secondary_query = Educator.objects.filter(educator_type="post-secondary").last()

        ctx = {
            "high_school": EducatorsSerializer(high_school_query).data,
            "postsecondary": EducatorsSerializer(post_secondary_query).data,
        }
        return Response(ctx)


class HighSchoolView(views.APIView):
    """
    this class merge 4 models for ui/ux
    """
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        highschool_query = HighSchool.objects.last()

        ctx = {
            **HighSchoolSerializer(highschool_query).data,

        }
        return Response(ctx)


class PostSecondaryView(views.APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        query = PostSecondary.objects.last()
        serializer = PostSecondarySerializer(query)
        return Response(serializer.data)
