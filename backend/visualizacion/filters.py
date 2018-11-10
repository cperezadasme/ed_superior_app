from django_filters import rest_framework as filters
from .models import Matricula, Titulados


class MatriculaFilter(filters.FilterSet):
    class Meta:
        model = Matricula
        fields = '__all__'


class TituladosFilter(filters.FilterSet):
    class Meta:
        model = Titulados
        fields = '__all__'
