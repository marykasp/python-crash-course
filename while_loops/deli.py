sandwich_orders = ['turkey club', 'pastrami', 'italian sub', 'blt', 'pastrami', 'tuna melt', 'pastrami']
finished_sandwhiches = []

print("Sorry the deli has run out of pastrimi")
while 'pastrami' in sandwich_orders:
  sandwich_orders.remove('pastrami')

while sandwich_orders:
  current_sandwhich = sandwich_orders.pop()
  print(f"I made your {current_sandwhich} sandwhich.")

  # append sandwhich made to new list
  finished_sandwhiches.append(current_sandwhich)

# Display all the sandwhichs that have been made: use a for loop to loop over the new list created
print("Here are all the sandwhiches that were made: ")
for sandwich in finished_sandwhiches:
  print(sandwich)

