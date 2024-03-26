from django.shortcuts import render, get_object_or_404

from the_speach_therapy_center.accounts.models import Profile


def patient_records(request):
    patients = Profile.objects.all()
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

