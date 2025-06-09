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
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
import sqlite3
from rest_framework_simplejwt.views  import TokenObtainPairView
""" 
    Essa página contém as views 
    Foi utilizado dois recursos do django para fazer :
    -Decorators
    -ClassBase
"""
#view de login para obtenção do token pelo o usuario
class LoginView (TokenObtainPairView) :
    serializer_class = TokenObtainPairSerializer

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

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def visualizarHistoricoPeloID(request , pk ) :
    if request.method == 'GET' :
        try:
            historico = Historico.objects.get(pk = pk)

            serializer = HistoricoSerializer(historico)

            return  Response(serializer.data, status=status.HTTP_200_OK)
        except Historico.DoesNotExist :
            return Response(status=status.HTTP_404_NOT_FOUND)
    else :
        Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def VisualizarHistoricoPorDia(request, data):
    try:
        historicos = Historico.objects.filter(timestamp__date=data)
        serializer = HistoricoSerializer(historicos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(
            {"error": f"Erro: {str(e)}"}, 
            status=status.HTTP_400_BAD_REQUEST
        )



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
            serializer = AmbientesSerializer(ambientes , many = True)

            return Response(serializer.data , status=status.HTTP_200_OK)
        except Ambiente.DoesNotExist :
            return Response(status=status.HTTP_204_NO_CONTENT)
    else :
        Response(status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def visualizarAmbientesPeloSig (request , sig) :
    if request.method == 'GET' :
        try :
            ambientes = Ambiente.objects.filter(sig= sig)

            serializer = AmbientesSerializer(ambientes, many = True)

            return Response(serializer.data, status=status.HTTP_200_OK)
        except Ambiente.DoesNotExist :
           return Response(status=status.HTTP_404_NOT_FOUND)
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
    
    serializer = SensorSerializer(sensores, data=request.data, partial=True)
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

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def visualizarSensoresPeloID(request , pk ) :
    if request.method == 'GET' :
        try:
            sensores = Sensores.objects.get(pk = pk)

            serializer = SensorSerializer(sensores)

            return  Response(serializer.data, status=status.HTTP_200_OK)
        except Sensores.DoesNotExist :
            return Response(status=status.HTTP_404_NOT_FOUND)
    else :
        Response(status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def visualizarSensoresPeloTipo(request, tipo):
    try:
        sensores = Sensores.objects.filter(tipo__iexact=tipo)
        if not sensores.exists():
            return Response({'message': 'Nenhum sensor encontrado para esse tipo.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = SensorSerializer(sensores, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)



#extraindo e importando funções:
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def ExtrairXLSXSensores(request):
    caminho_path = request.data.get('caminho_path')
    nome_planilha = request.data.get('nome_planilha')

    if not caminho_path or not nome_planilha:
        return Response(
            {"error": "Os campos 'caminho_path' e 'nome_planilha' são obrigatórios."},
            status=400
        )

    try:
        dados_excel = exp(caminho_path, nome_planilha)  # Suponha que isso retorna uma lista de dicionários
    except Exception as e:
        return Response(
            {"error": f"Erro ao ler a planilha: {str(e)}"},
            status=500
        )

    registros_criados = []
    try:
        for item in dados_excel:
            sensor = Sensores.objects.create(
                sensor=item.get('sensor'),
                tipo=item.get('sensor'),
                mac_address=item.get('mac_address'),
                unidade_med=item.get('unidade_med'),
                latitude=item.get('latitude'),
                longitude=float(item.get('longitude')),
                status=item.get('status', True)
            )
            registros_criados.append({
                 "id": sensor.id,
                "sensor": sensor.sensor,
                "tipo": sensor.sensor,
                "mac_address": sensor.mac_address,
                "unidade_med": sensor.unidade_med,
                "latitude": sensor.latitude,
                "longitude": sensor.longitude,
                "status": sensor.status
            })

    except Exception as e:
        return Response(
            {"error": f"Erro ao salvar no banco de dados: {str(e)}"},
            status=500
        )

    return Response(
        {"message": "Dados inseridos com sucesso!", "registros": registros_criados},
        status=201
    )
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def ExtrairXLSXAmbientes(request):
    caminho_path = request.data.get('caminho_path')
    nome_planilha = request.data.get('nome_planilha')

    if not caminho_path or not nome_planilha:
        return Response(
            {"error": "Os campos 'caminho_path' e 'nome_planilha' são obrigatórios."},
            status=400
        )

    try:
        dados_excel = exp(caminho_path, nome_planilha)
    except Exception as e:
        return Response(
            {"error": f"Erro ao ler a planilha: {str(e)}"},
            status=500
        )

    registros_criados = []
    try:
        for item in dados_excel:
            # Busca o sensor e o ambiente pelo nome (ou ID, dependendo da sua planilha)
            sensor_nome = item.get('sensor')
            ambiente_nome = item.get('ambiente')

            try:
                sensor = Sensores.objects.get(sensor=sensor_nome)
            except Sensores.DoesNotExist:
                return Response({"error": f"Sensor '{sensor_nome}' não encontrado."}, status=400)

            try:
                ambiente = Ambiente.objects.get(nome=ambiente_nome)
            except Ambiente.DoesNotExist:
                return Response({"error": f"Ambiente '{ambiente_nome}' não encontrado."}, status=400)

            historico = Historico.objects.create(
                sensor=sensor,
                ambiente=ambiente,
                valor=float(item.get('valor', 0))
            )

            registros_criados.append({
                "id": historico.id,
                "sensor": sensor.sensor,
                "ambiente": ambiente.nome,
                "valor": historico.valor,
                "timestamp": historico.timestamp
            })

    except Exception as e:
        return Response(
            {"error": f"Erro ao salvar no banco de dados: {str(e)}"},
            status=500
        )

    return Response(
        {"message": "Dados de histórico inseridos com sucesso!", "registros": registros_criados},
        status=201
    )




@api_view(['GET'])
@permission_classes([IsAuthenticated])
def ImportarPlanilhaHistorico(request) :
    try :

        conn = sqlite3.connect("db.sqlite3")

        df = pd.read_sql_query("SELECT * FROM app_historico", conn)

        df.to_excel("planilhaImportadaHistorico.xlsx", index=False)  

        df.to_csv("PlanilhaImportadaHistorico.csv", index=False)


        conn.close()
        
        return Response({'mesagem':'planilha criada com sucesso'},status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def ImportarPlanilhaSensores(request) :
    try:
        conn = sqlite3.connect("db.sqlite3")

        df = pd.read_sql_query("SELECT * FROM app_sensores", conn)

        df.to_excel("planilhaImportadaSensores.xlsx", index=False)  

        df.to_csv("PlanilhaImportadaSensores.csv", index=False)


        conn.close()
        
        return Response({'mesagem':'planilha criada com sucesso'},status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def ImportarPlanilhaAmbientes(request) :
    try:
        conn = sqlite3.connect("db.sqlite3")

        df = pd.read_sql_query("SELECT * FROM app_ambiente", conn)

        df.to_excel("planilhaImportadaSensores.xlsx", index=False)  

        df.to_csv("PlanilhaImportadaAmbientes.csv", index=False)


        conn.close()
        
        return Response({'mesagem':'planilha criada com sucesso'},status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


