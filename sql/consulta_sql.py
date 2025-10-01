import pandas as pd
from sqlalchemy import create_engine


def executar_consultas():
    # Criar engine com SQLAlchemy
    engine = create_engine(
        "mssql+pyodbc://localhost/Analytics?driver=ODBC+Driver+17+for+SQL+Server"
    )

    # Ler consultas do arquivo
    with open("sql/consultas_analise.sql", "r", encoding="utf-8") as f:
        queries = f.read().split(";")  # separa cada consulta

    # Executar e exibir cada consulta
    for i, query in enumerate(queries):
        query = query.strip()
        if query:
            try:
                print(f"\n Resultado da consulta {i+1}:")
                df = pd.read_sql(query, engine)
                print(df)
            except Exception as e:
                print(f"❌ Erro na consulta {i+1}: {e}")
