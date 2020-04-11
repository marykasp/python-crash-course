group_number = input("How many people are in your party tonight?: ")
group_number = int(group_number)

if group_number > 8:
  print("You will have to wait for a table.")
else:
  print("Your table is ready")