import json
import requests
import random
from functools import reduce
from rest_framework.authtoken.models import Token
from rest_framework import status, response, viewsets, views
from career_studio.settings import Onet_Token, Frontend_url, EMAIL_FROM
from interest_app.models import UserScores, InterestAnswerData
from personality_test.models import PersonalityTest
from cms_app.serializers import *
from django.views import View
from django.core.mail import send_mail
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics, permissions
from rest_framework.response import Response
from django.db.models import Q
from cms_app.custom_method import value_calculation, career_values
from utils.custom_mixin import QuerySetFilterMixin
from univercity_app.serializers import SchoolProfileSerializer
from univercity_app.models import SchoolProfile


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 1000


class StandardQNAPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 30


class FAQListView(generics.ListAPIView):
    '''
    This API accepts a GET request and return all the FAQ objects in descending order.
    '''
    queryset = FAQ.objects.order_by('-id').all()
    serializer_class = FAQSerializer


class LatestPrivacyPolicyView(generics.GenericAPIView):
    '''
    This API accepts a GET request and return latest privacy policy object.
    '''
    queryset = PrivacyPolicy.objects.all()
    serializer_class = PrivacyPolicySerializer

    def get(self, request):
        self.queryset = PrivacyPolicy.objects.order_by('id').last()
        return response.Response(self.serializer_class(self.queryset, many=False).data, status=status.HTTP_200_OK)


class LatestAboutUsView(generics.ListAPIView):
    '''
    This API accepts a GET request and return latest about us object.
    '''
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer

    def get(self, request):
        self.queryset = AboutUs.objects.order_by('id').last()
        return response.Response(self.serializer_class(self.queryset, many=False).data, status=status.HTTP_200_OK)


class LatestTermsAndConditionView(generics.ListAPIView):
    '''
    This API accepts a GET request and return latest about us object.
    '''
    queryset = TermsAndCondition.objects.all()
    serializer_class = TermsAndConditionSerializer

    def get(self, request):
        self.queryset = TermsAndCondition.objects.order_by('id').last()
        return response.Response(self.serializer_class(self.queryset, many=False).data, status=status.HTTP_200_OK)


class AboutUsPageView(View):
    template_name = 'cms_app/about-us.html'

    def get(self, request):
        ctx = {
            'about_us': AboutUs.objects.order_by('id').last()
        }
        return render(request, self.template_name, ctx)


class PrivacyPolicyPageView(View):
    template_name = 'cms_app/privacy-policy.html'

    def get(self, request):
        ctx = {
            'privacy_policy': PrivacyPolicy.objects.order_by('id').last()
        }
        return render(request, self.template_name, ctx)


class TermsAndConditionPageView(View):
    template_name = 'cms_app/terms-and-condition.html'

    def get(self, request):
        ctx = {
            'terms_and_condition': TermsAndCondition.objects.order_by('id').last()
        }
        return render(request, self.template_name, ctx)


class CareerLibraryView(viewsets.ModelViewSet):
    queryset = CareerLibrary.objects.all()
    serializer_class = CareerLibrarySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['career_options']
    pagination_class = StandardResultsSetPagination


class CareerLibraryUserView(viewsets.ModelViewSet):
    http_method_names = ('post',)
    queryset = CareerLibraryUser.objects.all()
    serializer_class = CareerLibraryUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        career_id = request.data['career_library_id']
        query = CareerLibraryUser.objects.filter(career_library=career_id)
        if query:
            delete = CareerLibraryUser.objects.filter(career_library=career_id).delete()
            return Response({'message': 'Marked Unimportant'}, status=status.HTTP_200_OK)
        else:
            career_instance = JobMaster.objects.get(id=career_id)
            payload = {
                'career_library': career_instance,
                'is_important': True,
                'created_by': request.user,
                'updated_by': request.user,
            }
            CareerLibraryUser.objects.create(**payload)
            return Response({'message': 'Marked Important'}, status=status.HTTP_200_OK)


class CareerLibraryListView(viewsets.ModelViewSet):
    http_method_names = ('post',)
    queryset = CareerLibrary.objects.all()
    serializer_class = CareerLibraryPostSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        job_list = []
        career_options = request.data['career_options']
        if request.user.id is not None:
            extravert_queryset = CareerLibrary.objects.filter(career_options=career_options,
                                                              job_type=request.data['extravert_job_type'],
                                                              category='extravert').values_list('name', flat=True)
            job_list.append(extravert_queryset)
            adventurous_queryset = CareerLibrary.objects.filter(career_options=career_options,
                                                                job_type=request.data['adventurous_job_type'],
                                                                category='adventurous').values_list('name', flat=True)
            job_list.append(adventurous_queryset)
            agreeable_queryset = CareerLibrary.objects.filter(career_options=career_options,
                                                              job_type=request.data['agreeable_job_type'],
                                                              category='agreeable').values_list('name', flat=True)
            job_list.append(agreeable_queryset)
            neurotic_queryset = CareerLibrary.objects.filter(career_options=career_options,
                                                             job_type=request.data['neurotic_job_type'],
                                                             category='neurotic').values_list('name', flat=True)
            job_list.append(neurotic_queryset)
            conscientious_queryset = CareerLibrary.objects.filter(career_options=career_options,
                                                                  job_type=request.data['conscientious_job_type'],
                                                                  category='conscientious').values_list('name',
                                                                                                        flat=True)
            job_list.append(conscientious_queryset)
            new_list = list(job_list[0]) + list(job_list[1]) + list(job_list[2]) + list(job_list[3]) + list(job_list[4])
            query_data = CareerLibrary.objects.filter(name__in=new_list)
            page = self.paginate_queryset(query_data)
            serializer = CareerLibrarySerializer(page, many=True)
            data = serializer.data
            return self.get_paginated_response(data)
        else:
            queryset = CareerLibrary.objects.filter(career_options=career_options)
            page = self.paginate_queryset(queryset)
            serializer = CareerLibrarySerializer(page, many=True)
            data = serializer.data
            return self.get_paginated_response(data)


class PersonalityTestReport(viewsets.ModelViewSet):
    http_method_names = ('get',)
    queryset = JobMaster.objects.all()
    serializer_class = JobMasterSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = [permissions.AllowAny]

    def list(self, request, *args, **kwargs):
        job_list = []
        personality_test_data = PersonalityTest.objects.filter(created_by=request.user).last()
        PersonalityTest.dashboard_data(personality_test_data)
        ctx = PersonalityTest.status_type(personality_test_data)
        extravert_queryset = JobMaster.objects.filter(job_category=ctx['extravert_status'],
                                                      category='extravert').values_list('title', flat=True)
        job_list.append(extravert_queryset)
        adventurous_queryset = JobMaster.objects.filter(job_category=ctx['adventurous_status'],
                                                        category='adventurous').values_list('title', flat=True)
        job_list.append(adventurous_queryset)
        agreeable_queryset = JobMaster.objects.filter(job_category=ctx['agreeable_status'],
                                                      category='agreeable').values_list('title', flat=True)
        job_list.append(agreeable_queryset)
        neurotic_queryset = JobMaster.objects.filter(job_category=ctx['neurotic_status'],
                                                     category='neurotic').values_list('title', flat=True)
        job_list.append(neurotic_queryset)
        conscientious_queryset = JobMaster.objects.filter(job_category=ctx['conscientious_status'],
                                                          category='conscientious').values_list('title', flat=True)
        job_list.append(conscientious_queryset)
        new_list = list(job_list[0]) + list(job_list[1]) + list(job_list[2]) + list(job_list[3]) + list(job_list[4])
        query_data = JobMaster.objects.filter(title__in=new_list)
        page = self.paginate_queryset(query_data)
        serializer = JobMasterSerializer(page, many=True)
        data = serializer.data
        return self.get_paginated_response(data)


class ExploreCareersViewSet(viewsets.ModelViewSet):
    http_method_names = ('get',)
    queryset = JobMaster.objects.all()
    serializer_class = JobMasterSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = [permissions.AllowAny]

    def list(self, request, *args, **kwargs):
        career_list = []
        category_list = ['Artistic', 'Realistic', 'Social', 'Conventional', 'Enterprising', 'Investigative']
        score_data = UserScores.objects.filter(created_by=request.user).last()
        for category in category_list:
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
            answer_str = InterestAnswerData.objects.filter(created_by=request.user, exam_status='Complete')
            header = {
                "Accept": "application/json",
                "Authorization": "Basic " + Onet_Token,
            }
            get_end = requests.get(
                f"https://services.onetcenter.org/ws/mnm/interestprofiler/careers?area={category}&score={score}"
                f"&answers={answer_str.last().answer}", headers=header)
            end_data = json.loads(get_end.text)
            end = end_data['total']
            result = requests.get(
                f"https://services.onetcenter.org/ws/mnm/interestprofiler/careers?area={category}&score={score}&start=1&end={end}"
                f"&answers={answer_str.last().answer}", headers=header)

            data = json.loads(result.text)['career']
            career_list.append([x['title'] for x in data])

        career_list_final = reduce(lambda x, y: x + y, career_list)
        # favorite job filter
        interest_fav = FavoriteCareer.objects.filter(created_by=request.user).values_list('name', flat=True)
        fav_list = []
        fav_job_query = None
        if interest_fav:
            final_query = []
            interest_fav = list(set(interest_fav))
            for item in interest_fav:
                item = item.replace('&', 'and')
                fav_list.append(item)
                fav_job_query = JobMaster.objects.filter(title=item)
                if fav_job_query:
                    final_query.append(fav_job_query.last())
            if final_query:
                fav_job_query = final_query

        fav_serializer = JobMasterSerializer(fav_job_query, context={'user': self.request.user}, many=True)

        # suggest job filter
        query_data = JobMaster.objects.filter(title__in=career_list_final)

        page = self.paginate_queryset(query_data)
        serializer = JobMasterSerializer(page, context={'user': self.request.user}, many=True)
        if fav_job_query:
            data = fav_serializer.data + serializer.data
        else:
            data = serializer.data
        return self.get_paginated_response(data)


class SelectCareerViewSet(viewsets.ModelViewSet):
    queryset = SelectCareer.objects.all()
    serializer_class = SelectCareerSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = [permissions.IsAuthenticated]
    keys_ref = {
        "achievement": 1,
        "working_conditions": 2,
        "recognition": 3,
        "relationships": 4,
        "support": 5,
        "independence": 6,
    }

    values_ref = {
        "1": "achievement",
        "2": "working_conditions",
        "3": "recognition",
        "4": "relationships",
        "5": "support",
        "6": "independence",
    }

    def list(self, request, *args, **kwargs):
        queryset = self.queryset.filter(created_by=self.request.user)
        queryset = self.paginate_queryset(queryset)
        result_work_test = value_calculation(request.user)
        ctx = {
            'keys_ref': self.keys_ref,
            'values_ref': self.values_ref,
            'result_work_test': result_work_test,
            'user': request.user
        }
        serializer = SelectCareerDetailSerializer(queryset, many=True, context=ctx)
        return self.get_paginated_response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, updated_by=self.request.user)


class DeleteSelectCareer(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        query = SelectCareer.objects.filter(name=request.data['name'], created_by=self.request.user).delete()
        return Response({'message': 'Deleted'}, status=status.HTTP_204_NO_CONTENT)


def split_string(string):
    # Split the string based on space delimiter
    list_string = map(''.join, zip(*[iter(string)] * 5))

    return list_string


def join_string(list_string):
    # Join the string based on '-' delimiter
    string = '-'.join(list_string)

    return string


class GenerateLink(views.APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        career = SelectCareer.objects.filter(created_by__id=request.user.id)
        get_token = Token.objects.get(user=request.user).key
        list_string = split_string(get_token)
        new_string = join_string(list_string)
        url = Frontend_url + '/' + new_string
        return Response({'url': url})

    def post(self, request):
        email_list = request.data['mail']
        mail = email_list.strip('][').split(', ')
        ls = []
        for item in mail:
            ls.append(item.strip('""'))

        try:
            subject = request.data.get('subject', 'Career Studio')
            message = request.data.get('message', '')

            res = send_mail(
                subject,
                message,
                EMAIL_FROM,
                ls,
                fail_silently=False,
            )
        except Exception as e:
            print(e)
        return Response({'message': 'mail sent'})


class ShareVote(views.APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        token = request.data['shared_token']
        shared_token = token.replace('-', '')
        get_user = Token.objects.get(key=shared_token).user.id
        career = SelectCareer.objects.filter(created_by__id=get_user)
        serializer = SelectCareerSerializer(career, many=True)
        return Response(serializer.data)


class VotingView(views.APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        get_data = SelectCareer.objects.get(id=request.data['career_id'])
        vote = int(get_data.votes)
        update_vote = vote + 1
        check_vote = CareerVotes.objects.filter(guest_token=request.data['guest_token'],
                                                career__id=request.data['career_id'])
        if check_vote:
            return Response({'message': 'Already Voted'}, status=status.HTTP_200_OK)
        else:
            update_vote = SelectCareer.objects.filter(id=get_data.id).update(votes=update_vote)
            CareerVotes.objects.create(guest_token=request.data['guest_token'], career=get_data)
            return Response({'message': 'Vote Done'}, status=status.HTTP_200_OK)


class PersonalityReportViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = RecommendationNot.objects.all()
    serializer_class = RecommendationNotSerializer

    def get_queryset(self):
        queryset = self.queryset.filter(created_by=self.request.user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, updated_by=self.request.user)


class AddRecommendateList(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        query = RecommendationNot.objects.filter(created_by=request.user)
        serializer = RecommendationNotSerializer(query, many=True)
        return Response(serializer.data)


class AddRecommendate(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, title):
        query = RecommendationNot.objects.filter(title=title, created_by=request.user)
        serializer = RecommendationNotSerializer(query, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RecommendationNotSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data)
        return Response(serializer.errors)


class DeleteRecommendate(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        favorite = RecommendationNot.objects.filter(title=request.data['title'], created_by=request.user).delete()
        return Response({'message': 'Marked not Recommendate', 'status': True}, status=status.HTTP_200_OK)


class CareerDetail(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        query = CareerLibraryDetail.objects.filter(title=request.data['title']).last()
        serializer = CareerLibraryDetailSerializer(query)
        return Response(serializer.data)


class CareerDetailViewSet(viewsets.ModelViewSet):
    queryset = CareerLibraryDetail.objects.all()
    serializer_class = CareerLibraryDetailSerializer
    permission_classes = [permissions.AllowAny]


class SoftSkillViewSet(viewsets.ModelViewSet):
    queryset = SoftSkills.objects.all()
    serializer_class = SoftSkillSerializer
    permission_classes = [permissions.AllowAny]


class HardSkillViewSet(viewsets.ModelViewSet):
    queryset = HardSkills.objects.all()
    serializer_class = HardSkillSerializer
    permission_classes = [permissions.AllowAny]


class WorkValueItemViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = WorkValueItems.objects.all()
    serializer_class = WorkValuesItemSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = None


class UserWorkValuesView(viewsets.ModelViewSet):
    queryset = UserWorkValues.objects.all()
    serializer_class = UserWorkValuesSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['created_by', 'category']
    pagination_class = None

    def create(self, request, *args, **kwargs):
        payload = request.data.copy()
        json_most = json.loads(payload['most'])
        json_more = json.loads(payload['more'])
        json_somewhat = json.loads(payload['somewhat'])
        json_less = json.loads(payload['less'])
        json_least = json.loads(payload['least'])

        old_values = self.queryset.filter(created_by=request.user).delete()

        # most category serializer
        for item in json_most:
            data = {
                "created_by": request.user.id,
                "category": item,
                "score": 5
            }
            serializer = self.serializer_class(data=data)
            if serializer.is_valid():
                serializer.save()

        # more category serializer
        for item in json_more:
            data = {
                "created_by": request.user.id,
                "category": item,
                "score": 4
            }
            serializer = self.serializer_class(data=data)
            if serializer.is_valid():
                serializer.save()

        # somewhat category serializer
        for item in json_somewhat:
            data = {
                "created_by": request.user.id,
                "category": item,
                "score": 3
            }
            serializer = self.serializer_class(data=data)
            if serializer.is_valid():
                serializer.save()

        # less category serializer
        for item in json_less:
            data = {
                "created_by": request.user.id,
                "category": item,
                "score": 2
            }
            serializer = self.serializer_class(data=data)
            if serializer.is_valid():
                serializer.save()

        # less category serializer
        for item in json_least:
            data = {
                "created_by": request.user.id,
                "category": item,
                "score": 1
            }
            serializer = self.serializer_class(data=data)
            if serializer.is_valid():
                serializer.save()

        res = value_calculation(request.user.id)
        return Response(res)


class UserWorkValuesCalculationView(viewsets.ModelViewSet):
    queryset = UserWorkValues.objects.all()
    serializer_class = UserWorkValuesSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = None

    def list(self, request, *args, **kwargs):
        old_values = self.queryset.filter(created_by=request.user)
        res = value_calculation(request.user.id)
        if old_values:
            res['status'] = True
        else:
            res['status'] = False
        return Response(res)


class ValuesResultView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = None
    queryset = CareerValues.objects.all()
    serializer_class = CareerValuesSerializer
    keys_ref = {
        "achievement": 1,
        "working_conditions": 2,
        "recognition": 3,
        "relationships": 4,
        "support": 5,
        "independence": 6,
    }

    values_ref = {
        "1": "achievement",
        "2": "working_conditions",
        "3": "recognition",
        "4": "relationships",
        "5": "support",
        "6": "independence",
    }

    def create(self, request, *args, **kwargs):
        payload = request.data.copy()
        career_list = payload['career_list'].strip('][').split(', ')
        result_work_test = value_calculation(request.user)
        result = []

        for item in career_list:
            query = self.queryset.filter(title=item[1:-1])
            if query:
                res = career_values(query, self.values_ref, self.keys_ref, result_work_test)
                ctx = {
                    'career_name': item,
                    'result': res
                }
                result.append(ctx)
        return Response(result)


class MajorSetPagination(PageNumberPagination):
    page_size = 16
    page_size_query_param = 'page_size'
    max_page_size = 1000


class MajorView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Major.objects.all()
    serializer_class = MajorSerializer
    pagination_class = MajorSetPagination

    def list(self, request, *args, **kwargs):
        query = SelectCareer.objects.filter(created_by=self.request.user)
        major_id = []
        queryset = None
        if query:
            for item in query:
                query_id = self.queryset.filter(typical_careers__icontains=item.name).values_list('id', flat=True)
                major_id.extend(query_id)
                queryset = self.queryset.filter(id__in=major_id)
        else:
            return Response([])

        queryset = self.paginate_queryset(queryset)
        serializer = self.serializer_class(queryset, many=True, context={'user': request.user})
        return self.get_paginated_response(serializer.data)


class MajorSubjectView(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = MajorSubject.objects.all()
    serializer_class = MajorSubjectSerializer
    pagination_class = None
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['major']


class UserMajorView(QuerySetFilterMixin, viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = UserSelectedMajor.objects.all()
    serializer_class = UserMajorSerializer
    pagination_class = None

    def create(self, request, *args, **kwargs):
        payload = request.data.copy()
        payload['created_by'] = request.user.id

        query = self.queryset.filter(created_by=request.user)
        if query:
            query.delete()
            ctx = {'message': 'Major deleted.'}
            return Response(ctx)
        serializer = self.serializer_class(data=payload)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class UserSelectedCareerView(QuerySetFilterMixin, viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = UserSelectedCareer.objects.all()
    serializer_class = UserSelectedCareerSerializer
    pagination_class = None

    def create(self, request, *args, **kwargs):
        payload = request.data.copy()
        payload['created_by'] = request.user.id

        query = self.queryset.filter(created_by=request.user)
        if query:
            # query.update(career=payload['career'], values=payload['values'])
            # serializer = self.serializer_class(query.last())
            # return Response(serializer.data)
            query.delete()
            ctx = {'message': 'Career deleted.'}
            return Response(ctx)
        serializer = self.serializer_class(data=payload)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class GuestMajorLibraryView(views.APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        career_selected = request.data.get('career', None)
        end = int(request.data['end'])
        query = Major.objects.order_by('?')[0:end]
        if career_selected is None:
            serializer = MajorSerializer(query, many=True)
            return Response(serializer.data)
        query_id = Major.objects.filter(typical_careers__icontains=career_selected)
        print(query_id)
        serializer = MajorSerializer(query_id, many=True)
        return Response(serializer.data)


class GuestSchoolLibraryView(views.APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        query = SchoolProfile.objects.filter(location__country_code__icontains=1).order_by('?')[0:6]
        serializer = SchoolProfileSerializer(query, many=True)
        return Response(serializer.data)
