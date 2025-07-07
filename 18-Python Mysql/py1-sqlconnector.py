import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password ="root",
    database="godigitaldb1"
)
print("Conected to mySql")
conn.close()