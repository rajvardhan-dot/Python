# #MAP
def cube(x):
    return x*x*x

# print(cube(5))

l = [1,2,3,4,5]
# # newl = []
# # for item in l:
# #     newl.append(cube(item))

newl = list(map(cube,l))

print(newl) 

#FILTER:
l = [1,2,3,4,5]
def filter_fn(a):
    return a>2

newll = list(filter(filter_fn, l))
print(newll)
 
from functools import reduce
#functools is a module in python from which we will export the reduce function
def add(x,y):
    return x+y
numbers = [1,2,3,4,5]
sum = reduce(add , numbers)
print(sum)

