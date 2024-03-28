from django.urls import path, include

from the_speach_therapy_center.services.views import getting_started, CreateQuestionnaireView, \
    EditQuestionnaireView, DeleteQuestionnaireView, questionnaires_page, \
    make_an_appointment, appointment_submit, appointment_update, appointment_update_submit, appointments_page, \
    delete_appointment

urlpatterns = (
    path('getstarted/', getting_started, name='getting started'),
    path('appointment', make_an_appointment, name='appointment create'),
    path('appointment-submit', appointment_submit, name='appointment submit'),
    path('appointment-update/<int:id>', appointment_update, name='appointment update'),
    path('appointment-update-submit/<int:id>', appointment_update_submit, name='appointment update submit'),
    path('appointment-delete/<int:id>', delete_appointment, name='appointment delete'),
    path('appointments/', appointments_page, name='appointments page'),
    path('questionnaires/', questionnaires_page, name='questionnaires page'),
    path('create/', CreateQuestionnaireView.as_view(), name='questionnaire create'),
    path("<int:pk>/",
         include([
             path("edit/", EditQuestionnaireView.as_view(), name='questionnaire edit'),
             path("delete/", DeleteQuestionnaireView.as_view(), name='questionnaire delete'),
         ])),
)



