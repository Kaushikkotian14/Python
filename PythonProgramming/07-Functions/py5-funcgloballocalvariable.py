x=100

def show_local():
    x=30
    print("local variable:",x)

def show_global():
    print("Global variable:", x)

def modify_global():
    global x
    x=x+50
    print("modifided global variable:", x)

show_global()
show_local()
modify_global()


