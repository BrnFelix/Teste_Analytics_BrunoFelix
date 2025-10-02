import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.simulador import SimuladorDados
from src.limpeza import LimpezaDados

def test_limpar_dados():
    df = SimuladorDados().gerar_dados()
    df_limpo = LimpezaDados().limpar(df)
    assert not df_limpo.isnull().any().any()
    assert df_limpo["Total_Vendas"].dtype == "float64"
