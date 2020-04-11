pizzas = ["pepporoni", "veggie", "deluxe"]

# loop through each item in the pizzas list and print each item to the screen
for pizza in pizzas:
  print(f"I like {pizza} pizza!")

print("I really love pizza")

# copy of pizza list
friends_pizzas = pizzas[:]

# add a new pizza to original list
pizzas.append('sausage')
friends_pizzas.append('pineapple')

print("My favorite pizzas are:")
for pizza in pizzas:
  print(pizza)

print("My friends favorite pizzas are:")
for pizza in friends_pizzas:
  print(pizza)