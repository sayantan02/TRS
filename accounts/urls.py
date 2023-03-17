from django.urls import path
from .import views

urlpatterns = [
    path('login/',views.login),
    path('otp/<str:number>/',views.otp),
    path('dashboard/',views.dashboard),
    path('logout/',views.user_logout),
]