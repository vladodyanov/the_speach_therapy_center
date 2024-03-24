from django.urls import path, include

from the_speach_therapy_center.services.views import getting_started, CreateQuestionnaireView,\
    EditQuestionnaireView, DeleteQuestionnaireView, questionnaires_page

urlpatterns = (
    path('getstarted/',getting_started, name='getting_started'),
    path('questionnaires/', questionnaires_page, name='questionnaires_page'),
    path('create/', CreateQuestionnaireView.as_view(), name='create_questionnaire'),
    path("<int:pk>/",
         include([
             path("edit/", EditQuestionnaireView.as_view(), name='edit_questionnaire'),
             path("delete/", DeleteQuestionnaireView.as_view(), name='delete_questionnaire'),
         ])),
)
