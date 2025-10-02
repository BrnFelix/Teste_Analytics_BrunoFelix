import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pandas as pd

def test_vendas_por_prato():
    df = pd.read_csv("data/data_clean.csv")
    df["Total_Vendas"] = df["Quantidade"] * df["Preco"]
    vendas_por_prato = df.groupby("Prato")["Total_Vendas"].sum()
    assert not vendas_por_prato.empty
    assert vendas_por_prato.max() > 0
