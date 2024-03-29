SELECT
    CASE
        WHEN Complain = 1 THEN 'Complained'
        ELSE 'Not Complained'
    END AS Complaint_Status,
    AVG(MntWines) AS Avg_Spending_Wines,
    AVG(MntFruits) AS Avg_Spending_Fruits,
    AVG(MntMeatProducts) AS Avg_Spending_Meat,
    AVG(MntFishProducts) AS Avg_Spending_Fish,
    AVG(MntSweetProducts) AS Avg_Spending_Sweets,
    AVG(MntGoldProds) AS Avg_Spending_Gold,
    AVG(AcceptedCmp3) AS Avg_Acceptance_Campaign_3,
    AVG(AcceptedCmp4) AS Avg_Acceptance_Campaign_4,
    AVG(AcceptedCmp5) AS Avg_Acceptance_Campaign_5,
    AVG(AcceptedCmp1) AS Avg_Acceptance_Campaign_1,
    AVG(AcceptedCmp2) AS Avg_Acceptance_Campaign_2
FROM
    customer
GROUP BY
    Complaint_Status;
