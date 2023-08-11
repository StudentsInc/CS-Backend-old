from django.urls import path, include
from rest_framework.routers import DefaultRouter

# local import
from .views import *

router = DefaultRouter()
router.register('survey', SurveyView, basename='survey')
router.register('user_survey', UserSurveyView, basename='user_survey')

urlpatterns = [
    path('', include(router.urls)),
]