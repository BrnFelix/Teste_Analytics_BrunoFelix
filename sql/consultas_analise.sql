-- Total de vendas por produto e categoria
SELECT 
    Prato AS Produto,
    Categoria,
    SUM(Quantidade * Preco) AS Total_Vendas
FROM 
    vendas
GROUP BY 
    Prato, Categoria
ORDER BY 
    Total_Vendas DESC;

-- Produtos que venderam menos em junho de 2023
SELECT 
    Prato AS Produto,
    SUM(Quantidade * Preco) AS Total_Vendas_Junho
FROM 
    vendas
WHERE 
    MONTH(Data) = 6 AND YEAR(Data) = 2023
GROUP BY 
    Prato
ORDER BY 
    Total_Vendas_Junho ASC;

-- Total de vendas por categoria
SELECT 
    Categoria,
    SUM(Quantidade * Preco) AS Total_Vendas
FROM 
    vendas
GROUP BY 
    Categoria
ORDER BY 
    Total_Vendas DESC;

-- Tendência mensal de vendas
SELECT 
    FORMAT(Data, 'yyyy-MM') AS Mes,
    SUM(Quantidade * Preco) AS Total_Vendas
FROM 
    vendas
GROUP BY 
    FORMAT(Data, 'yyyy-MM')
ORDER BY 
    Mes;
