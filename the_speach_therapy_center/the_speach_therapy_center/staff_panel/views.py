from datetime import datetime
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixin

from the_speach_therapy_center.accounts.models import Profile
from the_speach_therapy_center.services.models import Appointment
from the_speach_therapy_center.staff_panel.forms import CreateTreatmentPlanForm, EditTreatmentPlanForm
from the_speach_therapy_center.staff_panel.models import TreatmentPlan


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


def patient_treatment_plans(request):
    user = request.user
    treatment_plans = TreatmentPlan.objects.all()

    context = {
        'user': user,
        'treatment_plans': treatment_plans,
    }

    return render(request, 'staff_panel/treatment_plans.html', context=context)


class CreateTreatmentPlanView(auth_mixin.LoginRequiredMixin, views.CreateView):
    model = TreatmentPlan
    form_class = CreateTreatmentPlanForm
    template_name = 'staff_panel/treatment_plan_create.html'
    success_url = reverse_lazy('patient treatment plans')

    def form_valid(self, form):
        form.instance.therapist = self.request.user
        return super().form_valid(form)


class DetailsTreatmentPlanView(views.DetailView):
    queryset = TreatmentPlan.objects.all()
    template_name = "staff_panel/treatment_plan_details.html"


class EditTreatmentPlanView(views.UpdateView):
    model = TreatmentPlan
    form_class = EditTreatmentPlanForm
    template_name = 'staff_panel/treatment_plan_edit.html'
    success_url = reverse_lazy('patient treatment plans')


class DeleteTreatmentPlanView(views.DeleteView):
    queryset = TreatmentPlan.objects.all()
    template_name = 'staff_panel/treatment_plan_delete.html'
    success_url = reverse_lazy('patient treatment plans')
