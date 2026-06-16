names = ["Alice", "Bob", "Charlie", "David", "Eve"]
print(names[1])

print("Before: ",names[0])

names[0] = "Alison"
print("After: ",names[0])

names.append("Frank")
print("After append: ",names)

names.insert(2, "Bathel")
print ("After insert: ", names)

names.pop(3)
print("After pop: ", names)

print(names[-1])

