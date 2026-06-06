import psycopg2

conn=psycopg2.connect(
    host="localhost",
    database="fastapi_db",
    user="postgres",
    password="nizam2815"

)

cur=conn.cursor()

cur.execute("INSERT INTO books(id,title,author,price)VALUES(1,'Fastapi_Basics','Alex',500)")
conn.commit()
print("Boook inserted successfully")