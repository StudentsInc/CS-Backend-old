from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('country', CountryAPIView)
router.register('major-setup', MajorSetupAPIView)
router.register('school-profile', SchoolProfileAPIView)
router.register('school-galleries', SchoolGalleryAPIView)
router.register('school-major', SchoolMajorAPIView)
router.register('school-filter', SchoolFilterAPIView)
router.register('user-school', UserSchoolView)

urlpatterns = [
    path('', include(router.urls)),
]
