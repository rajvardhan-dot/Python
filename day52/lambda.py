# def double(X):
#     return X*2



double = lambda x : x*2
cube = lambda x : x*x*x
avg = lambda x,y:(x*y)/2



print(double(5))
print(cube(5))
print(avg(2,4))

#passing function as an argument
def appl(fx , value):
    return 6 + fx(value)
print(appl(cube,2))

