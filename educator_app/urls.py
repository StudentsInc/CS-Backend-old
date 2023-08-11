from django.urls import path
from educator_app.views import *

urlpatterns = [
    path('', EducatorView.as_view()),
    path('high-school', HighSchoolView.as_view()),
    path('post-secondary', PostSecondaryView.as_view()),
]
