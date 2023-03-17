from django.http import HttpResponseRedirect
from django.shortcuts import render
import razorpay
from django .conf import settings
from students.models import *
from datetime import datetime
from qrcode import *
from payments.models import *
from django.contrib import messages
import time

# Create your views here.
def index(request):
    return render(request, "frontend/index.html")


def scout(request):
    if request.method == "POST":
        full_name = request.POST['fullname']
        guardian_name = request.POST['guardian-name']
        address = request.POST['address']
        mobile_number = request.POST['mobile-number']
        whatsapp_number = request.POST['whatsapp-number']
        guardian_number = request.POST['guardian-number']
        pin_code = request.POST['pin-code']
        adhaar_card = request.FILES['adhaar-card']
        upload_picture = request.FILES['picture']

        training_fees = request.POST['training-fees']
        food_and_lodging_fees = request.POST['food-lodging-fees']
        uniform_fees = request.POST['uniform-fees']
        shoes_fees = request.POST['shoes-fees']
        ccrup_fees = request.POST['ccrup-fees']
        cap_fees = request.POST['cap-fees']
        belt_fees = request.POST['belt-fees']
        admission_fees = request.POST['registration-fees']
        membership_fees = request.POST['membership-fees']

        applying_for = "Hindustan Scout and Guides"

        # date_of_birth = request.POST['date-of-birth']
        # city = request.POST['city']
        # queries = request.POST['describe-queries']

        student = Student.objects.create(
            name = full_name,
            mobile_number = mobile_number,
            whatsapp_number = whatsapp_number,
            guardian_name = guardian_name,
            guardian_mobile_number = guardian_number,
            address = address,
            pin_code = pin_code,
            adhaar_card = adhaar_card,
            admission_fees = admission_fees,
            picture = upload_picture,
            applying_for = applying_for,
            training_fees = training_fees,
            food_and_lodging_fees = food_and_lodging_fees,
            uniform_fees = uniform_fees,
            shoes_fees = shoes_fees,
            ccrup_fees = ccrup_fees,
            cap_fees = cap_fees,
            belt_fees = belt_fees,
            membership_fees = membership_fees,
        )
        student.save()

        registrationNumber = "TRS-"+str(student.id)+"-"+datetime.now().strftime('%y')
        img = make(registrationNumber)
        img_name = 'qr' + str(time.time()) + '.png'
        img.save(settings.MEDIA_ROOT + '/qrcodes/' + img_name)
        try:
            RegistrationNumber.objects.create(
                registration_number = registrationNumber,
                student = student,
                qr_code = f"qrcodes/{img_name}"
            ).save()
            
            scout_payment = ScoutPayment.objects.create(
                student = student,
                training_fees = training_fees,
                food_and_lodging_fees = food_and_lodging_fees,
                uniform_fees = uniform_fees,
                shoes_fees = shoes_fees,
                ccrup_fees = ccrup_fees,
                cap_fees = cap_fees,
                belt_fees = belt_fees,
                admission_fees = admission_fees,
                membership_fees = membership_fees
            )
            scout_payment.save()

            return HttpResponseRedirect(f"/payments/initiate/{student.id}/{scout_payment.id}/fees for {applying_for}/Student {full_name} getting admitted to TRS APD for {applying_for} Course.")
        except:
            messages.error(request, "Please Try Again Later")
    return render(request, "frontend/scout.html")

def payment(request):
    return render(request, "frontend/payment.html")











