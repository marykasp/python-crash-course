car = "subaru"
print("Is car == 'audi'? I predict false")
print(car == "audi")

print("Yes the value of car is equal to subaru, so I predict true")
print(car == "subaru")

pizza_toppings = ['mushrooms', 'anchovies', 'peppers']

print("Is there an option for mushrooms in the pizza toppings? I predict True")
# tests whether item is in a list
print('mushrooms' in pizza_toppings)
print("I predict false, mushrooms are not in pizza toppings list")
print('mushrooms' not in pizza_toppings) # false

city = "chicago"

# equality operator
print(city == "los angeles") # False
# inequality operator
print(city != "detroit")  # true

city = "Maimi"
print(city.lower() == "maimi") # true

age_1 = 23
age_2 = 19

print((age_1 >= 21) and (age_2 >= 21)) # false
print(age_1 < 45) # true
print(age_1 > 18 or age_2 > 18) # true

