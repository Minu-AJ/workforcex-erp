from django.db import models
from employees.models import Employee

class Leave(models.Model):
    LEAVE_TYPE_CHOICE = [
        ('CASUAL', 'Casual Leave'),
        ('SICK', 'Sick Leave'),
        ('ANNUAL', 'Annual Leave'),
    ]
    
    STATUS_CHOICE = [
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
    ]
    
    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name='leaves'
    )
    leave_type = models.CharField(
        max_length=20,
        choices=LEAVE_TYPE_CHOICE
    )
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICE,
        default='PENDING'
    )
    applied_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.employee} - {self.leave_type} ({self.status})"
    