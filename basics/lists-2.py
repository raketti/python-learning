mylist1 = ["one", "two", "three", "four"]
i = 0
while i < len(mylist1):
    print(mylist1[i])
    i = i + 1
    
# Comprehension
print("Needs a line break!")

[print(x) for x in mylist1]

"""
The Syntax
newlist = [expression for item in iterable if condition == True]

The return value is a new list, leaving the old list unchanged.
"""

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print("New list: ", newlist)
print("Old list: ", fruits)

newlist2 = [x for x in range(10)]
print(newlist2)

newlist3 = [x for x in fruits]
print(newlist3)

# go through all items in the list
cars = ["volvo", "seat", "honda", "audi"]
print(cars)

carsNew = [x.capitalize() for x in cars] # Capitalize all items in the list
carsNew.sort() # Sort all items, defailt ascending
print(carsNew)
carsNew.sort(reverse=True) # Sort decending
print(carsNew)