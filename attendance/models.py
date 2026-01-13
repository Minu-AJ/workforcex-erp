from django.db import models
from employees.models import Employee
from django.utils import timezone


class Attendance(models.Model):
    STATUS_CHOICES = [
        ('PRESENT', 'Present'),
        ('ABSENT', 'Absent'),
        ('HALF_DAY', 'Half Day'),
    ]

    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name='attendance_records'
    )

    date = models.DateField(default=timezone.now)

    check_in = models.TimeField(null=True, blank=True)
    check_out = models.TimeField(null=True, blank=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='ABSENT'
    )

    marked_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('employee', 'date')
        ordering = ['-date']

    def __str__(self):
        return f"{self.employee} - {self.date} - {self.status}"
