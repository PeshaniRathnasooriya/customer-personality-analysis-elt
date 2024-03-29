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
