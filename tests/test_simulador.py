import pandas as pd

from vendas_analytics.simulador import gerar_dados


def test_gerar_dados():
    df = gerar_dados()
    assert isinstance(df, pd.DataFrame)
    assert len(df) >= 100  # Deve ter pelo menos 100 registros
