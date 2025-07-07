class myStudent:
    def __init__(self):
            self.sno=100
            self.sname="Kaushik"
            self.sub1="Physic"
            self.sub2 = "Maths"
    def display(mydata):
        print("Student ID:",mydata.sno)
        print("Student Name:", mydata.sname)
        print("Student Subject 1:", mydata.sub1)
        print("Student Subject 2:", mydata.sub2)

std=myStudent()
std.display()


