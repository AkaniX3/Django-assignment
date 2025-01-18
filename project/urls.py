from django.contrib import admin
from django.urls import path
from accounts.views import UserRegistrationView, UserLoginView, home, ReferralView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('referrals/<str:referral_code>/', ReferralView.as_view(), name='user-referral'),
]