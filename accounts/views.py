from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse, Http404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.shortcuts import render
from .models import UserProfile
from .serializers import UserProfileSerializer
import random
import string
import logging

logger = logging.getLogger(__name__)

def generate_referral_code(length=6):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

class UserRegistrationView(APIView):
    def post(self, request):
        logger.info("Incoming request for registration: %s", request.data)
        try:
            email = request.data.get('email')
            password = request.data.get('password')
            if not email or not password:
                return Response(
                    {'detail': 'Email and password are required.'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            referral_code = request.data.get('referral_code', None)
            referrer = None
            if referral_code:
                try:
                    referrer = UserProfile.objects.get(referral_code=referral_code)
                except UserProfile.DoesNotExist:
                    return Response({'detail': 'Invalid referral code.'}, status=status.HTTP_400_BAD_REQUEST)

            user = User.objects.create_user(
                username=email,
                email=email,
                password=password
            )
            serializer = UserProfileSerializer(data=request.data)
            if serializer.is_valid():
                generated_code = generate_referral_code()
                serializer.save(user=user, referral_code=generated_code, referred_by=referrer)

                logger.info("User registered successfully: %s", email)
                return Response(
                    {'message': 'User registered successfully!', 'referral_code': generated_code},
                    status=status.HTTP_201_CREATED
                )
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            logger.error(f"Error during registration: {e}", exc_info=True)
            return Response({'detail': 'Internal server error.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UserLoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            return Response({'detail': 'Email and password are required.'}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=email, password=password)
        if user is not None:
            user_profile = UserProfile.objects.get(user=user)
            logger.info("User logged in successfully: %s", email)
            return Response({
                'user_id': user_profile.id,
                'email': user_profile.email,
                'referral_code': user_profile.referral_code,
            }, status=status.HTTP_200_OK)

        logger.warning("Failed login attempt for email: %s", email)
        return Response({'detail': 'Invalid email or password.'}, status=status.HTTP_400_BAD_REQUEST)


class ReferralView(APIView):
    def get(self, request, referral_code):
        try:
            referrer = UserProfile.objects.get(referral_code=referral_code)
        except UserProfile.DoesNotExist:
            logger.warning("Invalid referral code accessed: %s", referral_code)
            raise Http404("Referral code not found.")

        referred_users = UserProfile.objects.filter(referred_by=referrer)
        if not referred_users.exists():
            return Response({'message': 'No referred users found.'}, status=status.HTTP_404_NOT_FOUND)

        referred_user_details = [
            {
                'name': user.name,
                'email': user.email,
                'registration_date': user.user.date_joined
            }
            for user in referred_users
        ]

        logger.info("Retrieved referred users for referral code: %s", referral_code)
        return Response(referred_user_details, status=status.HTTP_200_OK)


def home_page(request):
    return render(request, 'home.html')

def register_page(request):
    return render(request, 'register.html')


def login_page(request):
    return render(request, 'login.html')


def referral_page(request):
    return render(request, 'referral.html')
