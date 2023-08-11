from django.urls import path, include
from rest_framework.routers import DefaultRouter

from counseling_app.views import *

router = DefaultRouter()
router.register('appointment', AppointmentView)

urlpatterns = [
    path('', include(router.urls)),
    path('session', SessionView.as_view()),
    path('page', CounselingView.as_view()),
    path('paypal/success-payment/', PaypalSuccessView.as_view())
]
