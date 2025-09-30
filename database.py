import pandas as pd
import pyodbc

# Conexão com o sql server
conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=Analytics;Trusted_Connection=yes;"
)
cursor = conn.cursor()

# Executar script sql de criação da tabela
with open("sql/criar_tabela.sql", "r", encoding="utf-8") as f:
    cursor.execute(f.read())
    conn.commit()

# Carregar CSV
df = pd.read_csv("data/data_clean.csv")

# Inserir dados
for _, row in df.iterrows():
    cursor.execute(
        """
        INSERT INTO vendas (ID, Data, Prato, Categoria, Quantidade, Preco)
        VALUES (?, ?, ?, ?, ?, ?)
    """,
        row["ID"],
        row["Data"],
        row["Prato"],
        row["Categoria"],
        row["Quantidade"],
        row["Preco"],
    )

conn.commit()
cursor.close()
conn.close()
print("Dados inseridos com sucesso!")
