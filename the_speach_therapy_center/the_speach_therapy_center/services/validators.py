from django.utils import timezone

from the_speach_therapy_center.services.models import Appointment
from datetime import datetime, timedelta
from .models import *


def day_to_weekday(x):
    z = datetime.strptime(x, "%Y-%m-%d")
    y = z.strftime('%A')
    return y


def valid_weekday(days):
    weekdays_list = ['Monday', 'Tuesday', 'Thursday', 'Wednesday', 'Friday']
    # Loop days in the next 21 days:
    today = datetime.now()
    weekdays = []
    for i in range(0, days):
        x = today + timedelta(days=i)
        y = x.strftime('%A')
        if y in weekdays_list:
            weekdays.append(x.strftime('%Y-%m-%d'))
    return weekdays


def is_weekday_valid(x):
    validate_weekdays = []
    for j in x:
        if Appointment.objects.filter(day=j).count() < 10:
            validate_weekdays.append(j)
    return validate_weekdays


def check_time(times, day):
    # Shows the time of the day that has not been selected before:
    x = []
    for k in times:
        if Appointment.objects.filter(day=day, time=k).count() < 1:
            x.append(k)
    return x


def check_edit_time(times, day, id):
    # Show the time of the day that has not been selected before:
    x = []
    appointment = Appointment.objects.get(pk=id)
    time = appointment.time
    for k in times:
        if Appointment.objects.filter(day=day, time=k).count() < 1 or time == k:
            x.append(k)
    return x


# def get_timezone_day(timezone_name):
#     tz = timezone.timezone(timezone_name)
#     current_time = timezone.localtime(timezone.now(), tz)
#     day = current_time.strftime('%A')
#     return day
