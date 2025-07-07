def check_age(age):
    if age<18:
        raise ValueError("Not eligible for voting") #manually throw error
    else:
        print("Eligible for voting")

try:
    age=int(input("Enter Age:"))
    check_age(age)
except ValueError as e:
    print(e)
