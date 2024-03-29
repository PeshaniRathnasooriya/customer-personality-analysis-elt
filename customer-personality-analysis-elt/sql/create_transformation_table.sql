CREATE TABLE IF NOT EXISTS demographic_spending (
    Marital_Status VARCHAR(50),
    Education VARCHAR(50),
    Avg_Annual_Income FLOAT,
    Avg_Spending_Wines FLOAT,
    Avg_Spending_Fruits FLOAT,
    Avg_Spending_Meat FLOAT,
    Avg_Spending_Fish FLOAT,
    Avg_Spending_Sweets FLOAT,
    Avg_Spending_Gold FLOAT
);

CREATE TABLE IF NOT EXISTS customer_loyalty_spending (
    Days_Since_Enrollment INT,
    Total_Spending FLOAT
);

CREATE TABLE IF NOT EXISTS complaints_spending_campaign_response (
    Promotion_Campaign VARCHAR(20),
    Age_Group VARCHAR(20),
    Education VARCHAR(50),
    Total_Customers INT,
    Accepted_Customers INT,
    Acceptance_Rate FLOAT
);




