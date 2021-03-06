# from django.shortcuts import render
from django.db.models import Sum
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse
import csv

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
        queryset = Matricula.objects.values_list('year', flat=True).distinct().order_by('-year')
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


@api_view(['GET', 'POST', ])
def get_titulados_region(self):

    region_dict = {}
    queryset = Titulados.objects.all()
    for register in queryset:
        region = getattr(register, 'region')
        if region in region_dict:
            region_dict[region] += 1
        else:
            region_dict[region] = 0

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

    writer = csv.writer(response)

    writer.writerow(['Region', 'Titulados', ])
    for region in region_dict:
        writer.writerow([region, region_dict[region]])
    return response


@api_view(['GET', 'POST', ])
def get_matriculados_region(self):
    region_dict = {}
    queryset = Matricula.objects.all()
    for register in queryset:
        region = getattr(register, 'region')
        if region in region_dict:
            region_dict[region] += 1
        else:
            region_dict[region] = 0

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

    writer = csv.writer(response)

    writer.writerow(['Region', 'Matrícula', ])
    for region in region_dict:
        writer.writerow([region, region_dict[region]])
    return response


@api_view(['GET', 'POST', ])
def get_vs_region(self):
    query_params = self.GET
    query_matricula = Matricula.objects.all()
    query_titulados = Titulados.objects.all()

    if query_params.get('year'):
        query_matricula = query_matricula.filter(year=query_params.get('year'))
        query_titulados = query_titulados.filter(year=query_params.get('year'))

    if query_params.get('area_of_knowledge'):
        value = query_params.get('area_of_knowledge')
        query_matricula = query_matricula.filter(area_of_knowledge=value)
        query_titulados = query_titulados.filter(area_of_knowledge=value)

    if query_params.get('institution_classification_level_3'):
        value = query_params.get('institution_classification_level_3')
        query_matricula = query_matricula.filter(institution_classification_level_3=value)
        query_titulados = query_titulados.filter(institution_classification_level_3=value)

    region_dict_matricula = query_matricula.values('region').annotate(total=Sum('total_students'))
    region_dict_titulados = query_titulados.values('region').annotate(total=Sum('total_graduates'))

    region_dict_response = []
    for matricula in region_dict_matricula:
        details = {}

        total_titulados = region_dict_titulados.get(region=matricula['region']).get('total')
        details["region"] = matricula['region']
        details["matricula"] = matricula.get('total')
        details["titulados"] = total_titulados
        region_dict_response.append(details)

    print(region_dict_response)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

    writer = csv.writer(response)
    writer.writerow(['Region', 'Matrícula', 'Titulados'])
    for region in region_dict_response:
        writer.writerow([region["region"], region["matricula"], region["titulados"]])

    return response
