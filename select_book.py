import psycopg2

conn=psycopg2.connect(
    host="localhost",
    database="fastapi_db",
    user="postgres",
    password="nizam2815"

)

cur=conn.cursor()

cur.execute("SELECT *FROM books")
books=cur.fetchall()

for book in books:
    print(book)
cur.close()
conn.close()