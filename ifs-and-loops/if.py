a = 2
b = 12
print("Moi") if a > b else print("Hei")

c = 5
print("Moi") if a < b else print("Hei") if c > a else print("Kukkuu")

# Won't error out - if can't be empty
if a > b:
    pass