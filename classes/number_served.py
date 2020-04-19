class Restaurant:
    """A class representing a Restaurant model"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant name and cuisine type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        # add a default attribute (doesn't need to be passed in as a parameter)
        self.number_served = 0

    def describe_restaurant(self):
        print(f"The restaurant name is {self.restaurant_name}.")
        print(f"The type of cuisine is {self.cuisine_type}.")
    
    def open_restaurant(self):
        """Prints a message saying that the restaurant is open"""
        print(f"{self.restaurant_name} is now open for business!")

    # method that changes number of customers served
    def set_number_served(self, customers):
        self.number_served = customers

    # increment number_served
    def increment_number_served(self, customers):
        self.number_served += customers

# create a new instance
restaurant = Restaurant('Cluby Lucky', 'Italian')
print(f"{restaurant.restaurant_name} has servered {restaurant.number_served} customers.\n")

restaurant.number_served = 50
print(f"{restaurant.restaurant_name} has servered {restaurant.number_served} customers.\n")

restaurant.set_number_served(100)
print(f"{restaurant.restaurant_name} has servered {restaurant.number_served} customers.\n")

restaurant.increment_number_served(10)
print(f"{restaurant.restaurant_name} has servered {restaurant.number_served} customers.\n")

