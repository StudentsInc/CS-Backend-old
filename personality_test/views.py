from functools import reduce

from rest_framework import generics, permissions, viewsets, views, status
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from datetime import datetime, timedelta
from django_filters.rest_framework import DjangoFilterBackend

# local import
from account_app.models import GuestUser
from cms_app.models import CareerLibrary
from cms_app.serializers import CareerLibrarySerializer
from personality_test.serializers import *


class ReasonView(viewsets.ModelViewSet):
    serializer_class = ReasonSerializer
    queryset = Reason.objects.all()

    def list(self, request, *args, **kwargs):
        query = self.queryset
        serializer = ReasonSerializer(query, many=True)
        return Response(serializer.data)


class EducationLevelView(viewsets.ModelViewSet):
    serializer_class = EducationLevelSerializer
    queryset = EducationLevel.objects.all()

    def list(self, request, *args, **kwargs):
        query = self.queryset
        serializer = EducationLevelSerializer(query, many=True)
        return Response(serializer.data)


def configure_datetime(minute):
    time_str = str(datetime.utcnow())
    date_format_str = '%Y-%m-%d %H:%M:%S.%f'
    given_time = datetime.strptime(time_str, date_format_str)
    final_time = given_time + timedelta(minutes=minute)
    return final_time


# define pagination
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 50


class PersonalityDetailView(viewsets.ModelViewSet):
    http_method_names = ('post',)
    permission_classes = [permissions.AllowAny]
    serializer_class = GuestTokenInputSerializer
    queryset = PersonalityDetail.objects.all()

    def create(self, request, *args, **kwargs):
        last_year = datetime.today() - timedelta(days=365)
        try:
            if request.user.is_authenticated:
                check_test = PersonalityTest.objects.filter(created_by=request.user, exam_status='Complete',
                                                            created_on__gte=last_year)
                if check_test:
                    return Response({'exam_given': True}, status=status.HTTP_200_OK)
                else:
                    queryset = PersonalityDetail.objects.last()
                    serializer = PersonalityDetailSerializer(queryset)
                    qid = None
                    interest = PersonalityTest.objects.filter(created_by=request.user, exam_status='InProgress')
                    if interest:
                        qid = interest.last()
                    else:
                        qid = PersonalityTest.objects.create(created_by=request.user, start_time=datetime.utcnow())
                    ctx = serializer.data
                    ctx['personality_id'] = qid.id
                    return Response(ctx, status=status.HTTP_200_OK)
            else:
                queryset = PersonalityDetail.objects.last()
                serializer = PersonalityDetailSerializer(queryset)
                guest_user = GuestUser.objects.get(token=request.data['guest_token'])
                check_test = PersonalityTest.objects.filter(created_by=request.user, exam_status='Complete',
                                                            created_on__gte=last_year)
                if check_test:
                    return Response({'exam_given': True}, status=status.HTTP_200_OK)
                else:
                    qid = None
                    interest = PersonalityTest.objects.filter(guest_user=guest_user, exam_status='InProgress')
                    if interest:
                        qid = interest.last()
                    else:
                        qid = PersonalityTest.objects.create(guest_user=guest_user, start_time=datetime.utcnow())
                    ctx = serializer.data
                    ctx['personality_id'] = qid.id
                    return Response(ctx, status=status.HTTP_200_OK)
        except Exception as e:
            return Response([])


class PersonalityQuestionView(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = PersonalityQuestion.objects.all()
    serializer_class = PersonalityQuestionListSerializer
    pagination_class = None

    def create(self, request, *args, **kwargs):
        personality_id = request.data.get('personality_id')
        result_page = PersonalityQuestion.objects.filter(question_type=request.data['question_type'])
        serializer = PersonalityQuestionSerializer(result_page, many=True)
        ctx = []
        for item in serializer.data:
            dict_ctx = item
            interest = PersonalityTest.objects.get(id=personality_id)
            aid = interest.personality_test.all()
            answer = aid.filter(personality_question=item['id']).last()
            dict_ctx['answer_management'] = PersonalityAnswerSerializer(answer).data
            answer_list = ['strongly_agree', 'agree', 'neutral', 'disagree', 'strongly_disagree']
            dict_ctx['answer_management']['answer_choice'] = answer_list
            ctx.append(dict_ctx)
        return Response(ctx)


class PersonalityAnswerSubmissionView(viewsets.ModelViewSet):
    http_method_names = ('get', 'post')
    permission_classes = [permissions.AllowAny]
    queryset = PersonalityTest.objects.all()
    serializer_class = PersonalityTestPostSerializer

    def list(self, request, *args, **kwargs):
        query = PersonalityTest.objects.all()

    def create(self, request, *args, **kwargs):
        interest = PersonalityTest.objects.get(id=request.data['personality_id'])
        aid = interest.personality_test.all()
        answer = None

        if aid:
            answer = aid.filter(personality_question=request.data['question_id'])

        if answer:
            answer.update(answer_type=request.data['answer'], score=request.data['score'])
            serializer = PersonalityAnswerSerializer(answer.last())
            return Response(serializer.data)

        if request.user.is_authenticated:
            payload = {
                "created_by": request.user.pk,
                "answer_type": request.data['answer'],
                "personality_question": request.data['question_id'],
                "score": request.data['score']
            }
        else:
            guest_user = GuestUser.objects.get(token=request.data['guest_token'])
            payload = {
                "guest_user": guest_user.pk,
                "answer_type": request.data['answer'],
                "personality_question": request.data['question_id'],
                "score": request.data['score']
            }
        serializer = PersonalityAnswerSerializer(data=payload)
        if serializer.is_valid():
            serializer.save()
            interest = PersonalityTest.objects.get(id=request.data['personality_id'])
            answer_id = [i.id for i in interest.personality_test.all()] + [serializer.data['id']]
            interest.personality_test.add(*answer_id)
            interest.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class PersonalityTestTimeView(viewsets.ModelViewSet):
    http_method_names = ('post',)
    permission_classes = [permissions.AllowAny]
    serializer_class = TestTimeSerializer
    queryset = PersonalityTest.objects.all()

    def create(self, request, *args, **kwargs):
        query = PersonalityDetail.objects.get(id=request.data['personality_detail'])
        end_time = configure_datetime(query.duration)
        time_left = (end_time - datetime.utcnow()).seconds / 60
        payload = {
            "start_time": datetime.utcnow(),
            "end_time": end_time,
            "time_left": time_left,
            "created_by": request.user.pk
        }
        serializer = PersonalityTestTimeSerializer(data=payload)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class PersonalityEndExamView(viewsets.ModelViewSet):
    http_method_names = ('post',)
    permission_classes = [permissions.AllowAny]
    queryset = PersonalityTest.objects.all()
    serializer_class = EndTimeSerializer

    def create(self, request, *args, **kwargs):
        """
        This post request contains the ending of exam and also calculates the dashboard result and personality test
        report and also saves the data in User Assessment and Personality Dashboard.
        """
        if request.user.is_authenticated:
            personality_test = PersonalityTest.objects.filter(id=request.data['personality_test_id'],
                                                              created_by=request.user)
            user_detail = UserDetail.objects.get(id=request.data['user_detail_id'])
            personality_test.update(exam_status='Complete', end_time=datetime.utcnow(), user_detail=user_detail)
            PersonalityTest.assessment_stats_save(personality_test.last())
            current_user = PersonalityTest.user_scores(personality_test.last())
            ctx = PersonalityTest.status_type(personality_test.last())
            UserAssesmentStats.objects.create(assesment=personality_test.last(), extravert=ctx['extravert_status'],
                                              adventurous=ctx['adventurous_status'], agreeable=ctx['agreeable_status'],
                                              neurotic=ctx['neurotic_status'],
                                              conscientious=ctx['conscientious_status'],
                                              extravert_score=current_user['extravert_score'],
                                              adventurous_score=current_user['adventurous_score'],
                                              agreeable_score=current_user['agreeable_score'],
                                              neurotic_score=current_user['neurotic_score'],
                                              conscientious_score=current_user['conscientious_score'],
                                              created_by=request.user)
            dashboard_data = PersonalityTest.dashboard_data(personality_test.last())
            PersonalityDashboard.objects.create(extravert_scale=dashboard_data['extravert_dashboard'],
                                                adventurous_scale=dashboard_data['adventurous_dashboard'],
                                                agreeable_scale=dashboard_data['agreeable_dashboard'],
                                                neurotic_scale=dashboard_data['neurotic_dashboard'],
                                                conscientious_scale=dashboard_data['conscientious_dashboard'],
                                                extravert_score=dashboard_data['extravert_score'],
                                                adventurous_score=dashboard_data['adventurous_score'],
                                                agreeable_score=dashboard_data['agreeable_score'],
                                                neurotic_score=dashboard_data['neurotic_score'],
                                                conscientious_score=dashboard_data['conscientious_score'],
                                                created_by=request.user, updated_by=request.user)
            context = {
                'message': 'Exam ended successfully.'
            }
            return Response(context)
        else:
            guest_user = GuestUser.objects.get(token=request.data['guest_token'])
            personality_test = PersonalityTest.objects.filter(id=request.data['personality_test_id'],
                                                              guest_user=guest_user)
            user_detail = UserDetail.objects.get(id=request.data['user_detail_id'])
            personality_test.update(exam_status='Complete', end_time=datetime.utcnow(), user_detail=user_detail)
            PersonalityTest.assessment_stats_save(personality_test.last())
            current_user = PersonalityTest.user_scores(personality_test.last())
            ctx = PersonalityTest.status_type(personality_test.last())
            UserAssesmentStats.objects.create(assesment=personality_test.last(), extravert=ctx['extravert_status'],
                                              adventurous=ctx['adventurous_status'], agreeable=ctx['agreeable_status'],
                                              neurotic=ctx['neurotic_status'],
                                              conscientious=ctx['conscientious_status'],
                                              extravert_score=current_user['extravert_score'],
                                              adventurous_score=current_user['adventurous_score'],
                                              agreeable_score=current_user['agreeable_score'],
                                              neurotic_score=current_user['neurotic_score'],
                                              conscientious_score=current_user['conscientious_score'],
                                              guest_user=guest_user)
            dashboard_data = PersonalityTest.dashboard_data(personality_test.last())
            PersonalityDashboard.objects.create(extravert_scale=dashboard_data['extravert_dashboard'],
                                                adventurous_scale=dashboard_data['adventurous_dashboard'],
                                                agreeable_scale=dashboard_data['agreeable_dashboard'],
                                                neurotic_scale=dashboard_data['neurotic_dashboard'],
                                                conscientious_scale=dashboard_data['conscientious_dashboard'],
                                                extravert_score=dashboard_data['extravert_score'],
                                                adventurous_score=dashboard_data['adventurous_score'],
                                                agreeable_score=dashboard_data['agreeable_score'],
                                                neurotic_score=dashboard_data['neurotic_score'],
                                                conscientious_score=dashboard_data['conscientious_score'],
                                                guest_user=guest_user)
            context = {
                'message': 'Exam ended successfully.'
            }
            return Response(context)


class UserDetailView(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = UserDetail.objects.all()
    serializer_class = UserDetailSerializer


class GetReport(viewsets.ModelViewSet):
    http_method_names = ('post',)
    permission_classes = [permissions.AllowAny]
    queryset = PersonalityTest.objects.all()
    serializer_class = GuestTokenInputSerializer

    def create(self, request, *args, **kwargs):
        """
        It will give the real time data result of the user based on all users score and been calculated accordingly.
        """
        if request.user.is_authenticated:
            personality_test_data = PersonalityTest.objects.filter(created_by=request.user).last()
            current_user = PersonalityTest.user_scores(personality_test_data)
            PersonalityTest.dashboard_data(personality_test_data)
            ctx = PersonalityTest.status_type(personality_test_data)
            return Response({'user_score': current_user, 'user_status': ctx})
        else:
            guest_user = GuestUser.objects.get(token=request.data['guest_token'])
            personality_test_data = PersonalityTest.objects.filter(guest_user=guest_user).last()
            current_user = PersonalityTest.user_scores(personality_test_data)
            PersonalityTest.dashboard_data(personality_test_data)
            ctx = PersonalityTest.status_type(personality_test_data)
            return Response({'user_score': current_user, 'user_status': ctx})


class UserJobType(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = CareerLibrary.objects.all()
    serializer_class = CareerLibrarySerializer
    pagination_class = StandardResultsSetPagination

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset()).filter(career_options=request.query_params.get('category'),
                                                                    job_category=request.query_params.get('job_type'))

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class PersonalityAssessmentDashboard(viewsets.ModelViewSet):
    http_method_names = ('post',)
    permission_classes = [permissions.AllowAny]
    queryset = PersonalityDashboard.objects.all()
    serializer_class = GuestTokenInputSerializer
    pagination_class = None

    def create(self, request, *args, **kwargs):
        """
        It will give the dashboard data that to be shown of personality test and personality report.
        """
        if request.user.is_authenticated:
            queryset = self.filter_queryset(self.get_queryset()).filter(created_by=request.user).last()
            serializer = PersonalityDashboardSerializer(queryset)
            return Response(serializer.data)
        else:
            guest_user = GuestUser.objects.get(token=request.data['guest_token'])
            queryset = self.filter_queryset(self.get_queryset()).filter(guest_user=guest_user).last()
            serializer = PersonalityDashboardSerializer(queryset)
            return Response(serializer.data)


class PersonalityReportViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = PersonalityReportMaster.objects.all()
    serializer_class = PersonalityReportSerializer
    pagination_class = None
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'score']

    def list(self, request, *args, **kwargs):
        """
        It will give the dashboard data that to be shown of personality test and personality report.
        """
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
