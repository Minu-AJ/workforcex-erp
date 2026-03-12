from django.urls import path
from .import views


urlpatterns = [
    path('', views.payroll_list, name='payroll_list'),
    path('add/', views.add_payroll, name='add_payroll'),
    path('payslip/<int:id>/', views.generate_payslip, name='generate_payslip'),
]
