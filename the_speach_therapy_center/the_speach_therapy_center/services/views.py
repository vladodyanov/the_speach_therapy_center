from the_speach_therapy_center.accounts.models import Profile
from django.urls import reverse_lazy

from django.views import generic as views
from django.contrib.auth import mixins as auth_mixin
from django.shortcuts import render, redirect
from datetime import datetime, timedelta
from .models import *
from django.contrib import messages

from the_speach_therapy_center.services.forms import CreateQuestionnaireForm
from the_speach_therapy_center.services.models import UserQuestionnaire
from the_speach_therapy_center.services.validators import day_to_weekday, valid_weekday, is_weekday_valid, check_time, \
    check_edit_time


def getting_started(request):
    user = request.user
    user_email = user.email
    profile = Profile.objects.get(user=request.user)
    full_name = profile.full_name
    context = {
        'user_email': user_email,
        'full_name': full_name,
    }
    return render(request, template_name='services/getting_started.html', context=context)


def questionnaires_page(request):
    user = request.user
    user_email = user.email
    profile = Profile.objects.get(user=request.user)
    full_name = profile.full_name
    questionnaires = UserQuestionnaire.objects.filter(user=user)
    questionnaires_count = len([questionnaire for questionnaire in questionnaires])
    context = {
        'questionnaires': questionnaires,
        'questionnaires_count': questionnaires_count,
        'user_email': user_email,
        'full_name': full_name,
    }
    return render(request, template_name='services/questionnaires.html', context=context)


def appointments_page(request):
    user = request.user
    user_email = user.email
    profile = Profile.objects.get(user=request.user)
    full_name = profile.full_name
    appointments = Appointment.objects.filter(user=user).order_by('day', 'time')
    context = {
        'user_email': user_email,
        'full_name': full_name,
        'appointments': appointments,
    }
    return render(request, template_name='services/appointments.html', context=context)


class CreateQuestionnaireView(auth_mixin.LoginRequiredMixin, views.CreateView):
    form_class = CreateQuestionnaireForm
    template_name = 'services/questionnaire_create.html'
    success_url = reverse_lazy('questionnaires_page')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditQuestionnaireView(views.UpdateView):
    queryset = UserQuestionnaire.objects.all()
    fields = ['question_one', 'question_two', 'question_three', 'question_four',
              'question_five', 'comments', ]
    template_name = 'services/questionnaire_edit.html'
    success_url = reverse_lazy('questionnaires_page')


class DeleteQuestionnaireView(views.DeleteView):
    queryset = UserQuestionnaire.objects.all()
    template_name = 'services/questionnaire_delete.html'
    success_url = reverse_lazy('questionnaires_page')


def make_an_appointment(request):
    # Calling 'valid_weekday' Function to Loop days you want in the next 21 days:
    weekdays = valid_weekday(22)
    # Only show the days that are not full:
    validate_weekdays = is_weekday_valid(weekdays)

    if request.method == 'POST':
        service = request.POST.get('service')
        day = request.POST.get('day')
        if service is None:
            messages.success(request, "Please Select A Service!")
            return redirect('make appointment')

        # Store day and service in django session:
        request.session['day'] = day
        request.session['service'] = service
        return redirect('appointment submit')

    return render(request, 'services/appointment_create.html', {
        'weekdays': weekdays,
        'validate_weekdays': validate_weekdays,
    })


def appointment_submit(request):
    user = request.user
    times = [
        "3 PM", "4 PM", "5 PM", "6 PM", "7 PM"
    ]
    today = datetime.now()
    min_date = today.strftime('%Y-%m-%d')
    delta_time = today + timedelta(days=21)
    str_delta_time = delta_time.strftime('%Y-%m-%d')
    max_date = str_delta_time

    # Get stored data from django session:
    day = request.session.get('day')
    service = request.session.get('service')

    # Only show the time of the day that has not been selected before:
    hour = check_time(times, day)
    if request.method == 'POST':
        time = request.POST.get("time")
        date = day_to_weekday(day)

        if service is not None:
            if max_date >= day >= min_date:
                if date != 'Sunday' or date != 'Saturday':
                    if Appointment.objects.filter(day=day).count() < 11:
                        if Appointment.objects.filter(day=day, time=time).count() < 1:
                            appointment_form = Appointment.objects.get_or_create(
                                user=user,
                                service=service,
                                day=day,
                                time=time,
                            )
                            messages.success(request, "Appointment Saved!")
                            return redirect('appointments_page')
                        else:
                            messages.success(request, "The Selected Time Has Been Reserved Before!")
                    else:
                        messages.success(request, "The Selected Day Is Full!")
                else:
                    messages.success(request, "The Selected Date Is Incorrect")
            else:
                messages.success(request, "The Selected Date Isn't In The Correct Time Period!")
        else:
            messages.success(request, "Please Select A Service!")

    return render(request, 'services/appointment_submit.html', {
        'times': hour,
    })


def appointment_update(request, id):
    appointment = Appointment.objects.get(pk=id)
    user_date_picked = appointment.day
    today = datetime.today()
    min_date = today.strftime('%Y-%m-%d')
    delta24 = user_date_picked.strftime('%Y-%m-%d') >= (today + timedelta(days=1)).strftime('%Y-%m-%d')
    weekdays = valid_weekday(22)
    validate_weekdays = is_weekday_valid(weekdays)

    if request.method == 'POST':
        service = request.POST.get('service')
        day = request.POST.get('day')

        request.session['day'] = day
        request.session['service'] = service

        return redirect('appointment update submit', id=id)

    return render(request, 'services/appointment_update.html', {
        'weekdays': weekdays,
        'validate_weekdays': validate_weekdays,
        'delta24': delta24,
        'id': id,
    }
                  )


def appointment_update_submit(request, id):
    user = request.user
    times = [
        "3 PM", "4 PM", "5 PM", "6 PM", "7 PM"
    ]
    today = datetime.now()
    min_date = today.strftime('%Y-%m-%d')
    delta_time = today + timedelta(days=21)
    str_delta_time = delta_time.strftime('%Y-%m-%d')
    max_date = str_delta_time

    day = request.session.get('day')
    service = request.session.get('service')
    hour = check_edit_time(times, day, id)
    appointment = Appointment.objects.get(pk=id)
    user_selected_time = appointment.time

    if request.method == 'POST':
        time = request.POST.get("time")
        date = day_to_weekday(day)

        if service is not None:
            if max_date >= day >= min_date:
                if date != 'Sunday' or date != 'Saturday':
                    if Appointment.objects.filter(day=day).count() < 11:
                        if Appointment.objects.filter(day=day, time=time).count() < 1 or user_selected_time == time:
                            appointment_form = Appointment.objects.filter(pk=id).update(
                                user=user,
                                service=service,
                                day=day,
                                time=time,
                            )
                            messages.success(request, "Appointment Edited!")
                            return redirect('appointments_page')
                        else:
                            messages.success(request, "The Selected Time Has Been Reserved Before!")
                    else:
                        messages.success(request, "The Selected Day Is Full!")
                else:
                    messages.success(request, "The Selected Date Is Incorrect")
            else:
                messages.success(request, "The Selected Date Isn't In The Correct Time Period!")
        else:
            messages.success(request, "Please Select A Service!")
        return redirect('appointments_page')

    return render(request, 'services/appointment_update_submit.html', {
        'times': hour,
        'id': id,
    })

# def staffPanel(request):
#     today = datetime.today()
#     min_date = today.strftime('%Y-%m-%d')
#     delta_time = today + timedelta(days=21)
#     str_delta_time = delta_time.strftime('%Y-%m-%d')
#     max_date = str_delta_time
#     # Only show the Appointments 21 days from today
#     items = Appointment.objects.filter(day__range=[min_date, max_date]).order_by('day', 'time')
# 
#     return render(request, 'staffPanel.html', {
#         'items': items,
#     })
