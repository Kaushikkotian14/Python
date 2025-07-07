try:
    print("One")
    a=10
    b=1
    c=a/b
    print("Result:",c)

    myData = [1, 2, 3, 4, 5]
    print("MyData:", myData)
    print("MyData:", myData[40])
    print("End")

except ZeroDivisionError:
    print("You cant divide by 0")

except IndexError as arg:
    print("Some error")
    print(arg)

else:
    print("Everything going well")

finally:
    print("Finally close")



