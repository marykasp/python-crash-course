prompt = "What is your age? "

active = True
while active:
  age = input(prompt)
  age = int(age)

  if age < 3:
    ticket_price = 0
  elif age < 12:
    ticket_price = 10
  else:
    ticket_price = 15
  
  print(f"You ticket costs: ${ticket_price}")
  # change active state of program:
  active = False
  

# different version using break keyword to terminate the loop
age = None

while age == None:
  age = input(prompt)
  age = int(age)

  if age < 3:
    ticket_price = 0
  elif age < 12:
    ticket_price = 10
  else:
    ticket_price = 15
  
  print(f"You ticket costs: ${ticket_price}")
