from django.urls import path
from . import views

urlpatterns = [
    path('',views.login),
    path('registrasi',views.regis),
    path('dashboard',views.dash)
]