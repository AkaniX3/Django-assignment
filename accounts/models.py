from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    referral_code = models.CharField(max_length=10, blank=True, null=True)
    password = models.CharField(max_length=100)
    referred_by = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='referees')

    def __str__(self):
        return self.email
