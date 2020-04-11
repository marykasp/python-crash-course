# lists in a dictionary
favorite_places = {
  'mary': ['chicago', 'canada', 'belize'],
  'linda': ['valparaiso', 'dominican republic', 'jamaica'],
  'arthur': ['montana', 'valparaiso', 'dominican republic'],
  'sam': ['chicago']
}

# loop through the dictionary and print each persons name and their favorite places
for person, places in favorite_places.items():
  if len(places) == 1:
    print(f"\n{person} has only one favorite place:")
  else:
    print(f"\n{person}'s favorite places include:")
  for location in places:
    print(f"\t {location}")