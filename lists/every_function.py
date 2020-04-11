programming_languages = ["ruby", "javascript", "python", "java"]

print(programming_languages)

# sort list without changing original list
print(sorted(programming_languages))
print(programming_languages)

# reverse order of list:
programming_languages.reverse()
print(f"Programming languages reversed: {programming_languages}")

# sort the list alphabetically
programming_languages.sort()
print(f"Programming languages in alphabetical order:\n {programming_languages}")
# reverse sort the list
programming_languages.sort(reverse=True)
print(f"Programming languages in reverse order:\n {programming_languages}")

# remove last item in list
last_language = programming_languages.pop()
print(last_language)
print(programming_languages)

# append language to end of lst
programming_languages.append("java")
print(programming_languages)

# delete an item from list using del statement
del programming_languages[0]
print(f"Deleted first item from list:\n {programming_languages}")

# remove an item from list using value
programming_languages.append('C++')
print(programming_languages)
deleted_item = "C++"
programming_languages.remove(deleted_item)
print(programming_languages)

# insert another language anywhere in the list
programming_languages.insert(1, "R")
print(programming_languages)

print(f"The new length of the list is: {len(programming_languages)}")

