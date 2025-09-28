import pandas as pd

def limpar_dados(df):
    df = df.dropna()
    df = df.drop_duplicates()
    df['Data'] = pd.to_datetime(df['Data'])
    df['Quantidade'] = df['Quantidade'].astype(int)
    df['Preço'] = df['Preço'].astype(float)
    df['Total_Vendas'] = df['Quantidade'] * df['Preço']
    return df