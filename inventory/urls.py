"""inventory URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
"""Landlot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.db import router
from django.urls import path,include, re_path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render
from django.urls import include, re_path
from django.views.generic.base import TemplateView
router = DefaultRouter()
def render_react(request):
    return render(request, "index.html")
  
urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authen.urls')),
    path('settings/', include('settings.urls')),
    path('user-data/', include('userData.urls')),
    path('items/', include('items.urls')),
    path('related/', include('related.urls')),
    path('help/', include('help.urls')),
    path('pqs/',include('PQS.urls')),
    path('facilities/',include('facilities.urls')),
    path('hr/',include('HR.urls')),
    path('languages/',include('languages.urls')),
    path('message/',include('message.urls')),
    path('item/',include('item.urls')),
    path('maintanance/',include('maintanance.urls')),
    path('reports/',include('reports.urls')),
    path('dashboard/',include('dashboard.urls')),
    path('item/qr/',include('qr.urls')),
    re_path(r'^$', TemplateView.as_view(template_name='static_pages/index.html'), name='home'),




]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
