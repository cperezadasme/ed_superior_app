# from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Matricula, Titulados
from .serializers import MatriculaSerializer, TituladosSerializer
from . filters import MatriculaFilter, TituladosFilter


class MatriulaAPIView(ListAPIView):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    filter_class = MatriculaFilter


class TituladosAPIView(ListAPIView):
    queryset = Titulados.objects.all()
    serializer_class = TituladosSerializer
    filter_class = TituladosFilter


class YearAPIView(APIView):

    def get(self, request, format=None):
        queryset = Matricula.objects.values_list('year', flat=True).distinct()
        return Response(queryset)


class ClassificationLevel3APIView(APIView):
    def get(self, request, format=None):
        queryset = Matricula.objects.values_list(
            'institution_classification_level_3', flat=True).distinct()
        return Response(queryset)


class AreaKnowledgeAPIView(APIView):
    def get(self, request, format=None):
        queryset = Matricula.objects.values_list('area_of_knowledge', flat=True).distinct()
        return Response(queryset)
