# from django.shortcuts import render
from django.db.models import Sum
from rest_framework.generics import ListAPIView, GenericAPIView
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


class RegionAPIView(APIView):
    def get(self, request, format=None):
        queryset = Matricula.objects.values_list('region', flat=True).distinct()
        return Response(queryset)


class TotalTituladosAPIView(ListAPIView):
    queryset = Titulados.objects.all()
    serializer_class = TituladosSerializer
    filter_class = TituladosFilter

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.queryset)

        graduates_by_institution_types = queryset.values(
            'year', 'institution_classification_level_3',
        ).annotate(total_titulados=Sum('total_graduates'))

        institution_types = graduates_by_institution_types.values_list(
            'institution_classification_level_3', flat=True).distinct()
        years = graduates_by_institution_types.values_list(
            'year', flat=True).distinct()

        data = []

        for institution_type in institution_types:
            values = []
            for year in years:
                item = {}
                total = graduates_by_institution_types.get(
                    institution_classification_level_3=institution_type, year=year,
                ).get('total_titulados')

                item['total'] = total
                item['year'] = year

                values.append(item)

            institution = {
                'name': institution_type,
                'values': values,
            }

            data.append(institution)

        return Response(data)
