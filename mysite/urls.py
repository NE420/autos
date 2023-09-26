import os
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.static import serve
from django.views.generic import TemplateView

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE_ROOT = os.path.join(BASE_DIR, 'site')

urlpatterns = [
    path('', TemplateView.as_view(template_name='home/main.html')),
    path('admin/', admin.site.urls),
    path('autos/', include('autos.urls')),
     path('accounts/', include('django.contrib.auth.urls')),
]