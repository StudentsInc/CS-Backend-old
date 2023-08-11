from rest_framework import generics, permissions, viewsets, views, status
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from datetime import datetime, timedelta
import json, requests

# local import
from career_studio.settings import Onet_Token
from interest_app.serializer import *
from personality_test.models import PersonalityDashboard
from cms_app.models import *


def configure_datetime(minute):
    time_str = str(datetime.utcnow())
    date_format_str = '%Y-%m-%d %H:%M:%S.%f'
    given_time = datetime.strptime(time_str, date_format_str)
    final_time = given_time + timedelta(minutes=minute)
    return final_time


# define pagination
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 50


class InterestDetailView(views.APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = InterestDetailSerializer

    def post(self, request):
        try:
            if request.user.is_authenticated:
                queryset = InterestDetail.objects.last()
                serializer = self.serializer_class(queryset)
                qid = None
                interest = UserInterestTest.objects.filter(created_by=request.user, exam_status='InProgress')
                if interest:
                    qid = interest.last()
                else:
                    qid = UserInterestTest.objects.create(created_by=request.user, start_time=datetime.utcnow())
                ctx = serializer.data
                ctx['interest_id'] = qid.id
                return Response(ctx, status=status.HTTP_200_OK)
            else:
                queryset = InterestDetail.objects.last()
                serializer = self.serializer_class(queryset)
                guest_user = GuestUser.objects.get(token=request.data['guest_token'])
                qid = None
                interest = UserInterestTest.objects.filter(guest_user=guest_user, exam_status='InProgress')
                if interest:
                    qid = interest.last()
                else:
                    qid = UserInterestTest.objects.create(guest_user=guest_user, start_time=datetime.utcnow())
                ctx = serializer.data
                ctx['interest_id'] = qid.id
                return Response(ctx, status=status.HTTP_200_OK)
        except Exception as e:
            return Response([])


class InterestQuestionView(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = InterestQuestion.objects.all()
    serializer_class = InterestQuestionSerializer
    pagination_class = StandardResultsSetPagination

    def list(self, request, *args, **kwargs):
        interest_id = request.query_params.get('interest_id')
        result_page = self.paginate_queryset(self.get_queryset())
        serializer = InterestQuestionSerializer(result_page, many=True)
        ctx = []
        for item in serializer.data:
            dict_ctx = item
            interest = UserInterestTest.objects.get(id=interest_id)
            aid = interest.answer.all()
            answer = aid.filter(question_detail=item['id']).last()
            dict_ctx['answer_management'] = AnswerSerializer(answer).data
            dict_ctx['answer_management']['answer_choice'] = [5, 4, 3, 2, 1]
            ctx.append(dict_ctx)
        return self.get_paginated_response(ctx)


class AnswerSubmissionView(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = UserInterestTest.objects.all()
    serializer_class = UserInterestTestPostSerializer

    def create(self, request, *args, **kwargs):
        interest = UserInterestTest.objects.get(id=request.data['interest_id'])
        aid = interest.answer.all()
        answer = None

        if aid:
            answer = aid.filter(question_detail=request.data['question_id'])

        if answer:
            answer.update(answer=request.data['answer'])
            serializer = AnswerSerializer(answer.last())
            return Response(serializer.data)
        if request.user.is_authenticated:
            payload = {
                "created_by": request.user.pk,
                "answer": request.data['answer'],
                "question_detail": request.data['question_id']
            }
        else:
            guest_user = GuestUser.objects.get(token=request.data['guest_token'])
            payload = {
                "guest_user": guest_user.pk,
                "answer": request.data['answer'],
                "question_detail": request.data['question_id']
            }
        serializer = AnswerSerializer(data=payload)
        if serializer.is_valid():
            serializer.save()
            interest = UserInterestTest.objects.get(id=request.data['interest_id'])
            answer_id = [i.id for i in interest.answer.all()] + [serializer.data['id']]
            interest.answer.add(*answer_id)
            interest.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class TestTimeView(views.APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = TestTimeSerializer

    def post(self, request):
        query = InterestDetail.objects.get(id=request.data['interest_detail'])
        end_time = configure_datetime(query.duration)
        time_left = (end_time - datetime.utcnow()).seconds / 60
        if request.user.is_authenticated:
            payload = {
                "start_time": datetime.utcnow(),
                "end_time": end_time,
                "time_left": time_left,
                "created_by": request.user.pk
            }
        else:
            guest_user = GuestUser.objects.get(token=request.data['guest_token'])
            payload = {
                "start_time": datetime.utcnow(),
                "end_time": end_time,
                "time_left": time_left,
                "guest_user": guest_user.pk
            }
        serializer = self.serializer_class(data=payload)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class EndExamView(views.APIView):
    permission_classes = [permissions.AllowAny]

    def put(self, request):
        if request.user.is_authenticated:
            query = UserInterestTest.objects.filter(id=request.data['interest_id'], created_by=request.user)
            query.update(exam_status='Complete', end_time=datetime.utcnow())
            score_data = UserInterestTest.get_score(query.last())
            UserScores.objects.create(artistic_score=score_data['artistic_score'],
                                      social_score=score_data['social_score'],
                                      conventional_score=score_data['conventional_score'],
                                      realistic_score=score_data['realistic_score'],
                                      enterprising_score=score_data['enterprising_score'],
                                      investigative_score=score_data['investigative_score'],
                                      created_by=request.user, updated_by=request.user)
            interest_report = InterestReportMaster.objects.filter(report_category__in=score_data['report_list'])
            serializer = InterestReportSerializer(interest_report, many=True)
            ctx = {
                'message': 'Exam end successfully.',
                'report': serializer.data
            }
            return Response(ctx)
        else:
            guest_user = GuestUser.objects.get(token=request.data['guest_token'])
            query = UserInterestTest.objects.filter(id=request.data['interest_id'], guest_user=guest_user)
            query.update(exam_status='Complete', end_time=datetime.utcnow())
            score_data = UserInterestTest.get_score(query.last())
            UserScores.objects.create(artistic_score=score_data['artistic_score'],
                                      social_score=score_data['social_score'],
                                      conventional_score=score_data['conventional_score'],
                                      realistic_score=score_data['realistic_score'],
                                      enterprising_score=score_data['enterprising_score'],
                                      investigative_score=score_data['investigative_score'],
                                      guest_user=guest_user)
            interest_report = InterestReportMaster.objects.filter(report_category__in=score_data['report_list'])
            serializer = InterestReportSerializer(interest_report, many=True)
            ctx = {
                'message': 'Exam end successfully.',
                'report': serializer.data
            }
            return Response(ctx)


class InterestReportView(views.APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        if request.user.is_authenticated:
            query = UserInterestTest.objects.filter(created_by=request.user, exam_status='Complete')
            if query:
                score_data = UserInterestTest.get_score(query.last())
                interest_report = InterestReportMaster.objects.filter(report_category__in=score_data['report_list'])
                serializer = InterestReportSerializer(interest_report, many=True)
                personality_test = PersonalityDashboard.objects.filter(created_by=request.user)
                if personality_test:
                    return Response({'data': serializer.data, 'tests_finished': True})
                else:
                    return Response({'data': serializer.data, 'tests_finished': False})
            else:
                return Response([])
        else:
            guest_user = GuestUser.objects.get(token=request.data['guest_token'])
            query = UserInterestTest.objects.filter(guest_user=guest_user, exam_status='Complete')
            if query:
                score_data = UserInterestTest.get_score(query.last())
                interest_report = InterestReportMaster.objects.filter(report_category__in=score_data['report_list'])
                serializer = InterestReportSerializer(interest_report, many=True)
                return Response(serializer.data)
            else:
                return Response([])


class GetQuestion(views.APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        question_id = request.data['question_id']
        header = {
            "Accept": "application/json",
            "Authorization": "Basic " + Onet_Token,
        }
        net_data = requests.get(
            f"https://services.onetcenter.org/ws/mnm/interestprofiler/questions?start={question_id}&end={question_id}",
            headers=header)
        data = json.loads(net_data.text)
        saved_answer = None
        if request.user.is_authenticated:
            interest_data = InterestAnswerData.objects.filter(created_by=request.user, exam_status='InProgress')
        else:
            guest_user = GuestUser.objects.get(token=request.data['guest_token'])
            interest_data = InterestAnswerData.objects.filter(guest_user=guest_user, exam_status='InProgress')
        answer_data = list(interest_data.last().answer)
        if len(answer_data) >= int(request.data['question_id']):
            index = int(request.data['question_id']) - 1
            saved_answer = answer_data[index]
        return Response({'data': data, 'saved_answer': saved_answer})


class InterestAnswerDetailView(views.APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = InterestAnswerDetailSerializer

    def post(self, request):
        try:
            queryset = InterestDetail.objects.last()
            serializer = InterestDetailSerializer(queryset)
            last_year = datetime.today() - timedelta(days=365)
            qid = None
            if request.user.is_authenticated:
                check_interest = InterestAnswerData.objects.filter(created_by=request.user, exam_status='Complete',
                                                                   created_on__gte=last_year)
                if check_interest:
                    return Response({'exam_given': True}, status=status.HTTP_200_OK)
                else:
                    interest = InterestAnswerData.objects.filter(created_by=request.user, exam_status='InProgress')
                    if interest:
                        qid = len(interest.last().answer) + 1
                    else:
                        InterestAnswerData.objects.create(created_by=request.user, exam_status='InProgress')
                        qid = 1
            else:
                guest_user = GuestUser.objects.get(token=request.data['guest_token'])
                check_interest = InterestAnswerData.objects.filter(guest_user=guest_user, exam_status='Complete',
                                                                   created_on__gte=last_year)
                if check_interest:
                    return Response({'exam_given': True}, status=status.HTTP_200_OK)
                else:
                    interest = InterestAnswerData.objects.filter(guest_user=guest_user, exam_status='InProgress')
                    if interest:
                        qid = len(interest.last().answer) + 1
                    else:
                        InterestAnswerData.objects.create(guest_user=guest_user, exam_status='InProgress')
                        qid = 1
            ctx = serializer.data
            ctx['question_number'] = qid
            return Response(ctx, status=status.HTTP_200_OK)
        except Exception as e:
            return Response([])


class SubmitInterestQuestion(views.APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = InterestAnswerDetailSerializer

    def post(self, request):
        try:
            if request.user.is_authenticated:
                interest_data = InterestAnswerData.objects.filter(created_by=request.user, exam_status='InProgress')
                if interest_data:
                    question_id = int(request.data['question_id']) - 1
                    if len(interest_data.last().answer) == 0:
                        InterestAnswerData.objects.filter(created_by=request.user, exam_status='InProgress').update(
                            answer=request.data['value'])
                    if len(interest_data.last().answer) > 0:
                        answer_str = interest_data.last().answer
                        if len(answer_str) <= question_id:
                            new_string = answer_str + request.data['value']
                        else:
                            create_update = list(answer_str)
                            create_update[question_id] = request.data['value']
                            new_string = "".join(create_update)
                        InterestAnswerData.objects.filter(created_by=request.user, exam_status='InProgress').update(
                            answer=new_string)
                    interest_query = InterestAnswerData.objects.filter(created_by=request.user,
                                                                       exam_status='InProgress')
                    serializer = InterestAnswerDetailSerializer(interest_query.last())
                    return Response(serializer.data)
                else:
                    return Response([])
            else:
                guest_user = GuestUser.objects.get(token=request.data['guest_token'])
                interest_data = InterestAnswerData.objects.filter(guest_user=guest_user, exam_status='InProgress')
                if interest_data:
                    question_id = int(request.data['question_id']) - 1
                    if len(interest_data.last().answer) == 0:
                        InterestAnswerData.objects.filter(guest_user=guest_user, exam_status='InProgress').update(
                            answer=request.data['value'])
                    else:
                        answer_str = interest_data.last().answer
                        if len(answer_str) <= question_id:
                            new_string = answer_str + request.data['value']
                        else:
                            create_update = list(answer_str)
                            create_update[question_id] = request.data['value']
                            new_string = "".join(create_update)
                        InterestAnswerData.objects.filter(guest_user=guest_user, exam_status='InProgress').update(
                            answer=new_string)
                    queryset = InterestAnswerData.objects.filter(guest_user=guest_user, exam_status='InProgress').last()
                    serializer = InterestAnswerDetailSerializer(queryset)
                    return Response(serializer.data)
                else:
                    return Response([])
        except Exception as e:
            return Response([])


class InterestTestEndExam(views.APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        try:
            if request.user.is_authenticated:
                answer = InterestAnswerData.objects.filter(created_by=request.user,
                                                           exam_status='InProgress')
            else:
                guest_user = GuestUser.objects.get(token=request.data['guest_token'])
                answer = InterestAnswerData.objects.filter(guest_user=guest_user,
                                                           exam_status='InProgress')
            header = {
                "Accept": "application/json",
                "Authorization": "Basic " + Onet_Token,
            }
            result = requests.get(
                "https://services.onetcenter.org/ws/mnm/interestprofiler/results?answers=" + answer.last().answer,
                headers=header)
            data = json.loads(result.text)
            realistic_score = data['result'][0]['score']
            investigative_score = data['result'][1]['score']
            artistic_score = data['result'][2]['score']
            social_score = data['result'][3]['score']
            enterprising_score = data['result'][4]['score']
            conventional_score = data['result'][5]['score']
            answer.update(exam_status='Complete')
            if request.user.is_authenticated:
                UserScores.objects.create(artistic_score=artistic_score, realistic_score=realistic_score,
                                          investigative_score=investigative_score, social_score=social_score,
                                          enterprising_score=enterprising_score,
                                          conventional_score=conventional_score, created_by=request.user)
            else:
                UserScores.objects.create(artistic_score=artistic_score, realistic_score=realistic_score,
                                          investigative_score=investigative_score, social_score=social_score,
                                          enterprising_score=enterprising_score,
                                          conventional_score=conventional_score, guest_user=guest_user)
            return Response({'data': data, 'message': 'Exam Completed', 'status': True}, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response([])


class CareerLibraryList(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        detail = request.data.get('detail')
        category = request.data['category']
        start = request.data['start']
        end = request.data['end']
        score_data = UserScores.objects.filter(created_by=request.user).last()
        if category == 'Artistic':
            score = score_data.artistic_score
        elif category == 'Realistic':
            score = score_data.realistic_score
        elif category == 'Social':
            score = score_data.social_score
        elif category == 'Conventional':
            score = score_data.conventional_score
        elif category == 'Enterprising':
            score = score_data.enterprising_score
        elif category == 'Investigative':
            score = score_data.investigative_score
        answer_str = InterestAnswerData.objects.filter(created_by=request.user)
        header = {
            "Accept": "application/json",
            "Authorization": "Basic " + Onet_Token,
        }
        if detail is not None:
            result = requests.get(
                f"https://services.onetcenter.org/ws/mnm/interestprofiler/careers?area={category}&score={score}&start={start}&end={end}"
                f"&answers={answer_str.last().answer}",
                headers=header)
            json_data = json.loads(result.text)
            serializer = CareerLibraryListSerializer(json_data['career'],
                                                     context={'user': self.request.user}, many=True)
            return Response({'career': serializer.data, 'start': json_data['start'], 'end': json_data['end'],
                             'total': json_data['total']})
        else:
            result = requests.get(
                f"https://services.onetcenter.org/ws/mnm/interestprofiler/careers?area={category}&start={start}&end={end}",
                headers=header)
            json_data = json.loads(result.text)
            serializer = CareerLibraryListSerializer(json_data['career'],
                                                     context={'user': self.request.user}, many=True)
            return Response({'career': serializer.data, 'start': json_data['start'], 'end': json_data['end'],
                             'total': json_data['total']})


class AddFavoriteList(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        query = FavoriteCareer.objects.filter(created_by=request.user)
        serializer = FavoriteCareerSerializer(query, many=True)
        return Response(serializer.data)


class AddFavorite(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, name):
        query = FavoriteCareer.objects.filter(name=name, created_by=request.user)
        serializer = FavoriteCareerSerializer(query, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FavoriteCareerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data)
        return Response(serializer.errors)


class DeleteFavourite(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        favorite = FavoriteCareer.objects.filter(name=request.data['name'], created_by=request.user).delete()
        return Response({'message': 'Marked not Favorite', 'status': True}, status=status.HTTP_200_OK)


class InterestTestReportView(views.APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        if request.user.is_authenticated:
            query = InterestAnswerData.objects.filter(created_by=request.user, exam_status='Complete')
            if query:
                user_score = UserScores.objects.filter(created_by=request.user)
                score_data = UserScores.get_user_score(user_score.last())
                interest_report = InterestReportMaster.objects.filter(report_category__in=score_data['report_list'])
                serializer = InterestReportSerializer(interest_report, many=True)
                personality_test = PersonalityDashboard.objects.filter(created_by=request.user)
                career_select = UserSelectedCareer.objects.filter(created_by=request.user)
                major_select = UserSelectedMajor.objects.filter(created_by=request.user)

                if personality_test:
                    state = 0
                    if career_select:
                        state = 1
                    if major_select:
                        state = 2
                    return Response({'data': serializer.data, 'tests_finished': True})
                else:
                    return Response({'data': serializer.data, 'tests_finished': False, 'state': 0})
            else:
                return Response([])
        else:
            guest_user = GuestUser.objects.get(token=request.data['guest_token'])
            query = InterestAnswerData.objects.filter(guest_user=guest_user, exam_status='Complete')
            if query:
                user_score = UserScores.objects.filter(guest_user=guest_user)
                score_data = UserScores.get_user_score(user_score.last())
                interest_report = InterestReportMaster.objects.filter(report_category__in=score_data['report_list'])
                serializer = InterestReportSerializer(interest_report, many=True)
                return Response(serializer.data)
            else:
                return Response([])


# guest user
class GuestCareerLibraryList(views.APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        detail = request.data.get('detail')
        category = request.data['category']
        start = request.data['start']
        end = request.data['end']
        # score_data = UserScores.objects.filter(created_by=request.user).last()
        if category == 'Artistic':
            score = 40
        elif category == 'Realistic':
            score = 50
        elif category == 'Social':
            score = 31
        elif category == 'Conventional':
            score = 29
        elif category == 'Enterprising':
            score = 31
        elif category == 'Investigative':
            score = 35

        # answer_str = InterestAnswerData.objects.filter(created_by=request.user)
        header = {
            "Accept": "application/json",
            "Authorization": "Basic " + Onet_Token,
        }

        result = requests.get(
            f"https://services.onetcenter.org/ws/mnm/interestprofiler/careers?area={category}&start={start}&end={end}",
            headers=header)
        json_data = json.loads(result.text)
        serializer = CareerLibraryListSerializer(json_data['career'], many=True)
        return Response({'career': serializer.data, 'start': json_data['start'], 'end': json_data['end'],
                         'total': json_data['total']})
#