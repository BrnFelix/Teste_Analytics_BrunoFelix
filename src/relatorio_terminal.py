class RelatorioTerminal:
    def __init__(self, df):
        self.df = df.copy()

    def imprimir_relatorio(self):
        self.df["Mes"] = self.df["Data"].dt.to_period("M")
        self.df["Total_Vendas"] = self.df["Quantidade"] * self.df["Preco"]

        vendas_por_prato = (
            self.df.groupby("Prato")["Total_Vendas"].sum().sort_values(ascending=False)
        )
        prato_top = vendas_por_prato.idxmax()
        valor_top = vendas_por_prato.max()

        tabela = vendas_por_prato.reset_index()
        tabela.columns = ["Produto", "Total de Vendas (R$)"]
        print("\n Total de vendas por produto:\n")
        print(
            tabela.to_string(
                index=False, formatters={"Total de Vendas (R$)": "R$ {:,.2f}".format}
            )
        )
        print(
            f"\n Produto mais lucrativo: {prato_top} com R$ {valor_top:,.2f} em vendas."
        )

        vendas_mensais = self.df.groupby("Mes")["Total_Vendas"].sum().sort_index()
        print("\n Tendência mensal de vendas:\n")
        print(
            vendas_mensais.to_frame().to_string(
                formatters={"Total_Vendas": "R$ {:,.2f}".format}
            )
        )

        variacao_preco = self.df.groupby("Prato")["Preco"].agg(["min", "max"])
        variacao_preco["Diferença"] = variacao_preco["max"] - variacao_preco["min"]
        print("\n Variação de preço por prato:\n")
        print(
            variacao_preco.to_string(
                formatters={
                    "min": "R$ {:,.2f}".format,
                    "max": "R$ {:,.2f}".format,
                    "Diferença": "R$ {:,.2f}".format,
                }
            )
        )
        prato_maior_variacao = variacao_preco["Diferença"].idxmax()
        valor_variacao = variacao_preco["Diferença"].max()
        print(
            f"\n Prato com maior variação de preço do início ao final do ano de 2023: {prato_maior_variacao} (+R$ {valor_variacao:,.2f})"
        )
