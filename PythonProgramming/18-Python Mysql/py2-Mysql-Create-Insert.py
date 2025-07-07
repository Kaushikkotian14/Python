import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password ="root",
    database="godigitaldb1"
)

cursor =conn.cursor()

cursor.execute("Create table if not exists student(id INT, Name VARCHAR(100))")

cursor.execute("insert into student (id,name) values (1,'Raj')")
cursor.execute("insert into student (id,name) values (2,'Ram')")
conn.commit()
print("Table has created and data is inserted")

conn.close()