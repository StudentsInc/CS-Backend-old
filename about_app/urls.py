from django.urls import path
from about_app.views import *

urlpatterns = [
    path('', AboutView.as_view())
]
