from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('career_library', CareerLibraryView, basename='career_library')
router.register('career_library_user', CareerLibraryUserView, basename='career_library_user')
router.register('career_library_list', CareerLibraryListView, basename='career_library_list')
router.register('personality_report', PersonalityTestReport, basename='personality_report')
router.register('explore_careers', ExploreCareersViewSet, basename='explore_careers')
router.register('select_career', SelectCareerViewSet, basename='select_career')
router.register('career_detail_add', CareerDetailViewSet, basename='career_detail_add')
router.register('soft_skill', SoftSkillViewSet, basename='soft_skill')
router.register('hard_skill', HardSkillViewSet, basename='hard_skill')
router.register('work_value_item', WorkValueItemViewSet, basename='work_value_item')
router.register('user/work-value', UserWorkValuesView, basename='work-value-user')
router.register('user/work-value-calculation', UserWorkValuesCalculationView, basename='work-value-calculation')
router.register('career-values/result', ValuesResultView, basename='career-values-result')
router.register('career/major', MajorView, basename='major-list')
router.register('user-selected-major', UserMajorView, basename='user-major-list')
router.register('user-selected-career', UserSelectedCareerView, basename='user-career-list')
router.register('major-subject', MajorSubjectView, basename='major-subject-list')

urlpatterns = [
    path('', include(router.urls)),
    path('faqs', FAQListView.as_view()),
    path('about-us', LatestAboutUsView.as_view()),
    path('privacy-policy', LatestPrivacyPolicyView.as_view()),
    path('terms-and-condition', LatestTermsAndConditionView.as_view()),
    path('about-us-page', AboutUsPageView.as_view()),
    path('privacy-policy-page', PrivacyPolicyPageView.as_view()),
    path('terms-and-condition-page', TermsAndConditionPageView.as_view()),
    path('delete_career', DeleteSelectCareer.as_view()),
    path('share_vote_detail', ShareVote.as_view()),
    path('vote', VotingView.as_view()),
    path('generate_link', GenerateLink.as_view()),
    path('not_recommendate_career', AddRecommendate.as_view()),
    path('delete_not_recommendate_career', DeleteRecommendate.as_view()),
    path('not_recommendate_career_list', AddRecommendateList.as_view()),
    path('not_recommendate_career/<str:name>', AddRecommendate.as_view()),
    path('career_detail', CareerDetail.as_view()),
    path('guest/major_library', GuestMajorLibraryView.as_view()),
    path('guest/school_library', GuestSchoolLibraryView.as_view())
]
