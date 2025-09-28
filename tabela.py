import pandas as pd

# Carregando o dataset limpo
df_limpo = pd.read_csv("data/data_clean.csv")

# Recalculandoo Total_Vendas
df_limpo["Total_Vendas"] = df_limpo["Quantidade"] * df_limpo["Preço"]

# Total de vendas por prato
vendas_por_prato = (
    df_limpo.groupby("Prato")["Total_Vendas"].sum().sort_values(ascending=False)
)
prato_top = vendas_por_prato.idxmax()
valor_top = vendas_por_prato.max()

# Formatando a tabela
tabela = vendas_por_prato.reset_index()
tabela.columns = ["Produto", "Total de Vendas (R$)"]
print("\n Total de vendas por produto:\n")
print(
    tabela.to_string(
        index=False, formatters={"Total de Vendas (R$)": "R$ {:,.2f}".format}
    )
)

print(f"\n Produto mais lucrativo: {prato_top} com R$ {valor_top:,.2f} em vendas.")
