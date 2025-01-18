from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import UserProfile
from .serializers import UserProfileSerializer
import random
import string
from django.http import HttpResponse, Http404
from django.contrib.auth.models import User 

def home(request):
    return HttpResponse("Hello world")

class UserRegistrationView(APIView):
    def post(self, request):
        referral_code = request.data.get('referral_code', None)
        if referral_code:
            try:
                referrer = UserProfile.objects.get(referral_code=referral_code)
            except UserProfile.DoesNotExist:
                return Response({'detail': 'Invalid referral code.'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            referrer = None

        user = User.objects.create_user(
            username=request.data.get('email'),
            email=request.data.get('email'),
            password=request.data.get('password')
        )

        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            referral_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
            user_profile = serializer.save(user=user, referral_code=referral_code, referred_by=referrer)

            return Response({'message': 'User registered successfully!', 'referral_code': referral_code}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            user = UserProfile.objects.get(email=email)
        except UserProfile.DoesNotExist:
            return Response({'detail': 'Invalid email or password.'}, status=status.HTTP_400_BAD_REQUEST)

        if user.password == password:
            return Response({
                'user_id': user.id,
                'email': user.email
            }, status=status.HTTP_200_OK)

        return Response({'detail': 'Invalid email or password.'}, status=status.HTTP_400_BAD_REQUEST)

class ReferralView(APIView):
    def get(self, request, referral_code):
        try:
            referrer = UserProfile.objects.get(referral_code=referral_code)
        except UserProfile.DoesNotExist:
            raise Http404("Referral code not found.")

        referred_users = UserProfile.objects.filter(referred_by=referrer)

        if not referred_users:
            return Response({'message': 'No referred users found.'}, status=status.HTTP_404_NOT_FOUND)

        referred_user_details = []
        for user in referred_users:
            referred_user_details.append({
                'name': user.name,
                'email': user.email,
                'registration_date': user.user.date_joined
            })

        return Response(referred_user_details, status=status.HTTP_200_OK)
