from django.urls import path

from the_speach_therapy_center.services.views import getting_started

urlpatterns = (
    path('getstarted/', getting_started, name='getting_started'),
    # path("<str:username>/pet/<slug:pet_slug>/",
    #      include([
    #          path("", PetDetailView.as_view(), name='details pet'),
    #          path("edit/", PetEditView.as_view(), name='edit pet'),
    #          path("delete/", PetDeleteView.as_view(), name='delete pet'),
    #      ])),

)