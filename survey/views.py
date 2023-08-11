from .serializers import SurveySerializer, UserSurveySerializer, UserSurveyListSerializer
from .models import SurveyQuestion, UserSurvey
from rest_framework import generics, permissions, viewsets, views, status
from rest_framework.response import Response


class SurveyView(viewsets.ModelViewSet):
    serializer_class = SurveySerializer
    queryset = SurveyQuestion.objects.all()
    pagination_class = None


class UserSurveyView(viewsets.ModelViewSet):
    http_method_names = ('get', 'post',)
    serializer_class = UserSurveySerializer
    queryset = UserSurvey.objects.all()
    permission_classes = [permissions.IsAuthenticated, ]

    def list(self, request, *args, **kwargs):
        query = UserSurvey.objects.filter(created_by=request.user)
        serializer = UserSurveyListSerializer(query, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        question = UserSurvey.objects.filter(question=request.data['question'])

        if question:
            question.update(answer_type=request.data.get('answer_type'), answer_text=request.data.get('answer_text'))
            serializer = UserSurveySerializer(question.last())
            return Response(serializer.data)

        payload = {
            "created_by": request.user.pk,
            "updated_by": request.user.pk,
            "answer_type": request.data.get('answer_type'),
            "answer_text": request.data.get('answer_text'),
            "question": request.data['question'],
        }
        serializer = UserSurveySerializer(data=payload)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)