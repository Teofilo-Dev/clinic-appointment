"""
URL configuration for clinic_backend project.
"""
from django.contrib import admin
from django.urls import path
from clinic_backend import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Auth endpoints
    path('api/doctor/login/', views.doctor_login, name='doctor_login'),
    path('api/admin/login/', views.admin_login, name='admin_login'),
    path('api/receptionist/login/', views.receptionist_login, name='receptionist_login'),

    # Patient (no login required)
    path('api/doctors/', views.list_doctors, name='list_doctors'),
    path('api/appointment/request/', views.request_appointment, name='request_appointment'),
]
