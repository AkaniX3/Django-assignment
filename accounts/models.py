from django.db import models

class UserProfile(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    referral_code = models.CharField(max_length=10, blank=True, null=True)
    password = models.CharField(max_length=100)