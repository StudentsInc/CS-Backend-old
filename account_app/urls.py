from django.urls import path, include
from account_app.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('counsellor_appointment', CounsellorAppointmentView, basename='counsellor_appointment')
router.register('guest_token', GuestTokenViewSet, basename='guest_token')

urlpatterns = [
    path('', include(router.urls)),
    path('register', RegistrationAPI.as_view()),
    path('login', UserLoginAPI.as_view()),
    path('password/change', PasswordChangeAPI.as_view()),
    path('otp', OTPView.as_view()),
    path('reset/password', PasswordResetView.as_view()),
    path('guest_user_update', GuestUserUpdate.as_view()),
]
