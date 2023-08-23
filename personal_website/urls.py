
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
import home.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home.views.homepage, name='homepage')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)