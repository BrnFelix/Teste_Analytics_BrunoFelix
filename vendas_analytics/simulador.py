import random
from datetime import datetime, timedelta

import numpy as np
import pandas as pd


def gerar_dados():
    np.random.seed(42)
    random.seed(42)

    pratos = [
        "Feijoada",
        "Hambúrguer",
        "Pizza",
        "Salada Grega",
        "Sushi",
        "Lasanha",
        "Tiramisu",
        "Suco Natural",
    ]
    categorias = {
        "Feijoada": "Prato Principal",
        "Hambúrguer": "Prato Principal",
        "Pizza": "Prato Principal",
        "Salada Grega": "Entrada",
        "Sushi": "Prato Principal",
        "Lasanha": "Prato Principal",
        "Tiramisu": "Sobremesa",
        "Suco Natural": "Bebida",
    }

    def gerar_data():
        start = datetime(2023, 1, 1)
        return start + timedelta(days=random.randint(0, 364))

    dados = []
    for i in range(1, 101):
        prato = random.choice(pratos)
        categoria = categorias[prato]
        quantidade = random.randint(1, 10)
        preco = round(random.uniform(10, 120), 2)
        data = gerar_data()
        dados.append([i, data, prato, categoria, quantidade, preco])

    df = pd.DataFrame(
        dados, columns=["ID", "Data", "Prato", "Categoria", "Quantidade", "Preco"]
    )

    # Inserindo valores nulos e duplicatas
    df.loc[5, "Prato"] = np.nan
    df.loc[10, "Preco"] = np.nan
    df.loc[13, "Categoria"] = np.nan
    df.loc[20, "Quantidade"] = np.nan
    df.loc[29, "Data"] = np.nan
    df.loc[30, "Categoria"] = np.nan
    df.loc[33, "Prato"] = np.nan
    df.loc[47, "Quantidade"] = np.nan
    df.loc[65, "Data"] = np.nan
    df.loc[83, "Quantidade"] = np.nan

    df = pd.concat([df, df.iloc[[3, 8, 12, 3]]], ignore_index=True)

    return df
