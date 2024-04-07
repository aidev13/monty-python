# --- String data types ---

# ---Literal Assignment ---

first = 'david'
last = 'Liebherr'

# print(type(first))
# print(type(first) == int)
# print(isinstance(first, str))

# --- constructor function ---

# pizza = str("Peeperoni")
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))

# --- Concatenation ---
fullname = first + ' ' + last
# print(fullname)

fullname += "!"
# print(fullname)

# --- Casting a number to a string ---
decade = str(1986) #this is now not a number but rather a string, lets verify below
# print(type(decade)) #checking the type
# print(decade)

dob = decade + ', DOB'
# print(dob)

num = 2
num += 2
# print(type(num))
# print(num)

# Multiple lines
multi_lines = '''
Hey, bro

Go badgers,
   They lost bro!
      maybe next time...
'''
# print(multi_lines)

# --- Escaping special characters ---
sentence = 'I\'m always working!\n\tHey!\n\nWhere\'s this at \\located'
# print(sentence)

# --- string methods ---
# print(first)
# print(first.lower())
# print(first.upper())
# print(first)

sliced_first = first[1:] 
# print(first[0].upper() + sliced_first)
# print(first.title())

# print(multi_lines.title()) # changes the first letter of each work to a capital letter
# print(multi_lines.replace('maybe', 'We will win')) 
# print(multi_lines)

# print(len(multi_lines))
multi_lines += '                 '
multi_lines = '  ' + multi_lines
# print(len(multi_lines))

# print(len(multi_lines.strip()))
# print(len(multi_lines.lstrip()))
# print(len(multi_lines.rstrip()))

# --- building a menu ---

print(' ')

title = 'menu'.upper()
print(title.center(20, '='))
print('Coffee'.ljust(15, '.') + '$5'.rjust(5))
print('Eggs'.ljust(15, '.') + '$3'.rjust(5))
print('Bacon'.ljust(15, '.') + 'Free'.rjust(5))

print('')

# print(first[0])
# print(first[-1]) # gets the last value
# print(first[1:3]) # get a range
# print(first[1:])  # gets the remaining 
# print(first)
# print(first.title().replace('i','e'))
# print(first[0:4].replace('i','e'))
# print(first.title()[0:4].replace('i','e'))

# --- numerica data types ----

# Interger type
price_1 = 100
price_2 = int(80)
price_3 = str(80)
print(type(price_1))
print(type(price_2))
print(type(price_3))
print(isinstance(price_1, int))
print(isinstance(price_2, int))
print(isinstance(price_3, int))

# print(price_1 + price_2) 
# print(price_1 + price_3) # you get an error becuase price_3 is a string type as declared

# --- float type --- 

print('')
gpa = 3.28
print(type(gpa))
print(isinstance(gpa, float))

f = float(5.56)
print(f)
print(type(f))
print(isinstance(f, float))

# === COMPLEX TYPES ====
print('')
comp_value = 5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

# --- Built in functions for number ---
print('')
print(abs(gpa)) # absolute value
print(abs(gpa * -1)) # absolute value
print(round(gpa)) # absolute value

import math
print('')
print(math.pi)
print(round(math.sqrt(64))) #square root
print(math.ceil(gpa)) # rounds up
print(math.floor(gpa)) # rounds down

# --- Casting a string into a number ---
print('')
zipcode = '53124'
zip_value = int(zipcode)
print(type(zipcode))
print(zip_value)
print(type(zip_value))


