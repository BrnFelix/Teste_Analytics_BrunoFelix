import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import random
from datetime import datetime, timedelta


# 1. Simulação do Dataset
np.random.seed(42) # Para gerar valores aleatórios e fixos, para facilitar na análise dos dados
random.seed(42)

pratos = ['Feijoada', 'Hambúrguer', 'Pizza', 'Salada Grega', 'Sushi', 'Lasanha', 'Tiramisu', 'Suco Natural']
categorias = {
    'Feijoada': 'Prato Principal',
    'Hambúrguer': 'Prato Principal',
    'Pizza': 'Prato Principal',
    'Salada Grega': 'Entrada',
    'Sushi': 'Prato Principal',
    'Lasanha': 'Prato Principal',
    'Tiramisu': 'Sobremesa',
    'Suco Natural': 'Bebida'
}

def gerar_data():
    start = datetime(2023, 1, 1)
    end = datetime(2023, 12, 31)
    return start + timedelta(days=random.randint(0, 364))

dados = []
for i in range(1, 101):  # Inserindo 100 registros
    prato = random.choice(pratos)
    categoria = categorias[prato]
    quantidade = random.randint(1, 10)
    preco = round(random.uniform(10, 120), 2)
    data = gerar_data()
    dados.append([i, data, prato, categoria, quantidade, preco])

df = pd.DataFrame(dados, columns=['ID', 'Data', 'Prato', 'Categoria', 'Quantidade', 'Preço'])

# 2. Inserindo valores null e linhas duplicadas para fazer o tratamento depois
df.loc[5, 'Prato'] = np.nan
df.loc[10, 'Preço'] = np.nan
df.loc[13, 'Categoria'] = np.nan
df.loc[20, 'Quantidade'] = np.nan
df.loc[29, 'Data'] = np.nan
df.loc[30, 'Categoria'] = np.nan
df.loc[33, 'Prato'] = np.nan
df.loc[47, 'Quantidade'] = np.nan
df.loc[65, 'Data'] = np.nan
df.loc[83, 'Quantidade'] = np.nan

# Duplicatas múltiplas
df = pd.concat([df, df.iloc[[3, 8, 12, 3]]], ignore_index=True)

# 3. Tratando os Dados
df.dropna(inplace=True)  # Remove valores faltantes
df.drop_duplicates(inplace=True)  # Remove linhas iguais
df['Data'] = pd.to_datetime(df['Data'])
df['Quantidade'] = df['Quantidade'].astype(int)
df['Preço'] = df['Preço'].astype(float)

# 4. Salvando o dataset limpo
df.to_csv('data_clean.csv', index=False)

# 5. Análises utilzando o dataset totalmente limpo
df['Total_Vendas'] = df['Quantidade'] * df['Preço']
vendas_por_prato = df.groupby('Prato')['Total_Vendas'].sum().sort_values(ascending=False)
prato_top = vendas_por_prato.idxmax()
valor_top = vendas_por_prato.max()

# 6. Resultados

print("Tabela com as informações:")
#print(df)

print(f"\n#####################")

print(f"\nTotal de vendas por prato:")
#print(vendas_por_prato)
#print(f"\n Prato mais lucrativo: {prato_top} (R$ {valor_top:.2f})")



# ------- Análise exploratória -------------


# Agrupando por mês
df['AnoMes'] = df['Data'].dt.to_period('M')
vendas_mensais = df.groupby('AnoMes')['Total_Vendas'].sum()

# Gráfico de linha
plt.figure(figsize=(12, 6))
vendas_mensais.plot(kind='line', marker='o', color='teal')
plt.title('📊 Tendência de Vendas Mensais no Restaurante (2023)', fontsize=14)
plt.xlabel('Mês')
plt.ylabel('Total de Vendas (R$)')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# Total de vendas por categoria
vendas_por_categoria = df.groupby('Categoria')['Total_Vendas'].sum().sort_values()

plt.figure(figsize=(10, 6))
ax = sns.barplot(x=vendas_por_categoria.values, y=vendas_por_categoria.index, palette='viridis')

# Adicionando os valores exatos nas barras
for i, valor in enumerate(vendas_por_categoria.values):
    ax.text(valor + 5, i, f'R$ {valor:,.2f}', va='center', fontsize=10)

plt.title('💰 Total de Vendas por Categoria Gastronômica')
plt.xlabel('Total de Vendas (R$)')
plt.ylabel('Categoria')
plt.tight_layout()
plt.show()

vendas_por_prato_pct = df.groupby('Prato')['Total_Vendas'].sum()
plt.figure(figsize=(8, 8))
plt.pie(vendas_por_prato_pct, labels=vendas_por_prato_pct.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette('pastel'))
plt.title('🍕 Participação dos Pratos nas Vendas Totais')
plt.axis('equal')
plt.show()

df['AnoMes'] = df['Data'].dt.to_period('M')
vendas_mensais = df.groupby('AnoMes')['Total_Vendas'].sum()

