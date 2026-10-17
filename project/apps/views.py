from django.shortcuts import render,redirect,get_object_or_404
from .forms import employeeform
from .models import employee

# Create your views here.
def add_employee(request):
    form=employeeform(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('empl')
    return render(request,'add_empl.html',{'form':form})

def emp_details(request):
    search = request.GET.get('search', '')

    if search:
        emp = (
            employee.objects.filter(department__icontains=search) |
            employee.objects.filter(name__icontains=search)
        )
    else:
        emp = employee.objects.all()

    return render(request, 'emplyee_dashboard.html', {'empl': emp})


def edit_employee(request,id):
    employe=get_object_or_404(employee,id=id)
    form=employeeform(request.POST or None,instance=employe)
    if form.is_valid():
        form.save()
        return redirect('empl')
    return render(request,'update_empl.html',{'form':form})

def delete_employee(request,id):
    employe=get_object_or_404(employee,id=id)
    if request.method=="POST":
        employe.delete()
        return redirect('empl')
    return render(request,'remove_empl.html',{'employe':employe})
