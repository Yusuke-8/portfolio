"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import settings_base, settings_dev

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path(r'mdeditor/', include('mdeditor.urls')),
]

if settings_base.DEBUG:
    urlpatterns += static(settings_base.MEDIA_URL, document_root=settings_dev.MEDIA_ROOT)
