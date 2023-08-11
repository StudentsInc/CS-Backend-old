from django.urls import path, include
from rest_framework.routers import DefaultRouter

# local import
from personality_test.views import *

router = DefaultRouter()
router.register('reason', ReasonView, basename='reason')
router.register('education_level', EducationLevelView, basename='education_level')
router.register('personality_detail', PersonalityDetailView, basename='personality_detail')
router.register('personality_question', PersonalityQuestionView, basename='personality_question')
router.register('personality_answer_submission', PersonalityAnswerSubmissionView,
                basename='personality_answer_submission')
router.register('personality_end_time', PersonalityEndExamView, basename='personality_end_time')
router.register('user_detail', UserDetailView, basename='user_detail')
router.register('get_report', GetReport, basename='get_report')
router.register('job', UserJobType, basename='job')
router.register('personality_dashboard', PersonalityAssessmentDashboard, basename='personality_dashboard')
router.register('personality_report', PersonalityReportViewSet, basename='personality_report')

urlpatterns = [
    path('', include(router.urls)),
]