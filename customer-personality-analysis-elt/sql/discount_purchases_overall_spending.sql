SELECT
    NumDealsPurchases,
    SUM(MntWines) AS Total_Spending_Wines,
    SUM(MntFruits) AS Total_Spending_Fruits,
    SUM(MntMeatProducts) AS Total_Spending_Meat,
    SUM(MntFishProducts) AS Total_Spending_Fish,
    SUM(MntSweetProducts) AS Total_Spending_Sweets,
    SUM(MntGoldProds) AS Total_Spending_Gold,
    AVG(AcceptedCmp3) AS Avg_Acceptance_Campaign_3,
    AVG(AcceptedCmp4) AS Avg_Acceptance_Campaign_4,
    AVG(AcceptedCmp5) AS Avg_Acceptance_Campaign_5,
    AVG(AcceptedCmp1) AS Avg_Acceptance_Campaign_1,
    AVG(AcceptedCmp2) AS Avg_Acceptance_Campaign_2
FROM
    customer
GROUP BY
    NumDealsPurchases;
