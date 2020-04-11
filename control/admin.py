usernames = ["admin", "alserina", "rocketman", "rushmore", "butthead"]
# usernames = []

if usernames:
  for username in usernames:
    if username == "admin":
      print("Hello admin, would you like to see a status report?")
    else:
      print(f"Hello {username}, thank you for logging in.")
else:
  print("We need to find some users!")

current_users = ["admin", "alserina", "rocketman", "rushmore", "friedrice"]
new_users = ["peaches", "willowbrook", "ALSERINA", "mastermind", "RUSHMORE"]


for user in new_users:
  if user.lower() in current_users:
    print("Username alreaedy taken, please enter another one")
  else:
    print("congrats, that username is available")

numbers = list(range(1,10))

for num in numbers:
  if num == 1:
    print(f"{num}st")
  elif num == 2:
    print(f"{num}nd")
  elif num == 3:
    print(f"{num}rd")
  else:
    print(f"{num}th")