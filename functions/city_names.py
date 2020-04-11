def city_country(city, country):
  formatted = f"{city}, {country}"
  return formatted.title()

first_city = city_country('Chicago', 'USA')
print(first_city)
second_city = city_country('Tokyo', 'Japan')
print(second_city)
third_city = city_country('santiago', 'chile')
print(third_city)