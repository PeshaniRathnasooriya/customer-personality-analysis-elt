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
    INSERT INTO promotion_response_demographics (Promotion_Campaign, 
    Age_Group, Education, Total_Customers, Accepted_Customers, Acceptance_Rate)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    
complaints_spending_campaign_response = """
    INSERT INTO complaints_spending_campaign_response (
        Complaint_Status,
        Avg_Spending_Wines,
        Avg_Spending_Fruits,
        Avg_Spending_Meat,
        Avg_Spending_Fish,
        Avg_Spending_Sweets,
        Avg_Spending_Gold,
        Avg_Acceptance_Campaign_3,
        Avg_Acceptance_Campaign_4,
        Avg_Acceptance_Campaign_5,
        Avg_Acceptance_Campaign_1,
        Avg_Acceptance_Campaign_2
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """   
    
children_teenagers_spending = """
    INSERT INTO children_teenagers_spending (
        Kidhome,
        Teenhome,
        Avg_Spending_Wines,
        Avg_Spending_Fruits,
        Avg_Spending_Meat,
        Avg_Spending_Fish,
        Avg_Spending_Sweets,
        Avg_Spending_Gold
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    
discount_purchases_overall_spending = """
    INSERT INTO discount_purchases_overall_spending (
        NumDealsPurchases,
        Total_Spending_Wines,
        Total_Spending_Fruits,
        Total_Spending_Meat,
        Total_Spending_Fish,
        Total_Spending_Sweets,
        Total_Spending_Gold,
        Avg_Acceptance_Campaign_3,
        Avg_Acceptance_Campaign_4,
        Avg_Acceptance_Campaign_5,
        Avg_Acceptance_Campaign_1,
        Avg_Acceptance_Campaign_2
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
 