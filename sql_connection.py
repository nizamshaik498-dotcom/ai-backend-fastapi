import psycopg2

conn=psycopg2.connect(
    host="localhost",
    database="fastapi_db",
    user="postgres",
    password="nizam2815"
)

print("Database connection successful!")
conn.close()