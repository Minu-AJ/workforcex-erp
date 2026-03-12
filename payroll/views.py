from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Payroll
from employees.models import Employee
from reportlab.pdfgen import canvas


@login_required
def payroll_list(request):
    payrolls = Payroll.objects.all()
    return render(request, 'payroll/payroll_list.html', {'payrolls':payrolls})

@login_required
def add_payroll(request):
    
    if request.method == 'POST':
        employee_id = request.POST['employee']
        employee = Employee.objects.get(id=employee_id)
        
        Payroll.objects.create(employee=employee,
                               month = request.POST['month'],
                               basic_salary = request.POST['basic_salary'],
                               allowances = request.POST['allowances'],
                               deductions = request.POST['deductions']
                               )
        return redirect('payroll_list')
    
    employees = Employee.objects.all()
    return render(request, 'payroll/add_payroll.html', {'employees':employees})


#generate payslip

def generate_payslip(request, id):
    
    payroll = Payroll.objects.get(id=id)
    
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="payslip_{payroll.id}.pdf"'
    p = canvas.Canvas(response)
    p.setFont("Helvetica", 14)
    p.drawString(200, 800, "Salary Slip")
    p.setFont("Helvetica", 12)
    p.drawString(100, 750, f"Employee:{payroll.employee}")
    p.drawString(100, 720, f"Month:{payroll.month}")
    p.drawString(100, 690, f"Basic Salary:{payroll.basic_salary}")
    p.drawString(100, 660, f"Allowances:{payroll.allowances}")
    p.drawString(100, 630, f"Deductions:{payroll.deductions}")
    p.drawString(100, 600, f"Net Salary:{payroll.net_salary}")
    
    p.showPage()
    p.save()
    
    return response
    

