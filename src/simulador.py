import random
from datetime import datetime, timedelta

import numpy as np
import pandas as pd


class SimuladorDados:
    def gerar_dados(self):
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

        # Inserindo nulos e duplicatas
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

        # Ajuste de preço com crescimento temporal
        def ajustar_preco_temporal(row):
            categoria = row["Categoria"]
            preco = row["Preco"]
            data = pd.to_datetime(row["Data"], errors="coerce")

            limites = {
                "Entrada": (15.0, 40.0),
                "Prato Principal": (30.0, 80.0),
                "Bebida": (8.0, 25.0),
                "Sobremesa": (12.0, 40.0),
            }

            if pd.isna(preco) or pd.isna(data) or categoria not in limites:
                return preco

            minimo, maximo = limites[categoria]
            preco_base = max(min(preco, maximo), minimo)
            mes = data.month
            fator = 1 + ((mes - 1) / 12) * 0.3
            return round(preco_base * fator, 2)

        df["Preco"] = df.apply(ajustar_preco_temporal, axis=1)
        df["Total_Vendas"] = df["Quantidade"] * df["Preco"]

        return df
