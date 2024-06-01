def greet(fx):
    def mfx(*args , **kwargs):
        print("Good morning")
        fx(*args , *kwargs)
        print("thank for using this")
    return mfx
        
#@greet(1)
# def hello():
#     print("Hello world")

# def hello():(2)
#     print("Hello world")


# hello()
# greet(hello)() - agar @greet nhi lagaya toh aisa kro

#agar greet me aise function pass krne hain jo arguments lete ho toh usme kwargs and args use krte hain parameter pass krne ke liye


@greet
def add(a,b):
    print(a+b) 
greet(add)(1,2) 

#args take argument in the form of tuples and **kwargs take in the form of dictionary
