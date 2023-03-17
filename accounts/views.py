from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
from django.shortcuts import render
import random,math, requests
from .models import OTPValidation
from django.contrib import messages
from django.contrib.auth import authenticate, login as user_login, logout

def login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            phone = request.POST['phone-number']
            if User.objects.filter(username=phone).exists():
                digits = "0123456789"
                OTP = ""
                # length of password can be changed
                # by changing value in range
                for i in range(4) :
                    OTP += digits[math.floor(random.random() * 10)]
                
                url = "https://www.fast2sms.com/dev/bulkV2"

                payload = f"variables_values={OTP}&route=otp&numbers={phone}"
                headers = {
                    'authorization': "lvDXT574anOZmkfYeK023M6hc8gqEStbNHBpyPrCwUjIsALd19Jge5ZsdfEwyPxBvrmYOp7KVNjD89Lo",
                    'Content-Type': "application/x-www-form-urlencoded",
                    'Cache-Control': "no-cache",
                    }

                requests.request("POST", url, data=payload, headers=headers)
                OTPValidation.objects.create(user=User.objects.filter(username=phone).last(),number=phone,otp=OTP).save()
                return HttpResponseRedirect(f"/accounts/otp/{phone}")
        else:
            return render(request,"main_app/login.html")
    return HttpResponseRedirect("/accounts/dashboard")

def otp(request,number):
    if not request.user.is_authenticated:
        if request.method == "POST":
            otp = request.POST['otp']
            user = User.objects.filter(username=number).last()
            otp_object = OTPValidation.objects.filter(user=user).last()
            if user:
                if otp_object.otp == otp:
                    user_login(request,otp_object.user)
                    return HttpResponseRedirect("/accounts/dashboard")
                messages.error(request,"OTP Dosen't match!")
            messages.error(request, "No User Exists with this Username")
            otp_object.delete()
        return render(request, "main_app/validate_otp.html",{'number':number})
    return HttpResponseRedirect("/accounts/dashboard")

def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/accounts/login")

def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'hod_template/home_content.html')
    return HttpResponseRedirect("/accounts/login")