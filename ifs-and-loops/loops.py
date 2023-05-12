a = 2
b = 12
print("Moi") if a > b else print("Hei")

c = 5
print("Moi") if a < b else print("Hei") if c > a else print("Kukkuu")

# Won't error out - if can't be empty
if a > b:
    pass

i = 0
while i < 6:
    i += 1
    if i == 4: # Skip to next loop when i == 4
        continue
    print(i)
# end while

i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("Larger than life")   
# end while

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!") 
  
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj: # print first
  for y in fruits: # Then this
    print(x, y) 