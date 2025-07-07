try:
    print("One")
    myData=[1,2,3,4,5]
    print("MyData:",myData)
    print("MyData:",myData[5])
    print("End")

except IndexError as arg:
    print("Some error")
    print(arg)

else:
    print("Everything going well")

