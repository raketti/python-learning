# basic comparison and printing strings
if 5 > 2:
 print("Five is greater than two!")
if 2 < 5:
 print("Two is less than five!")

# variables and printing
x = 4
y = 2
print("x =", x)
print("y =", y)

# variable types
a = "banaani"
b = 1

print(type(a))
print(type(b))

# naming variables
firstVariable = "Tulkku"
secondVariable = "Tintti"

# defining multiple variables
c, d, e = "Mikkeli", "Makkeli", "Mokkeli"
print(c, d, e)
print(d)
print(e)

# sum, and other math functions
print(x + y)
print(x * y)
print(x / y)

juttu = "Awesome"
def myfunc():
    print("This is " + juttu)
myfunc()

# changing a global variable inside a function
def youfunc():
    x = int(8)
    y = int(4)
    print(x + y)
    print(x * y)
    print(x / y)
youfunc()

# changing a global variable inside a function
def wefunc():
    global x
    global y
    x = "Semmottis"
    y = "Tämmöttis"
    print(x, "ja", y)
wefunc()

print(x, "ja ehkä", y)

# get the n:th number on the string - NB! Counting starts from zero
teksti = "Teksti"
print(teksti[2])

# go through all letters in string
for x in "viinirypäle":
    print(x)

# Count the length of the string
tekstiMuuttuja = "Jonkun verran tekstiä ja sitten lasketaan."
print(len(tekstiMuuttuja)) # This came out as 42 by accident, I swear!

# Check if a specific string is in the variable string - returns a boolean
teksti = "Lilleri lalleri laudalla makasi."
print("lauda" in teksti)

# Same with an if
teksti2 = "Mukkelis makkelis mukelo meni."
if "makkelis" in teksti2:
    print("Jeppistä! Siellä on makkelis!")

if "jumprahuitti" not in teksti2:
    print("Hops! Ei ole jumprahuittia!")

# Check True or False / NB! Zero will return False as boolean
print(bool("Hello"))
print(bool(0))
print(bool(1))