# dictionaries nested inside a dictionary
people = {
  'eckman': {
  'first_name': 'Eric', 
  'last_name': "Eckman", 
  'city': 'chicago'
  },

  'mkasparian': {
  'first_name': 'mary',
  'last_name': 'kasparian',
  'city': 'chicago'
  },

  'abarkas': {
  'first_name': "annesa",
  'last_name': 'barkas',
  'city': 'valparaiso'
  }
}

# print(people)

# loop through key:value pairs of dictionary
for username, user_info in people.items():
  print(f"\n Username: {username}")
  full_name = user_info['first_name'] + user_info['last_name']
  location = user_info['city']

  print(f"\tFullname: {full_name.title()}")
  print(f"\tLocation: {location.title()}")