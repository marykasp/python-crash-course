rivers = {
  'nile': 'egypt',
  'yangtze': 'china',
  'mississippi': 'united states'
}

for river, country in rivers.items():
  print(f"The {river.title()} runs through {country.title()}")

# for loop over the keys
for river in rivers.keys():
  print(river.title())

for country in rivers.values():
  print(country.title())