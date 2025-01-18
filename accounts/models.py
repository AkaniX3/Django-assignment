from django.db import models

class UserProfile(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    referral_code = models.CharField(max_length=10, blank=True, null=True)
    password = models.CharField(max_length=100)
    referred_by = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='referees')

    def __str__(self):
        return self.email
