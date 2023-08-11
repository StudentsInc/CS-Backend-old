from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework import permissions, status, viewsets
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from account_app.serializer import *
from rest_framework.response import Response

from account_app.user_update import user_update
from career_studio import settings
from cms_app.views import StandardResultsSetPagination
from interest_app.models import *
import random


# Create your views here.


class RegistrationAPI(GenericAPIView):
    serializer_class = CreateUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            payload = request.data.copy()
            payload['created_by'] = user['user']
            payload['updated_by'] = user['user']
            # payload['user_role'] = request.data.get('user_role')
            profile_serializer = ProfileSerializer(data=payload)
            if profile_serializer.is_valid():
                profile_serializer.save()
                return Response(user)
            return Response(profile_serializer.errors)
        return Response(serializer.errors)


class UserLoginAPI(GenericAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Get or Generate token
        token, created = Token.objects.get_or_create(
            user=serializer.validated_data['user'])
        data = {
            'user': serializer.validated_data['user']
        }
        response_serializer = UserLoginReplySerializer(token, context={'request': data})
        if request.data.get('guest_token') is not None:
            token = request.data['guest_token']
            user = serializer.validated_data['user']
            user_update(token=token, user=user)
        else:
            pass
        return Response(response_serializer.data)


class PasswordChangeAPI(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        password = request.data.get("password")
        confirmPassword = request.data.get("confirmPassword")

        if password != confirmPassword:
            return Response({'error': 'Password does not match'},
                            status=500)

        user = User.objects.get(pk=request.user.pk)
        user.set_password(password)
        user.save()
        return Response({'ok': 'Password changed successfully! '},
                        status=200)


class OTPView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        user = User.objects.filter(email=request.data['email']).last()
        if user:
            otp = random.randint(1111, 9999)
            try:
                subject = 'SocialMarketing'
                message = f'Hi {user.username}, Here is OTP from SocialMarketing.\n{otp}'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [user.email, ]
                send_mail(subject, message, email_from, recipient_list)
            except Exception as e:
                print('send email.')
            model_data = request.data.copy()
            model_data['otp'] = otp
            model_data['created_by'] = user.pk
            model_data['updated_by'] = user.pk
            serializer = OTPSerializer(data=model_data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
        return Response({'message': 'There is no user register with this email.'})

    def put(self, request):
        user = User.objects.filter(email=request.data['email']).last()
        if user:
            query_otp = Otp.objects.filter(user=user.id).last()
            if query_otp:
                query_data = {
                    'verify': 'true'
                }
                if int(request.data['otp']) == int(query_otp.otp):
                    query_update = OTPSerializer(query_otp, data=query_data)
                    if query_update.is_valid():
                        query_update.save()
                        return Response({'message': 'you have successfully verify OTP.'}, status=status.HTTP_200_OK)
                    return Response({'message': query_update.errors}, status=status.HTTP_400_BAD_REQUEST)
                return Response({'message': 'OTP that you enter is not valid.', 'status': 400},
                                status=status.HTTP_400_BAD_REQUEST)
            return Response({'message': 'Please send OTP first.'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'There is no user register with this email.'}, status=status.HTTP_400_BAD_REQUEST)


class PasswordResetView(APIView):
    permission_classes = (permissions.AllowAny,)

    def put(self, request):
        user = User.objects.filter(email=request.data['email']).last()
        if user:
            query_otp = Otp.objects.filter(created_by=user.id, verify='true').last()
            if query_otp:
                user.set_password(request.data['password'])
                user.save()
                # remove previous otp
                inst = Otp.objects.filter(created_by=user).delete()
                return Response({'message': 'You have successfully reset your password.'}, status=status.HTTP_200_OK)
            return Response({'message': 'First Verify OTP then reset your password'},
                            status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'There is no user register with this email.'}, status=status.HTTP_400_BAD_REQUEST)


class CounsellorAppointmentView(viewsets.ModelViewSet):
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = CounsellorAppointmentSerializer
    queryset = CounsellorAppointment.objects.all()

    # def list(self, request, *args, **kwargs):
    #     query = self.queryset.filter(student=request.user)
    #     serializer = CounsellorAppointmentSerializer(query, many=True)
    #     return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        counsellor = User.objects.get(username='admin')
        data['counsellor'] = counsellor.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class GuestTokenViewSet(viewsets.ModelViewSet):
    # permission_classes = [permissions.IsAuthenticated]
    http_method_names = ('get', 'post')
    serializer_class = GuestTokenSerializer
    queryset = GuestUser.objects.all()
    pagination_class = StandardResultsSetPagination


class GuestUserUpdate(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        token = request.data['guest_token']
        user = request.user
        query = GuestUser.objects.filter(token=token).update(user=request.user)
        interest_answer = AnswerModel.objects.filter(guest_user__token=token).update(created_by=user, updated_by=user)
        user_interest_test = UserInterestTest.objects.filter(guest_user__token=token).update(created_by=user,
                                                                                             updated_by=user)
        user_score = UserScores.objects.filter(guest_user__token=token).update(created_by=user, updated_by=user)
        return Response({'message': "User Updated"})
