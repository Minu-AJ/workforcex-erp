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
def check_in(request):
    employee = Employee.objects.get(user=request.user)
    today = timezone.now().date()

    attendance, created = Attendance.objects.get_or_create(
        employee=employee,
        date=today
    )

    if attendance.check_in:
        messages.warning(request, "You have already checked in.")
    else:
        attendance.check_in = timezone.now().time()
        attendance.status = "PRESENT"
        attendance.save()
        messages.success(request, "Checked in successfully.")

    return redirect('mark_attendance')

@login_required
def check_out(request):
    employee = Employee.objects.get(user=request.user)
    today = timezone.now().date()

    attendance = Attendance.objects.filter(
        employee=employee,
        date=today
    ).first()

    if not attendance or not attendance.check_in:
        messages.error(request, "Check-in first.")
        return redirect('mark_attendance')

    if attendance.check_out:
        messages.warning(request, "Already checked out.")
        return redirect('mark_attendance')

    attendance.check_out = timezone.now().time()

    # Calculate work hours
    check_in_dt = timezone.datetime.combine(today, attendance.check_in)
    check_out_dt = timezone.datetime.combine(today, attendance.check_out)
    duration = (check_out_dt - check_in_dt).seconds / 3600
    attendance.work_hours = round(duration, 2)

    attendance.save()
    messages.success(request, "Checked out successfully.")
    return redirect('mark_attendance')

