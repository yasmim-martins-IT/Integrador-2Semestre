import json
from openpyxl import load_workbook

def Exportar_dados(caminho_arquivo, nome_planilha):
    """Função que tem como o objetivo extrair dados de uma planilha excel e 
        transforma-los em JSON.

        Usamos o metodo load_workbook da biblioteca openpyxl
        Os dados são previamente armazenados em uma lista antes de serem transformados em JSON
        importamos a biblioteca do Python Json para utilizar o metodo .dumps para transforma-los em json
    """
    wb = load_workbook(caminho_arquivo, data_only=True)
    ws = wb[nome_planilha] if nome_planilha else wb.active

    dados = []

    cabecalhos = [celula.value for celula in next(ws.iter_rows(min_row=1, max_row=1))]

    for linha in ws.iter_rows(min_row=2, values_only=True):
        dado = {cabecalho: valor for cabecalho, valor in zip(cabecalhos, linha)}
        dados.append(dado)

    return json.dumps(dados, indent=4, ensure_ascii=False)
