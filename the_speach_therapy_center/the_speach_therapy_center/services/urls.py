from django.urls import path

from the_speach_therapy_center.services.views import pediatric_service, adult_service, occupational_service

urlpatterns = (
    path('pediatric/', pediatric_service, name='pediatric'),
    path('adult/', adult_service, name='adult'),
    path('occupational/', occupational_service, name='occupational'),

)