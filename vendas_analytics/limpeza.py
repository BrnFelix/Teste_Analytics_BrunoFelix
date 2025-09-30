import pandas as pd


def limpar_dados(df):
    df = df.dropna()
    df = df.drop_duplicates()
    df["Data"] = pd.to_datetime(df["Data"])
    df["Quantidade"] = df["Quantidade"].astype(int)
    df["Preco"] = df["Preco"].astype(float)
    df["Total_Vendas"] = df["Quantidade"] * df["Preco"]
    return df
