from django.urls import path, include

from the_speach_therapy_center.services.views import getting_started, CreateQuestionnaireView, DetailsQuestionnaireView, \
    EditQuestionnaireView, DeleteQuestionnaireView, questionnaires_page

urlpatterns = (
    path('getstarted/', questionnaires_page, name='questionnaires_page'),
    path('questionnaires/', getting_started, name='getting_started'),
    path('create/', CreateQuestionnaireView.as_view(), name='create_questionnaire'),
    path("<int:pk>/",
         include([
             path("details/", DetailsQuestionnaireView.as_view(), name='details_questionnaire'),
             path("edit/", EditQuestionnaireView.as_view(), name='edit_questionnaire'),
             path("delete/", DeleteQuestionnaireView.as_view(), name='delete_questionnaire'),
         ])),
)
