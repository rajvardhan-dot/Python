# def avg(a,b):
#     print("the avg is",(a+b)/2)
    
# # avg(4,2)

# #default argument 
# def name(fname , mname = "var" , lname="dhan"):
#     print("Hello,",fname,mname,lname)
# name("raj")

# #keyword argument: key value mede skte hain
# def name(fname , mname , lname):
#     print("Hello",fname , mname , lname)
# name(mname = "var" ,lname = "dhan" , fname = "raj")

# #required argument 
# def name(fname , mname ,lname):
#     print("Hello",fname , mname , lname)
# name("raj","var","dhan")

# #arbitary argument:put start in front and you can pass the values in the form of tuples
# def name(*name):
#     print("Hello",name[0],name[1],name[2])
# name("james" , "raj" , "singh")

# #keyword arbitary argument
# def name(**name):
#     print("Hello,", name["fname"], name["mname"], name["lname"])
# name(mname = "Buchanan", lname = "Barnes", fname = "James")

# def name(fname , mname ,lname):
#     return "Hello," + fname + " " + mname + " " + lname
# print(name("raj","var" ,"dhan"))

# def avge(*numbers):
#     sum=0
#     for i in numbers:
#         sum = sum + i
#     print("avg is:",sum/len(numbers))
# avge(4,1,5,2,1)

def name(fname , lname):
    return fname + " " + lname
print (name("raj","singh"))
