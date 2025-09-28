from vendas_analytics.analise_exploratoria import AnaliseExploratoria
from vendas_analytics.limpeza import limpar_dados
from vendas_analytics.simulador import gerar_dados

# Gerar e limpar dados
df = gerar_dados()
df_limpo = limpar_dados(df)

# Salvar CSV
df_limpo.to_csv("data/data_clean.csv", index=False)

# Exibir gráficos
ae = AnaliseExploratoria(df_limpo)
ae.vendas_mensais()
ae.vendas_por_categoria()
ae.participacao_por_prato()
