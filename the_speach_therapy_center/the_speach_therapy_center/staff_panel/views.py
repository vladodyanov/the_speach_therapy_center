from datetime import datetime
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic as views

from the_speach_therapy_center.accounts.models import Profile
from the_speach_therapy_center.core.custom_decorators import staff_user_required
from the_speach_therapy_center.core.view_mixins import OwnerRequiredMixin, StaffPermissionMixin
from the_speach_therapy_center.services.models import Appointment
from the_speach_therapy_center.staff_panel.forms import TreatmentPlanCreationForm, TreatmentPlanChangeForm
from the_speach_therapy_center.staff_panel.models import TreatmentPlan


@staff_user_required
def patient_records(request):
    patients = Profile.objects.all().order_by('user__date_joined')
    context = {
        'patients': patients,
    }
    return render(request, template_name='staff_panel/patients_records.html', context=context)


@staff_user_required
def patient_details(request, pk):
    patient = get_object_or_404(Profile, pk=pk)
    context = {
        'patient': patient,
    }
    return render(request, 'staff_panel/patient_details.html', context=context)


@staff_user_required
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


@staff_user_required
def patient_treatment_plans(request):
    user = request.user
    treatment_plans = TreatmentPlan.objects.all()

    context = {
        'user': user,
        'treatment_plans': treatment_plans,
    }

    return render(request, 'staff_panel/treatment_plans.html', context=context)


class CreateTreatmentPlanView(StaffPermissionMixin, views.CreateView):
    model = TreatmentPlan
    form_class = TreatmentPlanCreationForm
    template_name = 'staff_panel/treatment_plan_create.html'
    success_url = reverse_lazy('patient treatment plans')

    def form_valid(self, form):
        form.instance.therapist = self.request.user
        return super().form_valid(form)


class DetailsTreatmentPlanView(StaffPermissionMixin, views.DetailView):
    queryset = TreatmentPlan.objects.all()
    template_name = "staff_panel/treatment_plan_details.html"


class EditTreatmentPlanView(StaffPermissionMixin, views.UpdateView):
    model = TreatmentPlan
    form_class = TreatmentPlanChangeForm
    template_name = 'staff_panel/treatment_plan_edit.html'
    success_url = reverse_lazy('patient treatment plans')


class DeleteTreatmentPlanView(StaffPermissionMixin, views.DeleteView):
    queryset = TreatmentPlan.objects.all()
    template_name = 'staff_panel/treatment_plan_delete.html'
    success_url = reverse_lazy('patient treatment plans')
