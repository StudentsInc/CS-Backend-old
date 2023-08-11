from rest_framework import status, permissions, viewsets, views
from rest_framework.response import Response
from datetime import datetime

# local import
from learning_style.serializer import *
from interest_app.views import StandardResultsSetPagination


# Create your views here.
class LearningQuestionView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = LearningQuestionSerializer
    queryset = LearningQuestion.objects.all()
    pagination_class = StandardResultsSetPagination

    def list(self, request):
        learning_id = request.query_params.get('learning_id')
        result_page = self.paginate_queryset(self.get_queryset())
        serializer = self.serializer_class(result_page, many=True)
        ctx = []
        for item in serializer.data:
            dict_ctx = item
            interest = LearningUserInterestTest.objects.get(id=learning_id)
            aid = interest.answer.all()
            answer = aid.filter(question_detail=item['id']).last()
            dict_ctx['answer_management'] = LearningAnswerModelSerializer(answer).data
            ctx.append(dict_ctx)
        return self.get_paginated_response(ctx)


class GenerateUIDView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = LearningUserInterestTestSerializer
    queryset = LearningUserInterestTest.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset().filter(created_by=request.user)
        query_progress_id = None
        if queryset:
            query_progress = queryset.filter(exam_status='InProgress')
            query_progress_id = query_progress.last().id if query_progress else None
        else:
            obj = LearningUserInterestTest.objects.create(created_by=request.user, start_time=datetime.utcnow(),
                                                          exam_status='InProgress')
            query_progress_id = obj.id
        ctx = {
            "message": "Exam id generated successfully.",
            "learning_id": query_progress_id
        }
        return Response(ctx, status=status.HTTP_200_OK)


class AnswerSubmissionView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = LearningUserInterestTest.objects.all()
    serializer_class = LearningUserInterestTestSerializer

    def create(self, request, *args, **kwargs):
        learning = LearningUserInterestTest.objects.get(id=request.data['learning_id'])
        aid = learning.answer.all()
        answer = None

        if aid:
            answer = aid.filter(question_detail=request.data['question_id'])

        if answer:
            answer.update(answer=request.data['answer'])
            serializer = LearningAnswerModelSerializer(answer.last())
            return Response(serializer.data)

        payload = {
            "created_by": request.user.pk,
            "answer": request.data['answer'],
            "question_detail": request.data['question_id']
        }
        serializer = LearningAnswerModelSerializer(data=payload)
        if serializer.is_valid():
            serializer.save()
            learning = LearningUserInterestTest.objects.get(id=request.data['learning_id'])
            answer_id = [i.id for i in learning.answer.all()] + [serializer.data['id']]
            learning.answer.add(*answer_id)
            learning.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class EndExamView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request):
        query = LearningUserInterestTest.objects.filter(id=request.data['learning_id'], created_by=request.user)
        query.update(exam_status='Complete', end_time=datetime.utcnow())
        ctx = {
            'message': 'Exam end successfully.'
        }
        return Response(ctx)
