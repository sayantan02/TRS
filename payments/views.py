from django.shortcuts import render, get_object_or_404
import razorpay
from django.conf import settings

from students.models import *
from .models import Payment, ScoutPayment

# Create your views here.

def initiate(request,student_id, scout_pay_id, title, description):
    client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID,settings.RAZORPAY_SECRET_KEY))
    pay_data = get_object_or_404(ScoutPayment, id=scout_pay_id)

    total = pay_data.admission_fees+ pay_data.belt_fees+ pay_data.cap_fees+pay_data.ccrup_fees+ pay_data.food_and_lodging_fees+ pay_data.membership_fees+pay_data.shoes_fees+ pay_data.training_fees+ pay_data.uniform_fees

    payment = client.order.create({'amount':total*100, 'currency':'INR', 'payment_capture': 1})
    
    # payment_labels = {'payment_labels':[{'name': "Admission Fees"},{'fees':pay_data.admission_fees}]}

    context = {
        'payment':payment,
        'title':title,
        'description':description,
        'fees':total,
        'pay_data':pay_data,
    }

    student = get_object_or_404(Student, id=student_id)
    regdNumber = RegistrationNumber.objects.filter(student=student).last()
    
    payment_user = Payment.objects.create(student=regdNumber.student, sub_payment_id = scout_pay_id, payment_amount = total, order_id = payment['id'])
    payment_user.save()
    
    return render(request, "payments/initiate.html", context)

def paymentSuccessful(request,order_id,payment_id,payment_signature):
    payment_user = Payment.objects.filter(order_id=order_id).last()
    payment_user.payment_id = payment_id
    payment_user.payment_signature = payment_signature
    payment_user.is_paid = True
    payment_user.save()
    context = {
        'payment_id':payment_id,
        'payment_signature':payment_signature,
    }
    return render(request, "payments/payment-success.html",context)

def Incomming(request):
    payments = Payment.objects.all()
    return render(request, "payments/income.html",{'payments':payments})

def receipt(request,payment_id,payment_signature):
    payment_user = Payment.objects.filter(payment_id=payment_id,payment_signature=payment_signature).last()
    sub_payment = get_object_or_404(ScoutPayment, id=payment_user.sub_payment_id)
    context = {
        'payment':payment_user,
        'sub_payment':sub_payment,
    }
    return render(request, "invoice/receipt.html",context)


