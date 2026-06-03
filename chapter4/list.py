#unlike strings lists are mutable
friends = ["Apple", "orange", 5, 590.38, "ria", "tony"]

print(friends[2])

friends[2] = "mango"

print(friends[2])

print(friends[0:4]) #it iwll take new value present at index 2 i.e. mango