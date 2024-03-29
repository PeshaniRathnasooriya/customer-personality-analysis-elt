SELECT
    Promotion_Campaign,
    Age_Group,
    Education,
    COUNT(*) AS Total_Customers,
    SUM(CASE WHEN Response = 1 THEN 1 ELSE 0 END) AS Accepted_Customers,
    AVG(CASE WHEN Response = 1 THEN 1 ELSE 0 END) AS Acceptance_Rate
FROM (
    SELECT
        CASE
            WHEN AcceptedCmp1 = 1 THEN 'Campaign_1'
            WHEN AcceptedCmp2 = 1 THEN 'Campaign_2'
            WHEN AcceptedCmp3 = 1 THEN 'Campaign_3'
            WHEN AcceptedCmp4 = 1 THEN 'Campaign_4'
            WHEN AcceptedCmp5 = 1 THEN 'Campaign_5'
            ELSE 'No_Acceptance'
        END AS Promotion_Campaign,
        CASE
            WHEN Year_Birth BETWEEN 1900 AND 1949 THEN '50s_and_older'
            WHEN Year_Birth BETWEEN 1950 AND 1959 THEN '50s'
            WHEN Year_Birth BETWEEN 1960 AND 1969 THEN '60s'
            WHEN Year_Birth BETWEEN 1970 AND 1979 THEN '70s'
            WHEN Year_Birth BETWEEN 1980 AND 1989 THEN '80s'
            ELSE '90s_and_younger'
        END AS Age_Group,
        Education,
        Response
    FROM
        customer
) AS subquery
GROUP BY
    Promotion_Campaign,
    Age_Group,
    Education
ORDER BY
    Promotion_Campaign,
    Age_Group,
    Education;
