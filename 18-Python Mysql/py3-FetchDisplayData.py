import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password ="root",
    database="godigitaldb1"
)

cursor =conn.cursor()

cursor.execute("Select * from student")
rows= cursor.fetchall()
for row in rows:
    print("ID:",row[0],"Name:",row[1])

conn.close()