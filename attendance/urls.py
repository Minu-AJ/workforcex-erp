from django.urls import path
from . import views

urlpatterns = [
    path('mark/', views.mark_attendance, name='mark_attendance'),
    path('my/', views.view_attendance, name='view_attendance'),
    path('check-in/', views.check_in, name='check_in'),
    path('check_out/', views.check_out, name='check_out')
]
