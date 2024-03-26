from django.urls import path

from the_speach_therapy_center.staff_panel.views import patient_records

urlpatterns = (
    path('patient_records/', patient_records, name='patient_records'),

)