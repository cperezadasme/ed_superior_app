"""ed_superior URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url, include
from django.views.generic import TemplateView
from backend.visualizacion.views import *

urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'api/', include('backend.visualizacion.urls')),
    url(
        r'index/$',
        TemplateView.as_view(template_name='index.html'),
        name='index',
    ),
    url(
        r'barchart_titulados/$',
        TemplateView.as_view(template_name='barchart_titulados.html'),
        name='barchart_titulados',
    ),
    url(
        r'barchart_matriculados/$',
        TemplateView.as_view(template_name='barchart_matriculados.html'),
        name='barchart_matriculados',
    ),
    url(
        r'barchart_matriculados_titulados/$',
        TemplateView.as_view(template_name='barchart_matriculados_titulados.html'),
        name='barchart_matriculados_titulados',
    ),
    url(r'titulados_region/', get_titulados_region, name="titulados_region"),
    url(r'matriculados_region/', get_matriculados_region, name="matriculados_region"),
    url(r'vs_region/', get_vs_region, name="vs_region"),
]
