name = 'ada lovelace'
# use title()  method on instance of string
print(name.title())
# strings are immutable in python- so original value is not modified
print(name)
print(name.upper())
print(name.lower())

first_name = 'ada'
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)
print(f"Hello, {full_name.title()}")
# store f-string: formatted string to a variable to then be printed

message = f"Hell0, {full_name.title()}"
print(message)