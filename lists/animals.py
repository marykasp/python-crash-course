pets = ["cats", "dogs", "hamsters", "gerbils", "ferrets"]

for pet in pets:
  print(f"{pet.title()} would make a great pet.")

print("Any of these animals would make a great pet.")

print(f"The first three items in this list are:\n {pets[:3]}")
print(f"Three items from the middle of the list are:\n {pets[1:4]}")
print(f"The last three items are: {pets[-3:]}")