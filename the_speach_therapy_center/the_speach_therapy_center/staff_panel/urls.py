from django.urls import path, include

from the_speach_therapy_center.staff_panel.views import patient_records, patient_details, patient_appointments, \
    CreateTreatmentPlanView, EditTreatmentPlanView, DeleteTreatmentPlanView, patient_treatment_plans, \
    DetailsTreatmentPlanView

urlpatterns = (
    path('patient_appointments/', patient_appointments, name='patient_appointments'),
    path('patient_records/', patient_records, name='patient_records'),
    path('patient_records/<int:pk>/', patient_details, name='patient_details'),
    path('patient_treatment_plans', patient_treatment_plans, name='patient_treatment_plans'),
    path('create/', CreateTreatmentPlanView.as_view(), name='create_treatment_plan'),
    path('<int:pk>/',
         include([
            path('details/', DetailsTreatmentPlanView.as_view(), name='details_treatment_plan'),
             path('edit/', EditTreatmentPlanView.as_view(), name='edit_treatment_plan'),
             path('delete/', DeleteTreatmentPlanView.as_view(), name='delete_treatment_plan'),
         ])),

)