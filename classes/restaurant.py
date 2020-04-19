# make a Restaurant class, __init__ method should store the restaurant name and a cuisine type
class Restaurant:
    """A class representing a Restaurant model"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant name and cuisine type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The restaurant name is {self.restaurant_name}.")
        print(f"The type of cuisine is {self.cuisine_type}.")
    
    def open_restaurant(self):
        """Prints a message saying that the restaurant is open"""
        print(f"{self.restaurant_name} is now open for business!")

# make an instance of the Restaurant class
new_restaurant = Restaurant('Bite cafe', 'vegan')
print(f"{new_restaurant.restaurant_name}")
print(f"{new_restaurant.cuisine_type}.\n")
new_restaurant.describe_restaurant()
new_restaurant.open_restaurant()
    