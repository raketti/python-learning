class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self): # function/method with a greeting text and object from Person class
        print("Hello, my name is " + self.name)
    # end def
    
p1 = Person("John", 36) # populate the class
p1.myfunc() # print the defined function with the data from the class