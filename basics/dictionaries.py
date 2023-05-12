mydic = {
    # key : value
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1984
}

print(mydic)
print(mydic["brand"])

#Print the dict key values
print(mydic.keys())

# Add color to the dict
mydic["color"] = "white"
print(mydic.keys())

# Same thing

x = mydic.keys() # Now we can use the variable x instead
print(x)
#mydic.popitem() # Removes the last item in the dict
#print(x)

""" This will delete only one key """
# del mydic["model"]

""" This will delete the whole dict """
# del mydic

# Print key names
for x in mydic:
    print(x)
    
# Usink keys
for x in mydic.keys():
    print(x)
    
# Print key values
for x in mydic:
    print(mydic[x])

# Using values
for x in mydic.values():
    print(x)
    
# Copy the dict to a new one
newdic = mydic.copy() # where_to_copy = what_to_copy.copy()
print(newdic)

myfamily = {
  "child1" : {
    "name" : "Julius",
    "year" : 2014
  },
  "child2" : {
    "name" : "Melissa",
    "year" : 2016
  },
  "child3" : {
    "name" : "Amanda",
    "year" : 2018
  }
}

for x in myfamily.values():
    print(x)