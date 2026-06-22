class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")


# # 9-1
restaurant = Restaurant("Nawaab", "Indian")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

# 9-2
restaurant1 = Restaurant("Nawaab", "Indian")
restaurant2 = Restaurant("Mama's Kitchen", "Italian")
restaurant3 = Restaurant("Dragon Palace", "Chinese")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()