Use Analytics;

CREATE TABLE vendas (
    ID INT,
    Data DATE,
    Prato VARCHAR(50),
    Categoria VARCHAR(50),
    Quantidade INT,
    Preco FLOAT
);

SELECT COUNT(*) FROM vendas;