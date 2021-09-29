from .models import Hospital, MainDoctor, Nurses, Doctor, Patients
from django import forms


class AddPatient(forms.ModelForm):
    class Meta:
        model = Patients
        fields = '__all__'

class AddMainDoctor (forms.ModelForm):
    class Meta:
        model = MainDoctor
        fields = '__all__'

class AddNurse (forms.ModelForm):
    class Meta:
        model = Nurses
        fields = '__all__'   

class AddDoctor (forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'