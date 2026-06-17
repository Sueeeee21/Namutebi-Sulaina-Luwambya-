# even_lamba = lambda x: x % 2 == 0

# number = int(input("Enter a number: "))
# if even_lamba(number):
#     print(f"{number} is even.")

# numbers = [3, 16, 7, 22, 9, 14, 5, 18]
# evens = list(filter(lambda x : x % 2 == 0, numbers))

# print("Even numbers: ", evens)

# greater_than = list(filter(lambda x : x > 10, numbers))
# print("Numbers greater than 10: ", greater_than)

# fruits = ['Cherry', 'Fig', 'Apple', 'Banana', 'Mango', 'Grapes', 'Dragonfruit']

# fruits.sort(key=lambda x: len(x), reverse=True)
# print(fruits) 

# def countdown(n):
#     if n == 0:
#         print("Done!")
#     else:
#         print(n)
#         countdown(n - 1)
# countdown(5)

# def factorial(n):
#     if n <= 1:
#         return 1
#     return n * factorial(n - 1)

# print(factorial(5))

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(10):
    print(fibonacci(i), end=" ")