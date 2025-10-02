# 📊 Vendas Analytics

Projeto de simulação, limpeza e análise de dados de vendas de um restaurante.
A ideia é gerar um conjunto de dados fictício com pratos, tratar inconsistências e explorar as informações de forma visual e tabular para entender padrões de consumo e quais produtos têm melhor desempenho.

## ✨ Motivação

Esse teste proposto pela Quod foi um desafio interessante (que também alugou um triplex na minha cabeça  sobre como estruturá-lo haha) a fim de compreender a lógica do candidato para análise de dados. Dessa forma, eu quis simular um cenário real de restaurante, passando por todo o processo: gerar os dados, limpar, organizar, analisar e visualizar.
Também aproveitei para incrementar funcionalidades extras que não estavam propostas no desafio original, como boas práticas com testes unitários e uma análise com dashboards utilizando a ferramenta PowerBI.
O foco foi criar algo que se parecesse com um caso do dia a dia, mas em um ambiente totalmente controlado.

## 🧠 Funcionalidades

Simulação de 100 registros de vendas com pratos variados;
Inserção proposital de dados nulos e duplicados para fins de limpeza;
Tratamento de dados: remoção de nulos, duplicatas e conversão de tipos;
Cálculo do total de vendas por produto;
Identificação do produto mais lucrativo;
Persistência dos dados em banco SQL Server;
Execução de consultas analíticas via SQLAlchemy.

Visualizações gráficas:
Tendência de vendas mensais;
Vendas por categoria gastronômica;
Participação percentual dos pratos;
Exibição tabular no terminal.

## 🗂 Estrutura do Projeto

```
data_first/
├── .pytest_cache              # Configuração de testes
├── config
│   ├── pytest.ini
├── data/
│   ├── data_clean.csv            # Dataset limpo gerado
├── PowerBI/                      # Exibição em png do PowerBI
│   ├── Dados Brutos.png
│   ├── Dados Tratados.png
│   ├── Dashboard Pronto.png
│   ├── Dashboard_Vendas.pbix
│   └── vendas_corrigido.csv
├── reports/                        # Imagens dos gráficos gerados
│   ├── Porcentagem de Vendas por Prato.png
│   ├── Vendas Mensais.png
│   └── Vendas Por Categoria.png
├── sql/                            # Parte que integra o Python ao Banco de Dados
│   ├── __pycache__
│   ├── consulta_sql.py
│   ├── consultas_analise.sql
│   ├── criar_tabela.sql
│   ├── database.py
│   ├── graficos.py
│   └── SQLQuery1.sql
├── src/                            # Pasta responsável pelas principais tarefas
│   ├── __pycache__
│   ├── __init__.py
│   ├── analise_exploratoria.py
│   ├── limpeza.py
│   ├── pipeline.py
│   ├── relatorio_terminal.py
│   └── simulador.py
├── tests                           # Pasta Responsável pelos testes unitários
│   ├── __pycache__
│   ├── test_analise.py
│   ├── test_limpeza.py
│   └── test_simulador.py          
├── main                          # Arquivo principal
├── README.md                     # Documentação do projeto
└── requirements.txt              # Dependências
 
```




## ❓ Como executar 

1. Instale todas as dependências pendentes pelo terminal rodando o seguinte comando:
```
pip install -r requirements.txt
```

2. Vá até o arquivo main.py e rode o código

## ✅ Testes

Para rodar os testes unitários:
```
pytest tests/
```


## 📈 Saída

Tabela no terminal:

    Total de vendas por produto:
    Produto        Total de Vendas (R$)
    Hambúrguer     R$ 5,066.06
    Sushi          R$ 4,528.00
    Feijoada       R$ 4,428.16
    Pizza          R$ 3,979.31

Produto mais lucrativo: Hambúrguer com R$ 5,115.74 em vendas.

 
Tendência mensal de vendas:

        Mes       Total_Vendas
        2023-01  R$ 3,586.35
        2023-02  R$ 2,383.13
        2023-03    R$ 376.74
        2023-04  R$ 1,457.76
        2023-05  R$ 1,526.94
        2023-06  R$ 1,559.89
        2023-07  R$ 1,556.62
        2023-08  R$ 2,967.12
        2023-09    R$ 415.54
        2023-10  R$ 4,912.64
        2023-11  R$ 3,692.96
        2023-12  R$ 2,747.46

Variação de preço por prato:

                min      max      Diferença
        Prato
        Feijoada     R$ 39.84 R$ 100.00  R$ 60.16
        Hambúrguer   R$ 38.06  R$ 98.00  R$ 59.94
        Lasanha      R$ 31.93  R$ 94.00  R$ 62.07
        Pizza        R$ 33.75 R$ 100.00  R$ 66.25
        Salada Grega R$ 22.26  R$ 51.00  R$ 28.74
        Suco Natural R$ 25.62  R$ 30.63   R$ 5.01
        Sushi        R$ 37.89 R$ 102.00  R$ 64.11
        Tiramisu     R$ 12.30  R$ 51.00  R$ 38.70

Prato com maior variação de preço do início ao final do ano de 2023: Pizza (+R$ 66.25)

Resultado da consulta 1 (Total de vendas por produto e categoria):

                Produto        Categoria  Total_Vendas
        0    Hambúrguer  Prato Principal       5115.74
        1      Feijoada  Prato Principal       4810.32
        2         Sushi  Prato Principal       4308.37
        3         Pizza  Prato Principal       4211.96
        4       Lasanha  Prato Principal       3827.09
        5  Salada Grega          Entrada       2778.80
        6      Tiramisu        Sobremesa       1232.85
        7  Suco Natural           Bebida        898.02


Resultado da consulta 2  (Produtos que venderam menos em junho de 2023):

        Produto           Total_Vendas_Junho
        0       Sushi              113.67
        1     Lasanha              182.65
        2       Pizza              236.25
        3    Feijoada              270.00
        4  Hambúrguer              757.32


Resultado da consulta 3 (Total de vendas por categoria):

                Categoria  Total_Vendas
        0  Prato Principal      22273.48
        1          Entrada       2778.80
        2        Sobremesa       1232.85
        3           Bebida        898.02


Resultado da consulta 4 (Tendência mensal de vendas):

                Mes  Total_Vendas
        0   2023-01       3586.35
        1   2023-02       2383.13
        2   2023-03        376.74
        3   2023-04       1457.76
        4   2023-05       1526.94
        5   2023-06       1559.89
        6   2023-07       1556.62
        7   2023-08       2967.12
        8   2023-09        415.54
        9   2023-10       4912.64
        10  2023-11       3692.96
        11  2023-12       2747.46

## 📈 Gráficos gerados:

Linha de Tendência de Venda Mensal
<img width="800" height="500" alt="Gráfico de Tendência de Vendas Mensais" src="https://github.com/user-attachments/assets/faa124c7-e591-46b7-9e64-6d843fed4df7" /> <br>

Lucro por Categoria

<img width="800" height="500" alt="Gráfico de Total de Vendas em Dinheiro Por Categoria" src="https://github.com/user-attachments/assets/c95e0380-347f-48d6-a953-cad21605f670" /> <br>


Percentual Vendido por Categoria
<img width="800" height="500" alt="Participação dos Pratos nas Vendas Totais" src="https://github.com/user-attachments/assets/c4a912dd-bbfa-43b0-baf8-37f6ef235e18" />


📊 Análise com Power BI

No dia a dia de quem trabalha com dados, não basta só tratar a base — é preciso também organizar e mostrar as informações de um jeito que faça sentido. Com essa ideia, peguei o arquivo data_clean.csv e criei outro chamado vendas_corrigido.csv.

A única diferença foi que ajustei a formatação das colunas preco e total_vendas, porque o Power BI não estava entendendo direito os valores. Depois de quebrar a cabeça o dia todo tentando resolver direto no Power BI, essa foi a forma mais prática de corrigir o problema.

🔑 Indicadores que encontrei

R$ 59,56 → preço médio por prato

R$ 27,18 mil → faturamento total em 2023

90 → total de pedidos feitos

8 → quantidade de pratos diferentes no cardápio

4 → categorias de produtos (entrada, prato principal, sobremesa e bebida)

📈 Algumas análises legais

Faturamento dos Top Pratos: por exemplo, só o Hambúrguer trouxe mais de R$ 5,12 mil.

Tendência Mensal de Faturamento: dá pra ver bem os picos e quedas de receita mês a mês.

Pedidos por Prato: mostra a distribuição de vendas entre os itens do cardápio (Salada Grega, Pizza, Feijoada etc.).

💰 Preços por categoria

Prato Principal → média de ~R$ 60

Sobremesas → média de ~R$ 40

Entradas e Bebidas → ficam em valores intermediários

📌 Conclusão

Esses indicadores ajudam a ter uma visão bem clara do restaurante: quais pratos vendem mais, quais trazem mais dinheiro, como o faturamento varia ao longo do tempo.
No fim, esse tipo de análise é o que apoia decisões estratégicas, e ainda deixa os dados bem mais interessantes de olhar no Power BI. 

