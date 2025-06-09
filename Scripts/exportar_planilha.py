import json
from openpyxl import load_workbook


import pandas as pd
import os

def Exportar_dados(caminho_path, nome_planilha):
    arquivo = os.path.join(caminho_path, f"{nome_planilha}.xlsx")
    
    df = pd.read_excel(arquivo)
    df = df.fillna('')  # Preencher NaN com string vazia, se necessário

    lista_dados = []

    for _, row in df.iterrows():
        dado = {
            "sensor": str(row.get("sensor", "")).strip(),
            "tipo": str(row.get("tipo", "")).strip(),
            "mac_address": str(row.get("mac_address", "")).strip(),
            "unidade_med": str(row.get("unidade_med", "")).strip(),
            "latitude": str(row.get("latitude", "")).strip(),
            "longitude": float(row.get("longitude", 0)),
            "status": bool(row.get("status", True))
        }
        lista_dados.append(dado)

    return lista_dados



def Exportar_dados_ambientes(caminho_path, nome_planilha):
    arquivo = os.path.join(caminho_path, f"{nome_planilha}.xlsx")
    
    df = pd.read_excel(arquivo)

    # Remover espaços em branco dos nomes das colunas
    df.columns = df.columns.str.strip()

    # Substituir valores nulos por string vazia
    df = df.fillna('')

    lista_dados = []

    for _, row in df.iterrows():
        dado = {
            "sig": str(row.get("sig", "")).strip(),
            "descricao": str(row.get("descricao", "")).strip(),
            "ni": str(row.get("ni", "")).strip(),
            "responsavel": str(row.get("responsavel", "")).strip()
        }
        lista_dados.append(dado)

    return lista_dados
