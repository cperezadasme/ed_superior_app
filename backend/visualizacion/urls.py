from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'matricula/$', views.MatriulaAPIView.as_view()),
    url(r'titulados/$', views.TituladosAPIView.as_view()),
    url(r'years/$', views.YearAPIView.as_view()),
    url(r'instituion-classification-3/$', views.ClassificationLevel3APIView.as_view()),
    url(r'area-knowledge/$', views.AreaKnowledgeAPIView.as_view()),
]
