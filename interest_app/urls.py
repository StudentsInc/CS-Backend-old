from django.urls import path, include
from rest_framework.routers import DefaultRouter

# local import
from interest_app.views import *

router = DefaultRouter()
router.register('question', InterestQuestionView)
router.register('answer/submission', AnswerSubmissionView)

urlpatterns = [
    path('', include(router.urls)),
    path('interest-detail', InterestDetailView.as_view()),
    path('time/start', TestTimeView.as_view()),
    path('exam/end', EndExamView.as_view()),
    path('interest_report', InterestReportView.as_view()),
    path('v2/question', GetQuestion.as_view()),
    path('v2/interest-detail', InterestAnswerDetailView.as_view()),
    path('v2/answer/submission', SubmitInterestQuestion.as_view()),
    path('v2/exam/end', InterestTestEndExam.as_view()),
    path('v2/career_library', CareerLibraryList.as_view()),
    path('v2/favorite_career', AddFavorite.as_view()),
    path('v2/delete_favourite', DeleteFavourite.as_view()),
    path('v2/favorite_career_list', AddFavoriteList.as_view()),
    path('v2/favorite_career/<str:name>', AddFavorite.as_view()),
    path('v2/interest_report', InterestTestReportView.as_view()),
    path('v2/guest/career_library', GuestCareerLibraryList.as_view())
]
#