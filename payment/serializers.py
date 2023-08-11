from rest_framework import serializers
from payment.models import *


class StripeAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = StripeAccount
        fields = '__all__'


class PaymentHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentHistory
        fields = '__all__'


class CreatePaymentSerializer(serializers.Serializer):
    amount = serializers.CharField(max_length=100, required=True)
    expiry = serializers.CharField(max_length=100, required=True)
    card_number = serializers.CharField(max_length=100, required=True)
    cvc = serializers.CharField(max_length=100, required=True)
