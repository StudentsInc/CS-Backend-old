from rest_framework import serializers, exceptions
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.utils import timezone
from account_app.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'first_name')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        token = self.get_token(user)
        ctx = {
            'user': user.pk,
            'token': token
        }
        return ctx

    def get_token(self, obj):
        token = Token.objects.create(user=obj)
        return token.key


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=35)
    password = serializers.CharField(style={'input_type': 'password'})

    def validate(self, data):
        user = authenticate(
            username=data['username'], password=data['password'])
        if not user:
            raise exceptions.AuthenticationFailed()
        elif not user.is_active:
            raise exceptions.PermissionDenied()

        # Update last login information whenever token is requested
        user.last_login = timezone.now()
        user.save(update_fields=['last_login'])

        data['user'] = user
        return data


class UserLoginReplySerializer(serializers.ModelSerializer):
    user = UserSerializer()

    # free = serializers.SerializerMethodField()

    # connected_contacts_count = serializers.SerializerMethodField()
    # deal_count = serializers.SerializerMethodField()
    # def get_free(self, obj):
    #     admin = User.objects.get(username='admin')
    #     check_paid = CounsellorAppointment.objects.filter(counsellor=admin).count()
    #     if check_paid > 50:
    #         free = False
    #     else:
    #         free = True
    #     return free

    class Meta:
        model = Token
        fields = ('key', 'user')


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class OTPSerializer(serializers.ModelSerializer):
    class Meta:
        model = Otp
        fields = '__all__'


class UserChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class CounsellorAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CounsellorAppointment
        fields = '__all__'


class GuestTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuestUser
        fields = ('token',)


class GuestUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuestUser
        fields = '__all__'
