favorite_languages = {
  'jen': "python",
  'sarah': "c",
  'edward': "ruby",
  'phil': "python"
}

friends_list = ['eric', 'cory', 'alec', 'sarah']

for person in friends_list:
  if person in favorite_languages.keys():
    print(f"Thank you {person.title()} for respondng to the poll")
  else:
    print(f"{person.title()}, please take this poll")

