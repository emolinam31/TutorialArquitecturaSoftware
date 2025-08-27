from django.contrib import admin
from django.urls import path, include
from django.conf import settings 
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),  # URLs del admin de Django
    path('', include('pages.urls')),   # Incluye todas las URLs de la app 'pages'
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)