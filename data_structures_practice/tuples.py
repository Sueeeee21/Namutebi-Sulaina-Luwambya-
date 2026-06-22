x = ("samsung", "iphone", "tecno", "redmi")

# 1. Output your favorite phone brand
print("Question 1: Favorite phone brand")
print(x[2])  # tecno

# 2. Negative indexing - print the 2nd last item
print("\nQuestion 2: 2nd last item using negative indexing")
print(x[-2])  # tecno

# 3. Update "iphone" to "itel" (convert to list, update, convert back)
print("\nQuestion 3: Update 'iphone' to 'itel'")
phones_list = list(x)
phones_list[1] = "itel"
x = tuple(phones_list)
print(x)

# 4. Add "Huawei" to the tuple
print("\nQuestion 4: Add 'Huawei' to the tuple")
x = x + ("Huawei",)
print(x)

# 5. Loop through the tuple
print("\nQuestion 5: Loop through the tuple")
for phone in x:
    print(phone)

# 6. Remove/delete the first item
print("\nQuestion 6: Remove the first item")
phones_list = list(x)
phones_list.pop(0)
x = tuple(phones_list)
print(x)

# 7. Create a tuple of cities in Uganda using tuple() constructor
print("\nQuestion 7: Tuple of cities in Uganda")
cities = tuple(("Kampala", "Entebbe", "Jinja", "Gulu", "Mbarara", "Mbale"))
print(cities)

# 8. Unpack the tuple
print("\nQuestion 8: Unpack the cities tuple")
city1, city2, city3, city4, city5, city6 = cities
print(city1, city2, city3, city4, city5, city6)

# 9. Range of indexes to print the 2nd, 3rd and 4th cities
print("\nQuestion 9: 2nd, 3rd and 4th cities (index 1 to 4)")
print(cities[1:4])

# 10. Join two tuples - first names and second names
print("\nQuestion 10: Join first names and second names tuples")
first_names = ("Namutebi", "Sulaina")
second_names = ("Luwambya",)
full_name = first_names + second_names
print(full_name)

# 11. Create a tuple of colors and multiply by 3
print("\nQuestion 11: Tuple of colors multiplied by 3")
colors = ("red", "blue", "green")
print(colors * 3)

# 12. Count how many times 8 appears
print("\nQuestion 12: Number of times 8 appears")
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
print(thistuple.count(8))
