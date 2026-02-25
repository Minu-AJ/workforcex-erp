from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from employees.models import Employee
from attendance.models import Attendance
from leaves.models import Leave
from payroll.models import Payroll


@login_required
def dashboard(request):
    today = timezone.now().date()
    
    total_employees = Employee.objects.count()
    present_today = Attendance.objects.filter(date=today, status='Present').count()
    absent_today = Attendance.objects.filter(date=today, status='Absent').count()
    pending_leaves = Leave.objects.filter(status='Pending').count()
    total_payroll = Payroll.objects.count()
    
    context = {
        'total_employees': total_employees,
        'present_today': present_today,
        'absent_today': absent_today,
        'pending_leaves': pending_leaves,
        'total_payroll': total_payroll,
    }
    
    return render(request, 'dashboard.html', context)

