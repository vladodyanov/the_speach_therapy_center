from django.urls import path

from the_speach_therapy_center.web.views import index

urlpatterns = (
    path('', index, name='index'),
)