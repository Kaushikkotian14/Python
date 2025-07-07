while (True):
    num1 = int(input("Enter number1:"))
    num2 = int(input("Enter number2:"))
    calc = input("Choose any one operation from(+,-,*,/):")

    match calc:
        case "+":
            print("Addition:", num1 + num2)
        case "-":
            print("Subtraction:", num1 - num2)
        case "*":
            print("Multipliation:", num1 * num2)
        case "/":
            print("Division:", num1 / num2)
        case _:
            print("Invalid")
