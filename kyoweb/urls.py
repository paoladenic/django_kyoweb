from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import handler404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', include('login.urls')),
    path('socio/', include('socio.urls')),
    path('', include('web.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
