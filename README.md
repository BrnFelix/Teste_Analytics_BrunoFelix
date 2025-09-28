# 📊 Vendas Analytics

Projeto de simulação, limpeza e análise de dados de vendas de um restaurante.
A ideia é gerar um conjunto de dados fictício com pratos, tratar inconsistências e explorar as informações de forma visual e tabular para entender padrões de consumo e quais produtos têm melhor desempenho.

## ✨ Motivação

Esse teste proposto pela Quod foi um desafio interessante (que também alugou um triplex na minha cabeça  sobre como estruturá-lo haha) a fim de compreender a lógica do candidato para análise de dados. Dessa forma, eu quis simular um cenário real de restaurante, passando por todo o processo: gerar os dados, limpar, organizar, analisar e visualizar.
Também aproveitei para incrementar funcionalidades extras que não estavam propostas no desafio original, como boas práticas com testes unitários e pre-commit.
O foco foi criar algo que se parecesse com um caso do dia a dia, mas em um ambiente totalmente controlado.

## 🧠 Funcionalidades

Simulação de 100 registros de vendas com pratos variados;
Inserção proposital de dados nulos e duplicados para fins de limpeza;
Tratamento de dados: remoção de nulos, duplicatas e conversão de tipos;
Cálculo do total de vendas por produto;
Identificação do produto mais lucrativo;

Visualizações gráficas:
Tendência de vendas mensais;
Vendas por categoria gastronômica;
Participação percentual dos pratos;
Exibição tabular no terminal.

## 🗂 Estrutura do Projeto

```
data_first/
├── pytest.ini                    # Configuração de testes
├── data/
│   ├── data_clean.csv            # Dataset limpo gerado
│   └── relatorio_vendas.pdf      # Relatório PDF gerado
├── images/
│   ├── Gráfico de Tendência de Vendas Mensais.png
│   ├── Gráfico de Total de Vendas em Dinheiro Por Categoria.png
│   ├── Participação dos Pratos nas Vendas Totais.png
├── tests/
│   ├── test_simulador.py
│   ├── test_limpeza.py
│   └── test_analise.py
├── vendas_analytcs/
│   ├── __pycache__
│   ├── __init__.py
│   ├── analise_exploratoria.py  # Gráficos e análises visuais
│   ├── limpeza.py                # Tratamento de dados
│   ├── simulador.py              # Geração de dados simulados
├── pre-commit-config.yaml
├── graficos.py                   # Executa os gráficos
├── pytest.ini
├── README.md                     # Documentação do projeto
├── requirements.txt              # Dependências
└── tabela.py                     # Exibe a tabela de vendas no terminal
```




## ❓ Como executar 

1. Instale todas as dependências pendentes pelo terminal rodando o seguinte comando:
```
pip install -r requirements.txt
```
2. Gere os gráficos
```
python graficos.py
```

3. Exiba a tabela de vendas no terminal
```
python tabela.py
```

## ✅ Testes

Para rodar os testes unitários:
```
pytest tests/
```

## 📦 Controle de Qualidade

Este projeto utiliza:

flake8 para verificação de estilo;
black para formatação automática;
isort para organização de imports;
pre-commit para aplicar tudo antes de cada commit.

Para ativar:
```
pre-commit install
```

## 📈 Exemplos de Saída

Tabela no terminal:

    Total de vendas por produto:
    Produto        Total de Vendas (R$)
    Hambúrguer     R$ 5,066.06
    Sushi          R$ 4,528.00
    Feijoada       R$ 4,428.16
    Pizza          R$ 3,979.31


## 📈 Gráficos gerados:

Linha de Tendência de Venda Mensal
<img width="700" height="500" alt="Gráfico de Tendência de Vendas Mensais" src="https://github.com/user-attachments/assets/faa124c7-e591-46b7-9e64-6d843fed4df7" /> <br>

Lucro por Categoria

<img width="700" height="500" alt="Gráfico de Total de Vendas em Dinheiro Por Categoria" src="https://github.com/user-attachments/assets/c95e0380-347f-48d6-a953-cad21605f670" /> <br>


Percentual Vendido por Categoria
<img width="700" height="500" alt="Participação dos Pratos nas Vendas Totais" src="https://github.com/user-attachments/assets/c4a912dd-bbfa-43b0-baf8-37f6ef235e18" />
