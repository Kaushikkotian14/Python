class Person:
    def __init__(s,name,age):
        s.name = name
        s.age = age
    def display(s):
        print("Name {} and age {}".format(s.name,s.age))

class Employee(Person):
    def __init__(s,name,age,emp_id,salary):
        Person.__init__(s,name,age)
        s.emp_id = emp_id
        s.salary = salary

    def display(s):
        super().display()
        print("Employee id:{} Salary: {}".format(s.emp_id,s.salary))

e1 = Employee("Kaushik",22,1234,23000)
e1.display()