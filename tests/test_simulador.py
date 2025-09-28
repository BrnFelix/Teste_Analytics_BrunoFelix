from vendas_analytcs.simulador import gerar_dados
import pandas as pd

def test_gerar_dados():
    df = gerar_dados()
    assert isinstance(df, pd.DataFrame)
    assert len(df) >= 100  # Deve ter pelo menos 100 registros
