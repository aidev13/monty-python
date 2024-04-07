# === FUNCTIONS ===
# FUNTIONS ARE USEABLE BLOCKS OF CODE.
def hello(): # in python we use the keyword 'def' to 'define a funtion'
   print('Hello world')

hello() # now you must call the funtion as so.

def sum(num1, num2): # the data we puut inside the parentheses here are called parameters
   print(num1 + num2)

sum(2, 36) # the data we put inside the perenthese are called aurguments

# The differnce bbetween parameters and arguments is that parameters never change, however arugments do.

def checking_type(num3 = 0, num4=0): # you can add default vaule to your parameters in case the user never passes in an argument like so => num3=0, num4=0
   if (type(num3) is not int or type(num4) is not int): # Cheking to make sure the right type was inputted into the argument
      return "Something went wrong!" # if so this return statement will run first, and the other will not
   return num3 + num4

total = checking_type()

print(total)
print('')

# === UNKNOWN ABOUT OF ARGUMENTS ===

def multiple_items(*args): # you can use the *args keyword in the parameter if you dont know howmany arguments are going to be provided by the user
   print(args)
   print(type(args)) # The data type is for *args is a tuple!

multiple_items('David', 'Lacey', 'Cody')
print('')

# === KEYWORD ARGUMENTS (KWARGS) ===

# what if we want to refer to a name in the parameter like the num3, and num4 in the checking_type function?

def mult_named_items(**kwargs): #used if you want the arguments to have keywords
   print(kwargs)
   print(type(kwargs)) # the type will be a dictionary

mult_named_items(first = 'Hello', last = 'World') #adding keywords to the arguments


