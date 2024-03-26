from django.urls import path

from the_speach_therapy_center.staff_panel.views import patient_records, patient_details

urlpatterns = (
    path('patient_records/', patient_records, name='patient_records'),
    path('patient_records/<int:pk>/', patient_details, name='patient_details')

)