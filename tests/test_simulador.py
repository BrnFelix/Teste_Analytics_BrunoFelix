import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pandas as pd
from src.simulador import SimuladorDados

def test_gerar_dados():
    df = SimuladorDados().gerar_dados()
    assert isinstance(df, pd.DataFrame)
    assert len(df) >= 100
    assert "ID" in df.columns
    assert "Total_Vendas" in df.columns

