from django.urls import path, include

from the_speach_therapy_center.services.views import getting_started, CreateQuestionnaireView, \
    EditQuestionnaireView, DeleteQuestionnaireView, questionnaires_page, booking, booking_submit, user_update, \
    user_update_submit

urlpatterns = (
    path('getstarted/',getting_started, name='getting_started'),
    path('booking',booking, name='booking'),
    path('booking-submit',booking_submit, name='booking_submit'),
    # path('user-panel', userPanel, name='userPanel'),
    path('user-update/<int:id>',user_update, name='user_update'),
    path('user-update-submit/<int:id>', user_update_submit, name='user_update_submit'),
    # path('staff-panel', views.staffPanel, name='staffPanel'),

    path('questionnaires/', questionnaires_page, name='questionnaires_page'),
    path('create/', CreateQuestionnaireView.as_view(), name='create_questionnaire'),
    path("<int:pk>/",
         include([
             path("edit/", EditQuestionnaireView.as_view(), name='edit_questionnaire'),
             path("delete/", DeleteQuestionnaireView.as_view(), name='delete_questionnaire'),
         ])),
)
