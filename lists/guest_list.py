guests = ["Albert Einstein", "Marie Curie", "John Steinbeck"]
message = "I would like to invite you to dinner."
print(f"{guests[0]}, {message}")
print(f"{guests[1]}, {message}")
print(f"{guests[2]}, {message}")

# name of guest who can't make it
print(guests[2])
guests[2] = "Bill Gates"
print(f"{guests[0]}, {message}")
print(f"{guests[1]}, {message}")
print(f"{guests[2]}, {message}")

print("I found a bigger table to invite more guests")
guests.insert(0, "Johnny Depp")
guests.insert(2, "Jane Austen")
guests.append("Steve Carrel")

print(f"{guests[0]}, {message}")
print(f"{guests[1]}, {message}")
print(f"{guests[2]}, {message}")
print(f"{guests[3]}, {message}")
print(f"{guests[4]}, {message}")
print(f"{guests[5]}, {message}")
print(f"I am now inviting {len(guests)} people to dinner.")

print("Now I can only invite 2 people to dinner.")
person = guests.pop()
print(f"I am sorry are can't invite you {person}")
person = guests.pop()
print(f"I am sorry are can't invite you {person}")
person = guests.pop()
print(f"I am sorry are can't invite you {person}")
person = guests.pop()
print(f"I am sorry are can't invite you {person}")



print(f"{guests[0]}, you are still invited")
print(f"{guests[1]}, you are still invited")

del guests[0]
del guests[0]
print(guests)