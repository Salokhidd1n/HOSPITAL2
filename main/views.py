from .models import Doctor, Hospital, Patients, MainDoctor
from django.shortcuts import render
from django.views.generic import CreateView
from .forms import *

# Create your views here.
def index (request):
    hospitals = Hospital.objects.all()
    return render(request, 'index.html',{'hospitals':hospitals})

  

def detail (request, pk):
    hospital_detail = Hospital.objects.get(pk=pk)
    doctor_detail = Doctor.objects.filter(hospital=pk)
    patients_detail = Patients.objects.filter(doctor=pk)

    context = {
        'hospital_detail':hospital_detail,
        'doctor_detail':doctor_detail,
        'patients_detail':patients_detail
    }
    return render (request, 'detail.html', context)

class AddDoctors(CreateView):
    form_class = AddDoctor
    template_name = 'addnew.html'
    raise_exception  = True

class AddNurses(CreateView):
        form_class = AddNurse
        template_name ='addnew.html'
        raise_exception = True
        
class AddPatients(CreateView):
    form_class = AddPatient
    template_name ='addnew.html'
    raise_exception = True
        