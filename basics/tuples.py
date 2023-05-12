# Tuples need the comma to be created
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple, a string
thistuple = ("apple")
print(type(thistuple))

"""
Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
"""

# Create tuple a, then define it as a list and change the second value to "kiwi" and convert the list back to tuple
a = ("apple", "orange", "banana")
b = list(a)
b[1] = "kiwi"
a = tuple(b)

print(a)

# this also works when appending or removing

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)