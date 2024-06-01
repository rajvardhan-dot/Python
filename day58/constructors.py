# class person:
#     def __init__(self):
#         print("hey my name is rajvardhan singh")
        
#     def info(self):
#         print(f"hey my name is {self.name} ")
  
   
# #//pehle object create kro    
# a = person()
# b = person()

# #agar changes krna hain toh kro
# b.name = "Ram"

# #method call kr diya
# b.info()

#************************#

class person:
    def __init__(self,n,o):
        print("hey my name is rajvardhan singh")
        self.name = n
        self.occ = o
        
    def info(self):
        print(f"hey my name is {self.name} ")

a = person("harry" , "developer")
b = person("ram" , "SDE")

a.info()
b.info()
