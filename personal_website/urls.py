
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include
import data_proj.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', data_proj.views.homepage, name='homepage'),
    path('blog/', include('blog.urls')), # directs it to 'blog.url' under the blog directory
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)