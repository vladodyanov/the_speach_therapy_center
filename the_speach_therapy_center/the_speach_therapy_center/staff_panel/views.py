from datetime import datetime
import calendar
from django.shortcuts import render, get_object_or_404

from the_speach_therapy_center.accounts.models import Profile
from the_speach_therapy_center.services.models import Appointment


def patient_records(request):
    patients = Profile.objects.all().order_by('user__date_joined')
    context = {
        'patients': patients,
    }
    return render(request, template_name='staff_panel/patients_records.html', context=context)


def patient_details(request, pk):
    patient = get_object_or_404(Profile, pk=pk)
    context = {
        'patient': patient,
    }
    return render(request, 'staff_panel/patient_details.html', context=context)


def patient_appointments(request):
    user = request.user
    appointments = Appointment.objects.all().order_by('day', 'time')
    today = datetime.today()
    month = today.month
    day = today.day

    context = {
        'user': user,
        'appointments': appointments,
        'month': month,
        'day': day,
    }

    return render(request, 'staff_panel/patients_appointments.html', context=context)

