from django.shortcuts import render
from .models import Ambiente , Sensores , Historico
from .serializer import UserSerializer , AmbientesSerializer , HistoricoSerializer , SensorSerializer
import pandas as pd
import csv
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView
from rest_framework import status
from Scripts.exportar_planilha import Exportar_dados as exp
from rest_framework.response import Response

from rest_framework_simplejwt.views  import TokenObtainPairView
""" 
    Essa página contém as views 
    Foi utilizado dois recursos do django para fazer :
    -Decorators
    -ClassBase
"""
class LoginView (TokenObtainPairView) :
    serializer_class =  UserSerializer

@api_view(['POST'])
def ExtrairXLSXSensores(request ) :
    if request.method == 'POST' :
        
        dados = exp(request.data['caminho_path'] , request.data['nome_planilha'])
        serializer = SensorSerializer(data = dados.data)
        if serializer.is_valid() :
            serializer.save()

            return Response(serializer.data)
    else :
        Response(status= status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def ExtrairXLSXAmbientes(request ) :
    if request.method == 'POST' :
        
        dados = exp(request.data['caminho_path'] , request.data['nome_planilha'])
        serializer = AmbientesSerializer(data = dados.data)
        if serializer.is_valid() :
            serializer.save()

            return Response(serializer.data)
    else :
        Response(status= status.HTTP_404_NOT_FOUND)


# Create your views here.
