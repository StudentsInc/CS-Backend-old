from django.urls import path, include
from rest_framework.routers import DefaultRouter

# local import
from learning_style.views import *

router = DefaultRouter()
router.register('question', LearningQuestionView)
router.register('generate/uid', GenerateUIDView)
router.register('answer/submit', AnswerSubmissionView)

urlpatterns = [
    path('', include(router.urls)),
    path('exam/end', EndExamView.as_view())
]
