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

    # Define the SQL statements to create tables
    create_people_table_query = """
        CREATE TABLE IF NOT EXISTS people (
            ID SERIAL PRIMARY KEY,
            Year_Birth INT,
            Education VARCHAR(50),
            Marital_Status VARCHAR(50),
            Income FLOAT,
            Kidhome INT,
            Teenhome INT,
            Dt_Customer DATE,
            Recency INT,
            Complain INT
        )
    """

    create_product_table_query = """
        CREATE TABLE IF NOT EXISTS product (
            ID SERIAL PRIMARY KEY,
            MntWines FLOAT,
            MntFruits FLOAT,
            MntMeatProducts FLOAT,
            MntFishProducts FLOAT,
            MntSweetProducts FLOAT,
            MntGoldProds FLOAT
        )
    """

    create_place_table_query = """
        CREATE TABLE IF NOT EXISTS place (
            ID SERIAL PRIMARY KEY,
            NumWebPurchases INT,
            NumCatalogPurchases INT,
            NumStorePurchases INT,
            NumWebVisitsMonth INT
        )
    """

    create_promotion_table_query = """
        CREATE TABLE IF NOT EXISTS promotion (
            ID SERIAL PRIMARY KEY,
            NumDealsPurchases INT,
            AcceptedCmp3 INT,
            AcceptedCmp4 INT,
            AcceptedCmp5 INT,
            AcceptedCmp1 INT,
            AcceptedCmp2 INT,
            Response INT
        )
    """

    # Execute the SQL statements to create tables
    cursor.execute(create_people_table_query)
    cursor.execute(create_product_table_query)
    cursor.execute(create_place_table_query)
    cursor.execute(create_promotion_table_query)

    # Open the CSV file for reading
    csv_file = 'marketing_campaign.csv'

    # Define the SQL statements to insert data into the tables
    insert_people_query = """
        INSERT INTO people (ID, Year_Birth, Education, Marital_Status, Income, 
                            Kidhome, Teenhome, Dt_Customer, Recency, Complain)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    insert_product_query = """
        INSERT INTO product (MntWines, MntFruits, MntMeatProducts, 
                             MntFishProducts, MntSweetProducts, MntGoldProds)
        VALUES (%s, %s, %s, %s, %s, %s)
    """

    insert_place_query = """
        INSERT INTO place (NumWebPurchases, NumCatalogPurchases, 
                           NumStorePurchases,NumWebVisitsMonth)
        VALUES (%s, %s, %s, %s)
    """

    insert_promotion_query = """
        INSERT INTO promotion (NumDealsPurchases, AcceptedCmp3, AcceptedCmp4, 
                               AcceptedCmp5, AcceptedCmp1, AcceptedCmp2,
                               Response)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """

    # Open the CSV file and iterate over its rows to insert into the database
    with open(csv_file, 'r', newline='') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            try:
                # Convert date string to datetime.date object
                row[7] = convert_to_date(row[7])
                # Execute the SQL command for inserting into people table
                cursor.execute(insert_people_query, tuple(row[:10]))
                # Print inserted row for debugging
                print("Inserted row into people table:", tuple(row[:10]))

                # Execute the SQL command for inserting into product table
                cursor.execute(insert_product_query, tuple(row[10:16]))
                # Print inserted row for debugging
                print("Inserted row into product table:", tuple(row[10:16]))

                # Execute the SQL command for inserting into place table
                cursor.execute(insert_place_query, tuple(row[16:20]))
                # Print inserted row for debugging
                print("Inserted row into place table:", tuple(row[16:20]))

                # Execute the SQL command for inserting into promotion table
                cursor.execute(insert_promotion_query, tuple(row[20:]))
                # Print inserted row for debugging
                print("Inserted row into promotion table:", tuple(row[20:]))

            except Exception as e:
                print("Error inserting row:", e)
                conn.rollback()  # Rollback the transaction in case of an error

    # Commit the transaction
    conn.commit()

    print("Data has been successfully loaded into all tables.")

except psycopg.Error as e:
    print("Error connecting to PostgreSQL:", e)

finally:
    # Close the cursor and database connection
    cursor.close()
    conn.close()
