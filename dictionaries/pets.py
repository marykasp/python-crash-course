greta = {
  'breed': 'english springer spaniel',
  'owner': 'Mary Kasparian'
}

naxos = {
  'breed': "doberman",
  'owner': 'Annesa Barkas'
}

chloe = {
  'breed': 'calico',
  'owner': "Sam Barkas"
}

# store dictionaries in a list
pets = [greta, naxos, chloe]

# loop through list and print everything to screen
for pet in pets:
  print(pet)
  for key,value in pet.items():
    print(f"\t{key}: {value}")