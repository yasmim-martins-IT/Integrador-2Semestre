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
#view de login para obtenção do token pelo o usuario
class LoginView (TokenObtainPairView) :
    serializer_class =  UserSerializer

#crud Historico:
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def CreateHistorico(request):
    serializer = HistoricoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def UpdateHistorico(request, pk):
    try:
        historico = Historico.objects.get(pk=pk)
    except Historico.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = HistoricoSerializer(historico, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def DeleteHistorico(request , pk) :
    if request.method == 'DELETE' :
        try :
            historico_delete = Historico.objects.get(pk = pk)

        except Historico.DoesNotExist:
            return Response(status= status.HTTP_404_NOT_FOUND)
        
        historico_delete.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
    else :
       return Response(status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def VisualizarHistorico(request) :
    if request.method == 'GET' :
        try :
            historicos = Historico.objects.all()
            serializer = HistoricoSerializer(historicos, many = True)

            return Response(serializer.data , status=status.HTTP_200_OK)
        except Historico.DoesNotExist :
            return Response(status=status.HTTP_204_NO_CONTENT)
    else :
        Response(status=status.HTTP_400_BAD_REQUEST)
#crud Ambientes :

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def CreateAmbiente(request):
    serializer = AmbientesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def UpdateAmbiente(request, pk):
    try:
        ambiente = Ambiente.objects.get(pk=pk)
    except Ambiente.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = AmbientesSerializer(ambiente, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def DeleteAmbientes(request , pk) :
    if request.method == 'DELETE' :
        try :
            ambiente_delete = Ambiente.objects.get(pk = pk)

        except Ambiente.DoesNotExist:
            return Response(status= status.HTTP_404_NOT_FOUND)
        
        ambiente_delete.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
    else :
       return Response(status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def VisualizarAmbiente(request) :
    if request.method == 'GET' :
        try :
            ambientes = Ambiente.objects.all()
            serializer = AmbientesSerializer(ambientes, many = True)

            return Response(serializer.data , status=status.HTTP_200_OK)
        except Ambiente.DoesNotExist :
            return Response(status=status.HTTP_204_NO_CONTENT)
    else :
        Response(status=status.HTTP_400_BAD_REQUEST)

#crud Sensores
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def CreateSensor(request):
    serializer = SensorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def UpdateSensores(request, pk):
    try:
        sensores= Sensores.objects.get(pk=pk)
    except Sensores.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = HistoricoSerializer(sensores, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def DeleteSensores(request , pk) :
    if request.method == 'DELETE' :
        try :
            sensores_delete = Sensores.objects.get(pk = pk)

        except Sensores.DoesNotExist:
            return Response(status= status.HTTP_404_NOT_FOUND)
        
        sensores_delete.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
    else :
       return Response(status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def VisualizarSensores(request) :
    if request.method == 'GET' :
        try :
            sensores=Sensores.objects.all()
            serializer = SensorSerializer(sensores, many = True)

            return Response(serializer.data , status=status.HTTP_200_OK)
        except Sensores.DoesNotExist :
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