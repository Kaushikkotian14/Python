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

def update_student(student_id,new_name):
    query="Update students Set name=%s where id =%s"
    values = (new_name,student_id)

    cursor.execute(query,values)
    conn.commit()
    print(f"\n Student ID {student_id} updated to name '{new_name}'.")

fetch_student()
update_student(2,"Ramesh")
fetch_student()
cursor.close()
conn.close()