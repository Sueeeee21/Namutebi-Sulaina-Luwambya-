class User:
    def __init__(self, first_name, last_name, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email

    def describe_user(self):
        print(f"\n{self.first_name} {self.last_name}, Age: {self.age}, Email: {self.email}")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}! Welcome back.")


user1 = User("Allan", "Katongole", 20, "allan@gmail.com")
user2 = User("Aman", "Kato", 25, "aman@gmail.com")
user3 = User("Aisha", "Kizito", 22, "aisha@gmail.com")

for user in [user1, user2, user3]:
    user.describe_user()
    user.greet_user()