from django.urls import path
from . import views

urlpatterns = [
    path('apply/', views.apply_leave, name='apply_leave'),
    path('manage/', views.manage_leaves, name='manage_leaves'),
    
    path('approve/<int:leave_id>/', views.approve_leave, name='approve_leave'),
    path('reject/<int:leave_id>/', views.reject_leave, name='reject_leave'),
    path('my/', views.my_leaves, name='my_leaves'),
    
]
