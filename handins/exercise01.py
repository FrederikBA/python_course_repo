import math

# Exercise 1
#1.A - Iterate a list of names to return a list of the names starting with H
names = ['Hans', 'Jens', 'Hanne', 'Peter', 'Birgitte']

names_starting_with_h = [name for name in names if name[0] == 'H']

#1.B - In one line create a list of the numbers 1-100 to the power of 3

number_list = [n**3 for n in range(1,101)]

#1.C - Iterate a list of names to create a list of tuples
# where the tuples first value is the length of the name and the second is the name

tuple_list = [(len(name), name) for name in names]

#1.D - Iterate over each character in a string and get only those that are nummeric

numeric_list = [n for n in 'FD6G5T2' if n.isdigit()]

#1.E - Using only a list comprehension wrapped in set() get all possible combinations
# from throwing 2 dice (hint use 2 for loops in a single list comprehension).
# Result should look like: [2,3,4,5,6,7,8,...]
# or a more complex/accurate solution: [(1,1),(1,2)...] in a way that (1,2) is equal to (2,1). 

die = range(1,7)

dice_result = set([(x,y) for x in die for y in die])

#Exercise 2
#2.A - Iterate a list of names and create a dictionary
# where key is the name and value is the length of the name

name_dict = {n: len(n) for n in names}


#2.B - Iterate a list of numbers and create a dictionary
# with {key:value} being {number:squareroot_of_number}
number_dict = {n: math.sqrt(n) for n in range(1,11)}


