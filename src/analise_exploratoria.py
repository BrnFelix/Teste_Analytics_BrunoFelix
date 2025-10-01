import matplotlib.pyplot as plt
import seaborn as sns


class AnaliseExploratoria:
    def __init__(self, df):
        self.df = df.copy()
        self.df["AnoMes"] = self.df["Data"].dt.to_period("M")

    def vendas_mensais(self):
        vendas_mensais = self.df.groupby("AnoMes")["Total_Vendas"].sum()
        plt.figure(figsize=(12, 6))
        vendas_mensais.plot(kind="line", marker="o", color="teal")
        plt.title("Tendência de Vendas Mensais (2023)")
        plt.xlabel("Mês")
        plt.ylabel("Total de Vendas (R$)")
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def vendas_por_categoria(self):
        vendas_por_categoria = (
            self.df.groupby("Categoria")["Total_Vendas"].sum().sort_values()
        ).reset_index()

        plt.figure(figsize=(10, 6))
        ax = sns.barplot(
            data=vendas_por_categoria,
            x="Total_Vendas",
            y="Categoria",
            hue="Categoria",
            palette="viridis",
            dodge=False,
            legend=False,
        )
        for i, valor in enumerate(vendas_por_categoria["Total_Vendas"]):
            ax.text(valor + 5, i, f"R$ {valor:,.2f}", va="center", fontsize=10)
        plt.title("Vendas por Categoria")
        plt.xlabel("Total de Vendas (R$)")
        plt.ylabel("Categoria")
        plt.tight_layout()
        plt.show()

    def participacao_por_prato(self):
        vendas_por_prato = self.df.groupby("Prato")["Total_Vendas"].sum()
        plt.figure(figsize=(8, 8))
        plt.pie(
            vendas_por_prato,
            labels=vendas_por_prato.index,
            autopct="%1.1f%%",
            startangle=140,
            colors=sns.color_palette("pastel"),
        )
        plt.title("Participação dos Pratos nas Vendas")
        plt.axis("equal")
        plt.show()
