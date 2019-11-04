from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .forms import EquipmentEntryForm, AssignmentForm, RequestForm
from .models import Equipment, StaffRequest

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = EquipmentEntryForm(request.POST)
        if form.is_valid():
            print("hello there")
            form.save()

    else:
        form = EquipmentEntryForm()

    context = {'form': form}

    return render(request,'equip_entry.html', context)

def assign(request, serial_number):
    if request.method == 'POST':
        form = AssignmentForm(request.POST)
        if form.is_valid():
            staff = request.POST.get('assigned_to')
            dep = request.POST.get('department')
            Equipment.objects.filter(serial_number=serial_number).update(assigned_to=staff, department=dep)

    else:
        form = AssignmentForm()
    context = {'form': form}
    return render(request,'equipment_assignment.html', context)


def order(request):
    if request.method =='POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            s_name = form.cleaned_data['staff_name']
            s_num = form.cleaned_data['staff_number']
            s_department = form.cleaned_data['staff_department']
            s_equipment = form.cleaned_data['r_equipment']

            staff_request = StaffRequest(staff_name = s_name, staff_number = s_num, staff_department = s_department, r_equipment = s_equipment )
            staff_request.save()

        return render(request, 'equipment_assignment.html')
    else:
        form = RequestForm()
        context = {'form': form}
        return render(request, 'equipment_request.html', context)
