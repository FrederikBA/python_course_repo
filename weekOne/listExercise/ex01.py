x = range(1,21)

oddNumbers = [element for element in x if element % 2 != 0]

print(oddNumbers)

y = range(2, 1000001)

evenNumbers = [element for element in y if element % 2 == 0]

print(min(evenNumbers))
print(max(evenNumbers))
print(sum(evenNumbers))

z = range(3,301)

multiplesOfThree = [element for element in z if element % 3 == 0]

print(multiplesOfThree)

g = range(1,11)

cubeList = [element**3 for element in g]

print(cubeList)