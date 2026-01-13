from django.urls import path
from . import views

urlpatterns = [
    path('mark/', views.mark_attendance, name='mark_attendance'),
    path('my/', views.view_attendance, name='view_attendance'),
]
