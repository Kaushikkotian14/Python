try:
    a=int(input("Enter 1st no:"))
    b= int(input("Enter 2st no:"))
    result = a/b

except ZeroDivisionError as z:
    print(z)
    print("You cant divide by 0")

except ValueError as arg:
    print("Enter Valid Number")
    print(arg)

else:
    print("Everything going well")

finally:
    print("Finally close")
