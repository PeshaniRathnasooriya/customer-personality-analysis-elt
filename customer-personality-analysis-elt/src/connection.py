import psycopg2

try:
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="peshani",
        host="localhost",
        port="5432"
    )
    print("Connected to the database")
except psycopg2.Error as e:
    print(f"Error connecting to the database: {e}")