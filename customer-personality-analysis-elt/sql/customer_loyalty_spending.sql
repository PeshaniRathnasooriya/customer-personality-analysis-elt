SELECT
    EXTRACT(DAY FROM AGE(CURRENT_DATE, Dt_Customer)) AS Days_Since_Enrollment,
    (MntWines + MntFruits + MntMeatProducts + MntFishProducts + MntSweetProducts + MntGoldProds) AS Total_Spending
FROM
    customer;

