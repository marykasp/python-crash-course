places_to_travel = ["thailand", "greece", "netherlands", "amsterdam", "italy"]
print(places_to_travel)

# sort list without mutating the original: use built in sorted() function 
print(sorted(places_to_travel))

print(places_to_travel)
print(sorted(places_to_travel, reverse=True))
print(places_to_travel)

# reverse to reverse list- changes original list
places_to_travel.reverse()
print(places_to_travel)
# revert back to original with reverse
places_to_travel.reverse()
print(places_to_travel)

# sort list- changing the original
places_to_travel.sort()
print(places_to_travel)

places_to_travel.sort(reverse=True)
print(places_to_travel)