from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'matricula/$', views.MatriulaAPIView.as_view(), name='matricula'),
    url(r'titulados/$', views.TituladosAPIView.as_view(), name='titulados'),
    url(r'years/$', views.YearAPIView.as_view(), name='years'),
    url(
        r'instituion-classification-3/$',
        views.ClassificationLevel3APIView.as_view(),
        name='classification-3',
    ),
    url(r'area-knowledge/$', views.AreaKnowledgeAPIView.as_view(), name='area-knowledge'),
    url(r'region/$', views.RegionAPIView.as_view(), name='region'),
    url(r'total-graduates/$', views.TotalTituladosAPIView.as_view(), name='total-graduates'),
]
