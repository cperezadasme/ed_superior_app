from rest_framework import serializers
from .models import Matricula, Titulados


class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        fields = '__all__'


class TituladosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Titulados
        fields = '__all__'
