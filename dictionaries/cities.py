cities = {
  'chicago': {
    'country': 'US',
    'population': 8000000,
    'fact': "has a nickname called the windy city"
  },

  'tokyo': {
    'country': 'japan',
    'population': 9000000,
    'fact': "formerly known as Edo in the 20th century"
  },
}

# print(cities)

for city, city_info in cities.items():
  print(f"\n{city.title()} Information:")
  country = city_info['country']

  print(f"\tCountry: {country.title()}")
  print(f"\tPopulation: {city_info['population']}")
  print(f"\tFun Fact: {city_info['fact']}")
