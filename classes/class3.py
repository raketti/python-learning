class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
    
  def printname(self): # create a functions/method
    print(self.firstname, self.lastname)

class Student(Person): # inherit the Person class to Student
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year
    
  def welcome(self): # create a welcoming text function/method
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

s = Student("Mike", "Tyson", 2010)
s.welcome()
print()

p = Person("John", "Doe")
p.printname()