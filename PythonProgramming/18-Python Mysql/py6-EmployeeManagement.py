import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="godigitaldb1"
)
cursor = conn.cursor()


def create_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS employee (id INT PRIMARY KEY, name VARCHAR(100), salary INT)")
    conn.commit()
    print("Table created successfully.")


def insert_record():
    id = int(input("Enter Employee ID: "))
    name = input("Enter Employee Name: ")
    salary = int(input("Enter Employee Salary: "))
    query = "INSERT INTO employee (id, name, salary) VALUES (%s, %s, %s)"
    values = (id, name, salary)
    cursor.execute(query, values)
    conn.commit()
    print("Inserted Successfully.")


def select_record():
    cursor.execute("SELECT * FROM employee")
    rows = cursor.fetchall()
    print("\n---- Employees Record ----\n")
    for row in rows:
        print("ID:", row[0], "| Name:", row[1], "| Salary:", row[2])
    print("---------------------------")


def update_record():
    emp_id = int(input("Enter Employee ID to update: "))
    new_name = input("Enter new name: ")
    new_salary = int(input("Enter new salary: "))
    query = "UPDATE employee SET name = %s, salary = %s WHERE id = %s"
    values = (new_name, new_salary, emp_id)
    cursor.execute(query, values)
    conn.commit()
    print("Record updated successfully.")


def delete_record():
    emp_id = int(input("Enter Employee ID to delete: "))
    cursor.execute("DELETE FROM employee WHERE id = %s", (emp_id,))
    conn.commit()
    print("Employee deleted successfully.")


while True:
    print("\nChoose your action:")
    print("1. Create Table\n2. Select Records\n3. Insert Record\n4. Update Record\n5. Delete Record\n6. Exit")
    choice = int(input("Enter your choice number: "))

    match choice:
        case 1:
            create_table()
        case 2:
            select_record()
        case 3:
            insert_record()
        case 4:
            update_record()
        case 5:
            delete_record()
        case 6:
            print("Exiting program.")
            break
        case _:
            print("Invalid choice. Try again.")
