from django.urls import path, include
from .import views


urlpatterns = [
    path('initiate/<str:student_id>/<int:scout_pay_id>/<str:title>/<str:description>/',views.initiate),
    path('payment-success/<str:order_id>/<str:payment_id>/<str:payment_signature>/',views.paymentSuccessful),
    path('income/',views.Incomming),
    path('receipt/<str:payment_id>/<str:payment_signature>/',views.receipt),
]