from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('the_speach_therapy_center.web.urls')),
    path('accounts/', include('the_speach_therapy_center.accounts.urls')),
    path('services/', include('the_speach_therapy_center.services.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
