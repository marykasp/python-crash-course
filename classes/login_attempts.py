class User:
    """Blueprint for a user data type"""

    def __init__(self, first_name, last_name, age, occupation):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.occupation = occupation
        self.login_attempts = 0

    def describe_user(self):
        print(f"The user {self.first_name} {self.last_name} is {self.age} years old and works as a {self.occupation}.")

    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name} and welcome to the site.")

    # increment login attempts
    def increment_login_attempts(self):
        """Increments login attempts by 1"""
        self.login_attempts += 1

    def reset_login_attemps(self):
        """Resets login attempts"""
        self.login_attempts = 0

# new User instance
new_user = User('Mary', 'Kasp', 31, 'scientist')
new_user.increment_login_attempts()
new_user.increment_login_attempts()
new_user.increment_login_attempts()
new_user.increment_login_attempts()

print(new_user.login_attempts)
new_user.reset_login_attemps()
print(new_user.login_attempts)