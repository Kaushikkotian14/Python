l=[12,23,66,34,45,66,77,88]
print(l)
n=len(l)
print("Length:",n)
l.append(60)
l.insert(0,5)
print("After inserting:",l)
l1=l.copy()
print("New created list:",l1)
n=l.count(66)
print("No. of times 66 found in list:",n)
l.remove(66)
print("After removing 66:",l)
