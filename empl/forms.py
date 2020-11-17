from django import forms
from .models import *
# class DateInput(forms.DateInput):
#     input_type = 'date'

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['vehicle_no','owner','vehicle_class','chassis_no']
        # fields = '__all__'
        # widgets = {
        #     'reg_date': DateInput()
        # }
class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        # fields = ['vehicle_no','owner','model','chassis_no']
        fields = '__all__'

class DieselForm(forms.ModelForm):
    class Meta:
        model = Diesel
        # fields = ['vehicle_no','owner','model','chassis_no']
        fields = '__all__'

class MaintenanceForm(forms.ModelForm):
    class Meta:
        model = Maintenance
        # fields = ['vehicle_no','owner','model','chassis_no']
        fields = '__all__'