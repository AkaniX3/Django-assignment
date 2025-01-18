from django.contrib import admin
from django.urls import path
from accounts.views import (
    UserRegistrationView, 
    UserLoginView, 
    ReferralView,
    home_page,
    register_page,
    login_page,
    referral_page,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='home_page'),

    # Frontend
    path('register/', register_page, name='register_page'),
    path('login/', login_page, name='login_page'),
    path('referral/', referral_page, name='referral_page'),

    # Endpoints
    path('api/register/', UserRegistrationView.as_view(), name='user-registration'),
    path('api/login/', UserLoginView.as_view(), name='user-login'),
    path('api/referrals/<str:referral_code>/', ReferralView.as_view(), name='user-referral'),
]
