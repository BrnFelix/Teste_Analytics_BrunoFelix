from vendas_analytics.limpeza import limpar_dados
from vendas_analytics.simulador import gerar_dados


def test_limpar_dados():
    df = gerar_dados()
    df_limpo = limpar_dados(df)
    assert not df_limpo.isnull().any().any()  # Sem valores nulos
    assert df_limpo["Total_Vendas"].dtype == "float64"
