# define a class called Dog
class Dog:
    #docstring comment
    """A simple attempt to model a dog"""
    # python runs this method automatically whenever we create a new instance based on the Dog class
    # self parameter is a reference to the instance itself that calls it
    # gives the instance access to the attributes and methods of a specific class
    def __init__(self, name, age):
        """Initialize naem and age attributes"""
        self.name = name
        self.age = age
    
    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate a dog rolling over in response to a command"""
        print(f"{self.name} rolled over.")

# a class is a set of instructions or template for how to make an instance (blueprint for creating a data type)
# class Dog is a set of instructions for how to make an individual instance representing specific dogs
my_dog = Dog('Willie', 6) 
my_dog.sit()
my_dog.roll_over()

print(f"My dog's name is {my_dog.name}")
print(f"My dog is {my_dog.age} years old.")

# create another individual instance of the Dog class
your_dog = Dog('Lucy', 3)
print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()