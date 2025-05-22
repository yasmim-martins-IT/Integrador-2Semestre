from django.urls import path
from .views import LoginView
from . import views

urlpatterns = [
    #Autentificação
    path('login/' , LoginView.as_view(), name = 'Login'),
    
    #Urls relacionadas ao Historico
    path('visualizarHistorico/',views.VisualizarHistorico, name='Visualizar Historico' ) , 
    path('criarHistorico/', views.CreateHistorico , name='Create Historico' ) ,
    path('atualizarHistorico/', views.UpdateHistorico, name = 'Update Historico') , 
    path('deleteHistorico/', views.DeleteHistorico, name='Delete Historico'),

    #Urls relacionadas aos Sensores
    path('visualizarSensor/',views.VisualizarSensores, name='Visualizar Sensores' ) , 
    path('criarSensor/', views.CreateSensor , name='Create Sensor' ) ,
    path('atualizarSensor/', views.UpdateSensores, name = 'Update Sensores') , 
    path('deleteSensor/', views.DeleteSensores, name='Delete Sensores'),

    #Urls relacionadas aos Ambientes
    path('visualizarAmbiente/',views.VisualizarAmbiente, name='Visualizar Ambientes' ) , 
    path('criarAmbiente/', views.CreateAmbiente , name='Create Ambiente' ) ,
    path('atualizarAmbiente/', views.UpdateSensores, name = 'Update Sensores') , 
    path('deleteSensor/', views.DeleteSensores, name='Delete Sensores'),


    #Extrair pdfs
    path('extrairSensores/', views.ExtrairXLSXSensores, name='Extrair Sensores'),
    path('extrairAmbientes', views.ExtrairXLSXAmbientes, name='Extrair Ambientes')


]