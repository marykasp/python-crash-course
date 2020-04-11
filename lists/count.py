for num in range(1,21):
  print(num)

millions = list(range(1,1000000))
# for num in millions:
#   print(num)

print(min(millions))
print(max(millions))
# sum of each num in the millions list
print(sum(millions))

# list of odd numbers
odd_numbers = list(range(1, 21, 2))
print(odd_numbers)
for num in odd_numbers:
  print(num)

# list of multiplies of 3 from 3 to 30
multiples_of_three = list(range(3,31,3))
for num in multiples_of_three:
  print(num)

squares = [value**2 for value in range(1,11)]
print(squares)

# use list comprehension to make a new list of numbers where an expression is applied to each number in a range
cubes = [value**3 for value in range(1,11)]
print(cubes)

# long way to generate a new list where expression is applied ot each value- use a for loop and create an empty list outside of the loop
new_cubes = []
for num in range(1,11):
  new_cubes.append(num** 3)

print(new_cubes)

for value in cubes:
  print(value)

for num in new_cubes:
  print(num)