def MattMult(x, y):
    return x*y

def MattDiv(x, y):
    if y == 0:
        return "Divide by Zero"
    else:
        return x/y
    
def MattAdd(x,y):
    return x+y

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def say_hello(self):
        print("Hello, my name is " + self.name + " and I am " + str(self.age) + " years old.")
