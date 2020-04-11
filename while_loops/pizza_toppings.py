prompt = "Please enter a pizza topping\n"
prompt += "If you are done adding toppings, enter quit: "

topping = ""
while topping != 'quit':
  topping = input(prompt)
  if topping == 'quit':
    break
  print(f"We will add {topping} to your pizza.")

  