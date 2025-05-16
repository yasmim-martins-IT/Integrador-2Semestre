import json
from openpyxl import load_workbook

def Exportar_dados(caminho_arquivo, nome_planilha):
    wb = load_workbook(caminho_arquivo, data_only=True)
    ws = wb[nome_planilha] if nome_planilha else wb.active

    dados = []

    cabecalhos = [celula.value for celula in next(ws.iter_rows(min_row=1, max_row=1))]

    for linha in ws.iter_rows(min_row=2, values_only=True):
        dado = {cabecalho: valor for cabecalho, valor in zip(cabecalhos, linha)}
        dados.append(dado)

    return json.dumps(dados, indent=4, ensure_ascii=False)
