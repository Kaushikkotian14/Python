import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password ="root",
    database="godigitaldb1"
)
cursor =conn.cursor()

def fetch_student():
    cursor.execute("Select * from Student")
    rows=cursor.fetchall()
    print("\n----Students Record----\n")
    for row in rows:
        print("ID:",row[0],"Name:",row[1])
    print("-------------------------")
fetch_student()
cursor.close()
conn.close()