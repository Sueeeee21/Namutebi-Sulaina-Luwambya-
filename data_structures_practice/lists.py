# names = ["Alice", "Bob", "Charlie", "David", "Eve"]
# print(names[1])

# print("Before: ",names[0])

# names[0] = "Alison"
# print("After: ",names[0])

# names.append("Frank")
# print("After append: ",names)

# names.insert(2, "Bathel")
# print ("After insert: ", names)

# names.pop(3)
# print("After pop: ", names)

# print(names[-1])

# fruits = ["apple", "banana", "cherry", "plum", "peach", "grape", "kiwi"]
# print("All fruits: ",fruits)

# print("3 to 5: ", fruits[2:5])

# countries = ["Uganda", "Sudan", "Egypt", "Tunisia", "Nigeria", "Ghana", "Malawi"]

# print("Original: ", countries)
# print("Copy:", countries.copy())

# for country in countries:
#     print(country)

animals = ["cat", "dog", "rabbit", "hamster", "parrot"]
# print("Before sort: ", animals)

# animals.sort()
# print("Ascending order: ", animals)

# animals.sort(reverse=True)
# print("Descending order: ", animals)

# for animal in animals:
#     if "a" in animal.lower():
#         print(animal)

first_names = ["Alice", "Bob", "Charlie", "David", "Eve"]   
last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones"] 

concatenated_list = first_names + last_names
print("Concatenated names: ", concatenated_list)

joined_list = list(zip(first_names, last_names))
full_names = [f"{first} {last}" for first, last in joined_list]

print("Joined list: ", joined_list)
print("Full names: ", full_names)