number = input("Please enter a number: ")
# convert the string value to a number
number = int(number)

if number % 10 == 0:
  print(f"{number} is a multiple of 10")
else:
  print(f"The number you picked: {number} is not a multiple of 10")