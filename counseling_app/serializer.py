from rest_framework import serializers
from counseling_app.models import *


class CounselingHeadlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = CounselingHeadline
        fields = '__all__'


class SessionTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SessionTime
        fields = '__all__'


class SessionSerializer(serializers.ModelSerializer):
    payment_done = serializers.SerializerMethodField('get_payment')
    session_time = serializers.SerializerMethodField('get_session_time')

    def get_payment(self, inst):
        user = self.context.get('user')
        date = self.context.get('date')
        appointment_query = Appointment.objects.filter(appointment_date=date, created_by=user)
        if appointment_query:
            return True
        return False

    def get_session_time(self, inst):
        user = self.context.get('user')
        date = self.context.get('date')
        appointment_query = Appointment.objects.filter(appointment_date=date, created_by=user)
        ctx = []
        for item in inst.session_time.all():
            res = {
                "time": item.time,
                "id": item.id
            }
            if appointment_query and item.time == appointment_query.last().appointment_time:
                res['is_disable'] = True
            else:
                res['is_disable'] = False
            ctx.append(res)
        return ctx

    class Meta:
        model = Session
        fields = '__all__'


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'


class CoachSerializer(serializers.ModelSerializer):
    session = SessionSerializer(many=True)

    class Meta:
        model = Coach
        fields = '__all__'
