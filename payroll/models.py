from django.db import models
from employees.models import Employee
from decimal import Decimal


class Payroll(models.Model):
    employee = models.ForeignKey(
                                    Employee, 
                                    on_delete=models.CASCADE, 
                                    related_name='payrolls'
                                )
    
    month = models.DateField()
    basic_salary = models.DecimalField(max_digits=10, decimal_places=2)
    allowances = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    deductions = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    net_salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        self.net_salary = Decimal(self.basic_salary) + Decimal(self.allowances) - Decimal(self.deductions)
        super().save(*args, **kwargs)
        
    def __str__(self):
        return f"{self.employee} - {self.month}"
    