import psycopg
from util import transformation_data_insertion_queries as tdiq

# Function to execute SQL queries from external files


def execute_sql_file(cursor, filename, fetch_result=False):
    with open(filename, 'r') as file:
        query = file.read()
        cursor.execute(query)
        if fetch_result:
            return cursor.fetchall()


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

    # Define the directory containing SQL transformation files
    sql_dir = "../sql/"

    # Example transformation: Demographic Influence on Income and Spending
    # Read and execute SQL queries from external files
    execute_sql_file(cursor, (sql_dir + 'create_transformation_table.sql'))
    file_names = ["demographic_income_spending", "customer_loyalty_spending", 
                  "complaints_spending_campaign_response"]
    for file in file_names:
        rows = execute_sql_file(
            cursor, (sql_dir + file + '.sql'), True)

        # SQL query to insert data into demographic_spending table
        insert_query = getattr(tdiq, file)

        # Insert each row into demographic_spending table
        for row in rows:
            cursor.execute(insert_query, row)

        # Commit the transaction
        conn.commit()

        print("Data transformations have been successfully executed for "
              + file+".")

except psycopg.Error as e:
    print("Error connecting to PostgreSQL:", e)

finally:
    # Close the cursor and database connection
    cursor.close()
    conn.close()
