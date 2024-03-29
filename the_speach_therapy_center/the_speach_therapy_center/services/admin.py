from django.contrib import admin

from the_speach_therapy_center.services.models import UserQuestionnaire, Appointment


@admin.register(UserQuestionnaire)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('comments', 'created_at', 'question_one', 'question_two', 'question_three', 'question_four',
                    'question_five')


@admin.register(Appointment)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('service', 'day', 'time')
