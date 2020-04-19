class User:
    """Blueprint for a user data type"""

    def __init__(self, first_name, last_name, age, occupation):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.occupation = occupation

    def describe_user(self):
        print(f"The user {self.first_name} {self.last_name} is {self.age} years old and works as a {self.occupation}.")

    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name} and welcome to the site.")


mary_k = User('Mary', 'Kasparian', 31, 'programmer')
mary_k.describe_user()
mary_k.greet_user()

eric_e = User('Eric', 'Eckman', 29, 'manager')
eric_e.describe_user()
eric_e.greet_user()



