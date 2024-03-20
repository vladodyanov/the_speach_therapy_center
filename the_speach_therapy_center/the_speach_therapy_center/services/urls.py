from django.urls import path

from the_speach_therapy_center.services.views import getting_started

urlpatterns = (
    path('getstarted/', getting_started, name='getting_started'),

)