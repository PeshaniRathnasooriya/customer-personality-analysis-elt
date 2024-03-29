import psycopg
import csv
import datetime

# Function to convert date string to datetime.date object


def convert_to_date(value):
    return datetime.datetime.strptime(value, '%m/%d/%Y').date()


try:
    # Database connection information
    dbname = "postgres"
    user = "postgres"
    password = "peshani"
    host = "localhost"
    port = "5432"

    # Connect to the PostgreSQL database
    conn = psycopg.connect(dbname=dbname, user=user,
                           password=password, host=host, port=port)

    # Create a cursor object using the cursor() method
    cursor = conn.cursor()

    # Define the SQL statement to create the customer table
    create_table_query = """
        CREATE TABLE IF NOT EXISTS customer (
            ID SERIAL PRIMARY KEY,
            Year_Birth INT,
            Education VARCHAR(50),
            Marital_Status VARCHAR(50),
            Income FLOAT,
            Kidhome INT,
            Teenhome INT,
            Dt_Customer DATE,
            Recency INT,
            Complain INT,
            MntWines FLOAT,
            MntFruits FLOAT,
            MntMeatProducts FLOAT,
            MntFishProducts FLOAT,
            MntSweetProducts FLOAT,
            MntGoldProds FLOAT,
            NumWebPurchases INT,
            NumCatalogPurchases INT,
            NumStorePurchases INT,
            NumWebVisitsMonth INT,
            NumDealsPurchases INT,
            AcceptedCmp3 INT,
            AcceptedCmp4 INT,
            AcceptedCmp5 INT,
            AcceptedCmp1 INT,
            AcceptedCmp2 INT,
            Response INT
        )
    """

    # Execute the SQL statement to create the customer table
    cursor.execute(create_table_query)

    # Open the CSV file for reading
    csv_file = 'marketing_campaign.csv'

    # Define the SQL statement to insert data into the customer table
    insert_query = """
        INSERT INTO customer (ID, Year_Birth, Education, Marital_Status, 
                              Income,Kidhome,Teenhome, Dt_Customer, Recency, 
                              Complain,MntWines,MntFruits,MntMeatProducts,
                              MntFishProducts,MntSweetProducts,MntGoldProds,NumWebPurchases,NumCatalogPurchases, 
                              NumStorePurchases, NumWebVisitsMonth,
                              NumDealsPurchases,AcceptedCmp3,AcceptedCmp4, 
                              AcceptedCmp5, AcceptedCmp1,AcceptedCmp2, 
                              Response)
        VALUES (%s, %s, %s, %s, %s, 
                %s,%s, %s, %s, %s,
                %s,%s, %s, %s, 
                %s, %s,%s,
                %s, %s, 
                %s, %s, %s,
                %s, %s, %s, 
                %s, %s)
    """

    # Open the CSV file and iterate over its rows to insert into the database
    with open(csv_file, 'r', newline='') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            print(row)  # Add this line for debugging
            try:
                # Convert date string to datetime.date object
                row[7] = convert_to_date(row[7])
                # Execute the SQL command
                cursor.execute(insert_query, row)
            except Exception as e:
                print("Error inserting row:", e)
                conn.rollback()  # Rollback the transaction in case of an error

    # Commit the transaction
    conn.commit()

    print("Data has been successfully loaded into the customer table.")

except psycopg.Error as e:
    print("Error connecting to PostgreSQL:", e)

finally:
    # Close the cursor and database connection
    cursor.close()
    conn.close()
