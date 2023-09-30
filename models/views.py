from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models.patient import Patient
from .models.phone_number import PhoneNumber
from .models.email import Email
from .models.address import Address


def index(request):
    return render(request, 'dashboard.html')

def patient(request, patient_id):
    patient = get_object_or_404(Patient, pk=patient_id)
    addresses = Address.objects.filter(object_id=patient_id)
    phone_numbers = PhoneNumber.objects.filter(object_id=patient_id)
    emails = Email.objects.filter(object_id=patient_id)
    context = {
        'patient': patient,
        'addresses': addresses,
        'phone_numbers': phone_numbers,
        'emails': emails,
    }
    return render(request, 'patients/patient.html', context)

def patients(request):
    patients = Patient.objects.all()
    context = {
        'patients': patients,
    }
    return HttpResponse(render(request, 'patients/patients.html', context))

def search(request,q):
    """ filter by name and last_name """
    if q:
        patients = Patient.objects.filter(name__icontains=q) | Patient.objects.filter(last_name__icontains=q)
        return HttpResponse(render(request, 'patients/search.html', {'patients': patients}))
    