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


# create three different instances from the class and call describe_restaurant on each individual instance
first_restaurant = Restaurant("Club Lucky", "Italian")
second_restaurant = Restaurant("Kuma's corner", "American hamburgers")
third_restaurant = Restaurant("Dante's", "Pizzaria")

first_restaurant.describe_restaurant()
second_restaurant.describe_restaurant()
third_restaurant.describe_restaurant()