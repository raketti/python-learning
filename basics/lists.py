# Creating and modifying lists

mylist1 = ["one", "two", "three", "four"]
mylist2 = [1, 2, 3, 4]
mylist3 = [True, False, True]
print(mylist1)

print(len(mylist1))

print(type(mylist1))

mylist4 = list(("five", 'six', "seven"))
print(mylist4)

print(mylist1[1]) #Print second item on list

print(mylist1[-1]) #Print last item on list

print(mylist1[1:3]) #Print from the second to third item on the list

print(mylist1[:3]) #Start from the beginning

print(mylist2[-3:-1]) #Start range from the end

mylist2[1] = 5 # Change the second item on the list
print(mylist2)

mylist1[1:3] = ["apple", "orange"] # Change the second and third item on the list
print(mylist1)

mylist1[1:2] = ["pineapple", "banana"] # Change the second item with two new values on the list
print(mylist1)

mylist1[0:6] = ["watermelon"] # Change all values two a new value on the list
print(mylist1)

mylist1[1:2] = ["pineapple", "banana"] # Change the second item with two new values on the list
mylist1.insert(3, "apple")
print(mylist1)

mylist1.insert(4, "kiwi")
print(mylist1)

mylist1.append("carrot") #Add carrot to the end of the list
print(mylist1)

mylist1.extend(mylist2) # add mylist2 to the end of the mylist1
mylist3 = mylist1 + mylist2 # also adds lists 1 and 2 as list 3
print(mylist1)
print(mylist3)

mylist1.remove("pineapple")
print(mylist1)

print(mylist1[2:5])

mylist1.pop() #Removes the last item on the list
print(mylist1)


# del mylist2 #This will completely delete the list
# print(mylist2)
# commented out because we get an error

"""
Results in an error as it doesnt exist

  File "../lists.py", line 60, in <module>
    print(mylist2)
          ^^^^^^^
NameError: name 'mylist2' is not defined. Did you mean: 'mylist1'?
"""

mylist3.clear() #This will clear the list, but keep it
print(mylist3)

#From tis point on mylist2 is not defined and mylist3 is empty

#Print all items in a list
for x in mylist1:
    print(x)
    
#Let's loop through the list items by referring to their index number
for i in range(len(mylist1)):
    print(i)