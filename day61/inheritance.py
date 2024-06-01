#inheritance

class employee:
    def __init__(self,name , id):
        self.name = name
        self.id = id
    
    def showdetails(self):
        print(f"the name of employee: {self.id} is {self.name}")
        
        
e  = employee("rohan" , 420)
e.showdetails()


class programmer(employee):
    def showlanguage(self):
        print("the default language is python")

e2 = programmer("raj" , 26)
e2.showdetails()
e2.showlanguage()