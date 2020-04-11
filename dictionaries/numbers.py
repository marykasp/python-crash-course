favorite_numbers = {
  'Eric': 29,
  'Mary': 25,
  'Ness': 7,
  'Linda': 4
}

# print(f"Eric's favorite number is {favorite_numbers['Eric']}")
# print(f"Mary's favorite number is {favorite_numbers['Mary']}")
# print(f"Ness's favorite number is {favorite_numbers['Ness']}")
# print(f"Linda's favorite number is {favorite_numbers['Linda']}")


multiple_favorite_numbers = {
  'eric': [29, 34],
  'mary': [25, 14],
  'ness': [7, 10],
  'linda': [4, 51]
}

for name, numbers in multiple_favorite_numbers.items():
  print(f"\n{name}'s favorite numbers:")
  for num in numbers:
    print(f"\t{num}")