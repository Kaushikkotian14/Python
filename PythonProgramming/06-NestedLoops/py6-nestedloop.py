for i in range(5):
    for j in range(5):
        if i == j or j==4-i:
            print(1,end=" ")
        else:
            print(7,end=" ")
    print()
