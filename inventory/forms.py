from django import forms
from .models import Equipment, StaffRequest

class EquipmentEntryForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ['type', 'mac_address', 'serial_number','vendor','status']


class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ('assigned_to', 'department')


class RequestForm(forms.ModelForm):
    class Meta:
        model = StaffRequest
        fields = ('staff_name', 'staff_number', 'staff_department', 'r_equipment')
