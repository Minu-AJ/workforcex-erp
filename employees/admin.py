# employees/admin.py
from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'department', 'designation', 'joining_date', 'is_active')
    search_fields = ('employee_id', 'department')
    

