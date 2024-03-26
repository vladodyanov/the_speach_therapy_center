from django.shortcuts import render

from the_speach_therapy_center.accounts.models import Profile


def patient_records(request):
    patients = Profile.objects.all()
    # patients = [user for user in registered_users if not user.is_staff and user.is_superuser]

    context = {
        'patients': patients,
    }
    return render(request, template_name='staff_panel/patients_records.html', context=context)
