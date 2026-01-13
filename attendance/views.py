from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib import messages
from .models import Attendance
from employees.models import Employee


@login_required
def mark_attendance(request):
    employee = Employee.objects.get(user=request.user)
    today = timezone.now().date()
    
    # check if already marked
    attendance, created = Attendance.objects.get_or_create(
        employee=employee,
        date=today,
        defaults={'status': 'PRESENT'}
    )
    
    if request.method == "POST":
        status = request.POST.get("status")
        
        # update status only
        attendance.status = status
        attendance.save()
        
        messages.success(request, f"Attendance marked as {status}")
        return redirect('view_attendance')
    
    context = {
        'attendance': attendance,
        'today': today
    }
    return render(request, 'attendance/mark.html', context)
    

@login_required
def view_attendance(request):
    employee = Employee.objects.get(user=request.user)
    records = Attendance.objects.filter(employee=employee)        
    return render(request, 'attendance/list.html', {'records': records})


@login_required
@hr_admin_required
