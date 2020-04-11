# write a program that polls users about their dream vacation
responses = {}

active_poll = True

while active_poll:
  name = input("What is your name: ")
  response = input("What is one place in the world that you would like to visit? ")

  # add response to dictionary
  responses[name] = response

  repeat = input("Would you like to let another person respond? (y/n): ")
  if repeat == 'n':
    active_poll = False

for name, location in responses.items():
  print(f"{name} would love to visit {location}")