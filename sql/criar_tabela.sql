IF OBJECT_ID('vendas', 'U') IS NOT NULL
    DROP TABLE vendas;

CREATE TABLE vendas (
    ID INT PRIMARY KEY,
    Data DATE,
    Prato VARCHAR(100),
    Categoria VARCHAR(50),
    Quantidade INT,
    Preco FLOAT,
    Total_Vendas FLOAT
);
