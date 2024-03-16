from django.urls import path

from the_speach_therapy_center.web.views import index, about, contact, gallery

urlpatterns = (
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('gallery/', gallery, name='gallery'),

)