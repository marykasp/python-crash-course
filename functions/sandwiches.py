# function that takes arbitary arguments
def make_sandwhich(*sandwich_toppings):
  print(f"You would like a sandwich with the following toppings:")
  for topping in sandwich_toppings:
    print(f"- {topping}")

make_sandwhich('turkey', 'swiss cheese', 'green peppers')
make_sandwhich('bacon', 'lettuce')