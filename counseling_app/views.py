# third party import
from django.shortcuts import reverse
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from django.views import View
from rest_framework import views, permissions, viewsets
from rest_framework.response import Response
from django.contrib.auth.models import User
# local import
from counseling_app.custom_method import appointment_history
from counseling_app.paypal_view import PayPal
from career_studio.settings import *
from counseling_app.serializer import *
from payment.stripe_view import *


# Create your views here.
class CounselingView(views.APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        headline_context = CounselingHeadline.objects.last()
        coach_context = Coach.objects.last()

        ctx = {
            "counseling": CounselingHeadlineSerializer(headline_context).data,
            "coach": CoachSerializer(coach_context).data
        }
        return Response(ctx)


class SessionView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        date = request.data['date']
        session = request.data['session']

        query = Session.objects.filter(session=session).exclude(unavailable_date=date)
        serializer = SessionSerializer(query.last(), context={'user': request.user, 'date': date})
        return Response(serializer.data)


class AppointmentView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    def get_queryset(self):
        return self.queryset.filter(created_by=self.request.user)

    def create(self, request, *args, **kwargs):
        payload = request.data.copy()
        payload['created_by'] = request.user.id
        payment_method = request.data['payment_method']
        if payment_method == 'stripe':
            expiry, amount, card_number, cvc = payload['expiry'], payload['amount'], payload['card_number'], payload[
                'cvc']
            try:
                res = stripe_charge_create(expiry, amount, card_number, cvc)
                payload['charge_id'] = res
                payload['session_cost'] = amount
                res = appointment_history(payload)
                return Response(res)
            except Exception as e:
                return Response(e)
        else:
            amount = payload['amount']
            payload['payment_method'] = 'paypal'
            payload['session_cost'] = amount
            res = appointment_history(payload)
            appointment_id = res['id']
            try:
                token = PayPal.get_paypal_token(client_id=client_id, client_secret=secret_key)
                protocol = 'https://' if request.is_secure() else 'http://'
                success_url = protocol + get_current_site(request).domain + reverse(
                    'paypal_payment_success') + '?uid=' + str(request.user.id) + '&appointment_id=' + str(
                    appointment_id)
                cancel_url = protocol + get_current_site(request).domain + reverse('paypal_payment_cancel')
                res = PayPal.checkout_order(token.json()['access_token'], appointment_id, success_url, cancel_url,
                                            amount)
                return Response(res)
            except Exception as e:
                return Response(str(e))


class PaypalSuccessView(View):
    def get(self, request, *args, **kwargs):
        appointment_id = request.GET.get('appointment_id')
        uid = request.GET.get('uid')
        pay_id = request.GET.get('PayerID')
        query = Appointment.objects.filter(id=appointment_id).update(charge_id=pay_id)
        user = User.objects.get(id=uid)
        msg = f"Hello {user.first_name} {user.last_name}. your payment had received successfully."
        return HttpResponse(msg)
