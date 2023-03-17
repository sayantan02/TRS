from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class OTPValidation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    number = models.CharField(max_length=15)
    otp = models.CharField(max_length=10)