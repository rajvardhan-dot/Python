a = [1,2,3]
b = [1,2,3]
print(a is b)#exact location of object(false)
print(a == b)#value of the object(True)

a = (1,2,3)
b = (1,2,3)
print(a is b)#exact location of object(True) bcoz tuple is immutable
print(a == b)#value of the object(True)

