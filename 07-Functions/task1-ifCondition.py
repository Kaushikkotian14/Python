while (True):
    num1 = int(input("Enter number1:"))
    num2 = int(input("Enter number2:"))
    calc = input("Choose any one operation from(+,-,*,/):")

    if (calc == "+"):
        print("Addition:", num1 + num2)
    elif (calc == "-"):
        print("Subtraction:", num1 - num2)
    elif (calc == "*"):
        print("Multipliation:", num1 * num2)
    elif (calc == "/"):
        print("Division:", num1 / num2)
    else:
        print("Invalid")
    23