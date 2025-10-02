import os

from sql.consulta_sql import executar_consultas
from sql.database import inserir_dados
from src.analise_exploratoria import AnaliseExploratoria
from src.limpeza import LimpezaDados
from src.relatorio_terminal import RelatorioTerminal
from src.simulador import SimuladorDados

def executar_pipeline():

    df = SimuladorDados().gerar_dados()
    df_limpo = LimpezaDados().limpar(df)
    df_limpo.to_csv("data/data_clean.csv", index=False, encoding="utf-8")
    inserir_dados(df_limpo)
    RelatorioTerminal(df_limpo).imprimir_relatorio()
    analise = AnaliseExploratoria(df_limpo)
    analise.vendas_mensais()
    analise.vendas_por_categoria()
    analise.participacao_por_prato()

    executar_consultas()
