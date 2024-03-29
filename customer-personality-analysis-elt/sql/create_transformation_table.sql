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

CREATE TABLE IF NOT EXISTS promotion_response_demographics (
    Promotion_Campaign VARCHAR(20),
    Age_Group VARCHAR(20),
    Education VARCHAR(50),
    Total_Customers INT,
    Accepted_Customers INT,
    Acceptance_Rate FLOAT
);

CREATE TABLE IF NOT EXISTS discount_purchases_overall_spending (
    NumDealsPurchases INT,
    Total_Spending_Wines FLOAT,
    Total_Spending_Fruits FLOAT,
    Total_Spending_Meat FLOAT,
    Total_Spending_Fish FLOAT,
    Total_Spending_Sweets FLOAT,
    Total_Spending_Gold FLOAT,
    Avg_Acceptance_Campaign_3 FLOAT,
    Avg_Acceptance_Campaign_4 FLOAT,
    Avg_Acceptance_Campaign_5 FLOAT,
    Avg_Acceptance_Campaign_1 FLOAT,
    Avg_Acceptance_Campaign_2 FLOAT
);


CREATE TABLE IF NOT EXISTS complaints_spending_campaign_response (
    Complaint_Status VARCHAR(20),
    Avg_Spending_Wines FLOAT,
    Avg_Spending_Fruits FLOAT,
    Avg_Spending_Meat FLOAT,
    Avg_Spending_Fish FLOAT,
    Avg_Spending_Sweets FLOAT,
    Avg_Spending_Gold FLOAT,
    Avg_Acceptance_Campaign_3 FLOAT,
    Avg_Acceptance_Campaign_4 FLOAT,
    Avg_Acceptance_Campaign_5 FLOAT,
    Avg_Acceptance_Campaign_1 FLOAT,
    Avg_Acceptance_Campaign_2 FLOAT
);

CREATE TABLE IF NOT EXISTS children_teenagers_spending (
    Kidhome INT,
    Teenhome INT,
    Avg_Spending_Wines FLOAT,
    Avg_Spending_Fruits FLOAT,
    Avg_Spending_Meat FLOAT,
    Avg_Spending_Fish FLOAT,
    Avg_Spending_Sweets FLOAT,
    Avg_Spending_Gold FLOAT
);





