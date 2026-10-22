import json
import os
from datetime import datetime

ARQUIVO_HISTORICO = "historico_imc.json"


def carregar_historico():
    if not os.path.exists(ARQUIVO_HISTORICO):
        return []
    with open(ARQUIVO_HISTORICO, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def salvar_medicao(peso, altura, imc, classificacao):
    historico = carregar_historico()
    historico.append({
        "data": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "peso": peso,
        "altura": altura,
        "imc": round(imc, 2),
        "classificacao": classificacao,
    })
    with open(ARQUIVO_HISTORICO, "w", encoding="utf-8") as arquivo:
        json.dump(historico, arquivo, ensure_ascii=False, indent=2)
