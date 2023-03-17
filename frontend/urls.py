from django.urls import path, include
from .import views


urlpatterns = [
    path('',views.index),
    path('scouts/',views.scout),
    path('pay-fees/',views.payment),
]