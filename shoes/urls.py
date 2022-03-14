from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import include
from django.contrib.auth.models import User

urlpatterns = [
    path('api/v1/admin/', admin.site.urls),
    path('api/v1/', include('main.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
