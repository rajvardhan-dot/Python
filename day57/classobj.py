class person:
    name = "raj"
    occupation = "SDE"
    networth = 10
    #method
    def info(self):
        print(f"{self.name} is a {self.occupation}")
    
a = person()
b = person()
c = person()

a.name = "litika"
a.occupation = "electrical"

b.name = "shubh"
b.occupation = "tester"

a.info()
b.info()
c.info()



b