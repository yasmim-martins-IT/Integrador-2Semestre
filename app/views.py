from django.shortcuts import render
from .models import Ambiente , Sensores , Historico
from .serializer import UserSerializer , AmbientesSerializer , HistoricoSerializer , SensorSerializer
import pandas as pd
import csv
from rest_framework.decorators import api_view , permission_classes
from rest_framework.generics import ListAPIView
from rest_framework import status
from Scripts.exportar_planilha import Exportar_dados as exp
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

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
@permission_classes([IsAuthenticated])
def createHistorico(request):
    if request.method == 'POST' :
        serializer = HistoricoSerializer(serializer.data)

        if serializer.is_valid() :
            serializer.save()

            return Response(serializer.data , status= status.HTTP_201_CREATED )
        else :
            Response(status= status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateHistorico(request , pk) :
    if request.method == 'PUT' :
        try:
            historico_atualizado = Historico.objects.get(pk = pk)
        except Historico.DoesNotExist :
           return Response(status= status.HTTP_404_NOT_FOUND)
        
        serializer  = HistoricoSerializer(historico_atualizado , data = request.data ,partial = True )
    else :
        Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteHistorico(request , pk) :
    if request.method == 'DELETE' :
        try :
            historico_delete = Historico.objects.get(pk = pk)

        except Historico.DoesNotExist:
            return Response(status= status.HTTP_404_NOT_FOUND)
        
        historico_delete.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
    else :
        Response(status=status.HTTP_400_BAD_REQUEST)
        
        

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def ExtrairXLSXSensores(request ) :
    
    if request.method == 'POST' :
        
        dados = exp(request.data['caminho_path'] , request.data['nome_planilha'])
        serializer = SensorSerializer(data = dados.data)
        serializerHistorico  = HistoricoSerializer(dados = dados.data)
        if serializer.is_valid() and serializerHistorico.is_valid() :
            serializer.save()
            serializerHistorico.save()

            return Response(serializer.data , status= status.HTTP_201_CREATED )
    else :
        Response(status= status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def ExtrairXLSXAmbientes(request ) :
    if request.method == 'POST' :
        
        dados = exp(request.data['caminho_path'] , request.data['nome_planilha'])
        serializer = AmbientesSerializer(data = dados.data)
        serializerHistorico = HistoricoSerializer(dados = dados.data)
        if serializer.is_valid() and serializerHistorico.is_valid() :
            serializer.save()
            serializerHistorico.save()


            return Response(serializer.data , status= status.HTTP_201_CREATED)
    else :
        Response(status= status.HTTP_400_BAD_REQUEST)



# Create your views here.
