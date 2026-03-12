from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = [
            'user',
            'employee_id',
            'department',
            'designation',
            'joining_date',
            'basic_salary',
            'is_active',
        ]