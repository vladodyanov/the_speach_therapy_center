from django.urls import path, include

from the_speach_therapy_center.staff_panel.views import patient_records, patient_details, patient_appointments, \
    CreateTreatmentPlanView, EditTreatmentPlanView, DeleteTreatmentPlanView, patient_treatment_plans, \
    DetailsTreatmentPlanView

urlpatterns = (
    path('patient_appointments/', patient_appointments, name='patient appointments'),
    path('patient_records/', patient_records, name='patient records'),
    path('patient_records/<int:pk>/', patient_details, name='patient details'),
    path('patient_treatment_plans', patient_treatment_plans, name='patient treatment plans'),
    path('create/', CreateTreatmentPlanView.as_view(), name='treatment plan create'),
    path('<int:pk>/',
         include([
            path('details/', DetailsTreatmentPlanView.as_view(), name='treatment plan details'),
             path('edit/', EditTreatmentPlanView.as_view(), name='treatment plan edit'),
             path('delete/', DeleteTreatmentPlanView.as_view(), name='treatment plan delete'),
         ])),

)