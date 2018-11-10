from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'matricula/$', views.MatriulaAPIView.as_view()),
    url(r'titulados/$', views.TituladosAPIView.as_view()),
]