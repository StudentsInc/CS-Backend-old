from django.contrib import admin
from payment.models import *


# Register your models here.
@admin.register(StripeAccount)
class StripeAccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'account_id', 'created_by')


@admin.register(PaymentHistory)
class PaymentHistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'amount', 'transaction_id', 'created_by')
