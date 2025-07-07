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

class Manager(Employee):
    def __init__(s,name,age,emp_id,salary,team_size,project_name):
        Employee.__init__(s,name,age,emp_id,salary)
        s.team_size=team_size
        s.project_name=project_name

    def display(s):
        super().display()
        print("Team Size:{} Project Name: {}".format(s.team_size,s.project_name))

m1 = Manager("Kaushik",22,1234,23000,23,"AIDS")
m1.display()

e1 = Employee("Raj",25,456,40000)
e1.display()