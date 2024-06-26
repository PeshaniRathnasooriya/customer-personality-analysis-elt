SELECT
    Marital_Status,
    Education,
    AVG(Income) AS Avg_Annual_Income,
    AVG(MntWines) AS Avg_Spending_Wines,
    AVG(MntFruits) AS Avg_Spending_Fruits,
    AVG(MntMeatProducts) AS Avg_Spending_Meat,
    AVG(MntFishProducts) AS Avg_Spending_Fish,
    AVG(MntSweetProducts) AS Avg_Spending_Sweets,
    AVG(MntGoldProds) AS Avg_Spending_Gold
FROM
    customer
GROUP BY
    Marital_Status,
    Education;
