import pandas as pd
import os
import datetime as datetime
import django
from app.models import Sensores , Historico

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "smart_city.settings")
django.setup()

def importar_planilha (path ,tiposSensor , siglaAmbiente) :
    try :
        sensor = Sensores.objects.get(tipo = tiposSensor, ambienteSigla = siglaAmbiente) 
    except Sensores.DoesNotExist :
        print(f'Sendo do tipo {tiposSensor} ou o Ambiente {siglaAmbiente} não foi encontrado')
        return
    
    df = pd.read_excel('../Dados Integrador/Ambientes.xlsx')
