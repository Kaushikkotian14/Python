def say_hello():
    return "Hello"

def say_gooodbye():
    return "Good Bye"

def say_thankyou():
    return "Thank you"

def default_message():
    return "Invalid Choice"

choice = int(input("Enter your choice (1.Hello 2.Good Bye 3.Thank You):"))

match choice:
    case 1:
        print(say_hello())

    case 2:
        print(say_gooodbye())

    case 3:
        print(say_thankyou())

    case _:
        print(default_message())