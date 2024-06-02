#in python we have dir, dict, and help  built function fucntion we have

x = [1,2,3]
print(dir(x))#to get to know about each and every method

print(x.__add__)


#dict
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("John", 30)
print(p.__dict__)  # Output: {'name': 'John', 'age': 30}

#help():
help(str)

