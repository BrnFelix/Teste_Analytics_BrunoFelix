import pandas as pd
from vendas_analytcs.simulador import gerar_dados
from vendas_analytcs.limpeza import limpar_dados
from vendas_analytcs.analise_exploratoria import AnaliseExploratoria

# Gerar e limpar dados
df = gerar_dados()
df_limpo = limpar_dados(df)

# Salvar CSV
df_limpo.to_csv('data/data_clean.csv', index=False)

# Exibir gráficos
ae = AnaliseExploratoria(df_limpo)
ae.vendas_mensais()
ae.vendas_por_categoria()
ae.participacao_por_prato()
