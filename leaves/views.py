from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from accounts.decorators import hr_admin_required
from employees.models import Employee
from .models import Leave

def apply_leave(request):
    employee = Employee.objects.get(user=request.user)
    
    if request.method == 'POST':
        Leave.objects.create(
            employee=employee,
            leave_type=request.POST['leave_type'],
            start_date=request.POST['start_date'],
            end_date=request.POST['end_date'],
            reason=request.POST['reason']
        )
        return redirect('dashbord')
    return render(request, 'leaves/apply.html')

@login_required
@hr_admin_required
def manage_leaves(request):
    leaves = Leave.objects.all()
    return render(request, 'leaves/manage.html', {'leaves':leaves})

@login_required
@hr_admin_required
def approve_leave(request, leave_id):
    leave = get_object_or_404(Leave, id=leave_id)
    leave.status = 'APPROVED'
    leave.save()
    return redirect('manage_leaves')

@login_required
@hr_admin_required
def reject_leave(request, leave_id):
    leave = get_object_or_404(Leave, id=leave_id)
    leave.status = 'REJECTED'
    leave.save()
    return redirect('manage_leaves')

@login_required
def my_leaves(request):
    employee = Employee.objects.get(user=request.user)
    leaves = Leave.objects.filter(employee=employee)
    return render(request, 'leaves/my_leaves.html', {'leaves': leaves})


