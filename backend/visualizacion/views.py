# from django.shortcuts import render
from rest_framework.generics import ListAPIView

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
