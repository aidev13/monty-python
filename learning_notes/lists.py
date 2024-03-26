# a list in python is just like an array in JS or PHP
users = ['David', 'Stacey', 'Lacey', 'Cody', 'Bob']
data = ['Kris-ann', 35, False]
emptyList = []

constructor_list = list(['David', 37, True]) # making a list with the list construtor function

print(constructor_list[1])
print('')

print('David' in emptyList) # check to see if a piece of data is in a list, will return True or False

print(users[0]) # find the value of a lists index 
print(users[-1]) # see the LAST value in a list
print(users[-2]) # checks second to last value in list and so on...
print(users[-3]) 

print(users.index('Cody')) #find the index's postion based for a value   
print(users[0:3]) # find a range of values 
print(users[3:])

print(len(users))

# --- adding to a list ---
users.append('Tammy')
print(users)

# --- Adding a list to a list ---
# ex 1
users += ['Bop'] # when using this ex, make sure you use [] if you have one item otherwise each charatcher will become part of the list rather than the word itself...
print(users)

# ex 2
users.extend(['GG', 'Travis', 'Chris']) # add more a new list to an exsisting list
print(users)

# ex 3
# users.extend(data) # add an exsisting list to an excisting list
# print(users)

# --- Picking a spot to insert our data in a list ---

print("")
users.insert(0, 'Karla')
print(users)

print("")
users[2:2] = ['Alex', 'Porter']
print(users)

print("")
users[1:2] = ['Carl', "DJL"]
print(users)

# --- Removing data ---

print("")
users.remove('Alex') # removing a single piece of data
print(users)

print("")
users.pop() # removing the last item in list
print(users)

print("")
print(users.pop()) # pop returns the vaule of what was popped off!

print("")
del users[0] # delete data by its index
print(users)

print("")
# del data # delete an entire list
# data.clear() # Clears data from a list, but does not delete the list itself

# --- Sorting ---

print("")
users[1:2] = ["dave"]
users.sort() # will sort the list alphabetically form A - Z
print(users)

print("")
users.sort(key=str.upper)
print(users)

print("")
users.sort(key=str.lower)
print(users)

numbers = [1,2,45,63,43,13,56]
print("")
numbers.sort() # --- NOTE: You can only sort the same data types... ---
print(numbers)
numbers.sort(reverse=True) # reverseing the sorted list
print(numbers)

print("")
numbers.reverse() # reversing the data
print(numbers)
users.reverse()
print(users)

print("")
print(sorted(numbers, reverse=True))
print(sorted(users, reverse=True))

print("")
numbers_copy = numbers.copy() # gets a copy of original unsorted LIST
print(numbers_copy)

print("")
print(type(numbers)) # shows the type which is a list type in this case

# --- Tuples ---

# Explaination
# A tuple is an ordered collection of elements, similar to a list. However, unlike lists, tuples are immutable, meaning once they are created, their contents cannot be changed. Tuples are typically used to store heterogeneous data, and they are defined using parentheses.

# Tuples can be accessed using indexing and slicing, just like lists. They are commonly used when you want to represent a collection of items that should not be modified after creation.

# To make a tuple, we use (), instead of []

my_tuple = tuple(('Stacey', 31, True)) # Using the tupel constructor function
my_tuple_2 = ('Hello, world', 123, True) # using ()

print(my_tuple) # verfing the type
print(my_tuple_2) # verfing the type

print(type(my_tuple)) # verfing the type
print(type(my_tuple_2))

print('')

# --- Packing and Unpacking a tuple ---

# packing - assigning vaules to a tuple
newlist = list(my_tuple)
newlist.append('is hot')
newtuple = tuple(newlist)
print(newlist)
print(newtuple)

# unpacking - removing values from tuple
anothertuple = (1, 2, 3, 3, 3, 4, 5)
(*one, two, three, hey) = anothertuple

print('')
print(one)
print(two)
print(hey)

print('')
# print(anothertuple.count(3))
print(anothertuple.index(5))





