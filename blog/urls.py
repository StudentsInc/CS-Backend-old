from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('all', BlogAPIView)
router.register('latest-blogs', Latest_n_NumbersOfBlogAPIVIew)
router.register('user-blogs', RetriveBlogsBasedOnUserAPIView)

urlpatterns = [
    path('', include(router.urls))
]

