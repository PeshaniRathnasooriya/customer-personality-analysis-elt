demographic_income_spending = """
    INSERT INTO demographic_spending (
        Marital_Status,
        Education,
        Avg_Annual_Income,
        Avg_Spending_Wines,
        Avg_Spending_Fruits,
        Avg_Spending_Meat,
        Avg_Spending_Fish,
        Avg_Spending_Sweets,
        Avg_Spending_Gold
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

customer_loyalty_spending = """
    INSERT INTO customer_loyalty_spending (Days_Since_Enrollment,
                                           Total_Spending)
    VALUES (%s, %s)
    """
    
promotion_response_demographics = """
    INSERT INTO complaints_spending_campaign_response (Promotion_Campaign, 
    Age_Group, Education, Total_Customers, Accepted_Customers, Acceptance_Rate)
    VALUES (%s, %s, %s, %s, %s, %s)
    """