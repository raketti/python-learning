class Person:
  def __init__(self, name, age): # self can be what-ever
    self.name = name
    self.age = age

p1 = Person("Jaakko", 39)

print("Olen", p1.name, p1.age, "vuotta.")
print()

class Kaveri:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    
  def __str__(self): # defines what to return when the class object is a string
    return f"{self.name}({self.age})" # note the f for formatting

p2 = Kaveri("John", 36)

print(p2) 