from django.urls import path,include
from rest_framework.routers import DefaultRouter
from payment.views import *

router = DefaultRouter()
router.register(r'stripe/account/connect', StripeAccountConnect, basename='stripe_account')
router.register(r'stripe/charge/create', StripePaymentCharge, basename='stripe_charge_create')

urlpatterns = [
    path('', include(router.urls))
]
