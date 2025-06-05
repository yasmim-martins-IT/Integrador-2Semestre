from django.urls import path
from .views import LoginView
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # para login (token)
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    #Autentificação
    path('login/' , LoginView.as_view(), name = 'Login'),
    
    #Urls relacionadas ao Historico
    path('visualizarHistorico/',views.VisualizarHistorico, name='Visualizar Historico' ) , 
    path('criarHistorico/', views.CreateHistorico , name='Create Historico' ) ,
    path('atualizarHistorico/<int:pk>', views.UpdateHistorico, name = 'Update Historico') , 
    path('deleteHistorico/<int:pk>', views.DeleteHistorico, name='Delete Historico'),
    #get historico com filtros
    path('visualizarHistorico/<int:pk>', views.visualizarHistoricoPeloID, name= 'Visualizer Historico pelo ID'),
    path('visualizarHistorico/<str:data>/', views.VisualizarHistoricoPorDia , name= 'Visualizar o Historico pela data'),

    #Urls relacionadas aos Sensores
    path('visualizarSensor/',views.VisualizarSensores, name='Visualizar Sensores' ) , 
    path('criarSensor/', views.CreateSensor , name='Create Sensor' ) ,
    path('atualizarSensor/<int:pk>', views.UpdateSensores, name = 'Update Sensores') , 
    path('deleteSensor/<int:pk>', views.DeleteSensores, name='Delete Sensores'),
    #get sensores com filtros
    path('visualizarSensorId/<int:pk>',views.visualizarSensoresPeloID, name = 'visualizar_Sensores_por_ID'), 
    path('visualizarSensoresTipo/<str:tipo>/', views.visualizarSensoresPeloTipo , name = 'visuzalizar_sensores_pelo_tipo'),

    #Urls relacionadas aos Ambientes
    path('visualizarAmbiente/',views.VisualizarAmbiente, name='Visualizar Ambientes' ) , 
    path('criarAmbiente/', views.CreateAmbiente , name='Create Ambiente' ) ,
    path('atualizarAmbiente/<int:pk>', views.UpdateAmbiente, name = 'Update Ambiente') , 
    path('deleteAmbiente/<int:pk>', views.DeleteAmbientes, name='Delete ambientes'),
    #get ambientes com filtros
    path('visualizarAmbiente/<int:sig>/', views.visualizarAmbientesPeloSig , name = 'Vizualizar ambiente pelo Sig'),

    #Extrair planilhas
    path('extrairSensores/', views.ExtrairXLSXSensores, name='Extrair Sensores'),
    path('extrairAmbientes/', views.ExtrairXLSXAmbientes, name='Extrair Ambientes') ,
    
    #Importar planilhas
    path('ImportarPlanilhaHistorico/',views.ImportarPlanilhaHistorico, name = 'Importar Planilha Historico') , 
    path('ImportarPlanilhaSensores/',views.ImportarPlanilhaSensores, name = 'Importar Planilha Sensores') , 
    path('ImportarPlanilhaAmbientes/',views.ImportarPlanilhaAmbientes, name = 'Importar Planilha Ambientes') , 
    


]