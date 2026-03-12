from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.db.models import Count
from employees.models import Employee
from attendance.models import Attendance
from leaves.models import Leave
from payroll.models import Payroll
from datetime import timedelta

@login_required
def dashboard(request):
    today = timezone.now().date()

    total_employees = Employee.objects.count()
    today_attendance = Attendance.objects.filter(date=today).count()
    present_today = Attendance.objects.filter(date=today, status='PRESENT').count()
    absent_today = Attendance.objects.filter(date=today, status='ABSENT').count()
    half_day_today = Attendance.objects.filter(date=today, status='HALF_DAY').count()
    pending_leaves = Leave.objects.filter(status='PENDING').count()
    total_payroll = Payroll.objects.count()

    # ✅ 7-Day Attendance Trend
    last_7_days = []
    present_counts = []

    for i in range(6, -1, -1):
        day = today - timedelta(days=i)
        count = Attendance.objects.filter(date=day, status='PRESENT').count()
        last_7_days.append(day.strftime("%b %d"))
        present_counts.append(count)

    context = {
        'total_employees': total_employees,
        'today_attendance': today_attendance,
        'present_today': present_today,
        'absent_today': absent_today,
        'half_day_today': half_day_today,
        'pending_leaves': pending_leaves,
        'total_payroll': total_payroll,

        # Chart Data
        'last_7_days': last_7_days,
        'present_counts': present_counts,
    }

    return render(request, 'dashboard.html', context)

