
# --- LOOPS ---

# while loops - will excute a block of code while the condition is true
# ballcount = 0
# while ballcount < 4:
#    ballcount += 1
#    print(f"Ball {ballcount}")
#    if ballcount == 4:
#       ballcount = 0
#       print(f"Ball {ballcount}")
#       break

value = 1
while value <= 10:
   # print(value)
   value += 1

print('')

# breaking the loop

value = 1
while value <= 10:
   # print(value)
   if value == 5:
      break
   value += 1

# continuing a loop
   
value = 1
while value <= 10:
   value += 1
   if value == 5:
      continue
   # print(value)

# --- Write a program that counts down from a given number to 0 using a while loop.
   
# num = int(input('Enter a number to count down from: '))
# while num >= 0:
#    print(num)
#    num -= 1

# --- Write a program that calculates the sum of numbers entered by the user until they enter 0.
   
# sum = 0
# num = int(input("Enter a number (0 to stop): "))
# while num != 0:
#     sum += num
#     num = int(input("Enter a number (0 to stop): "))
# print("Sum of the numbers entered:", sum)
   

# --- Write a program that generates a random number between 1 and 100 and asks the user to guess it. The program should continue until the user guesses the correct number.

# import random

# target = random.randint(1, 100)
# guess = int(input("Guess the number between 1 and 100: "))

# while guess != target:
#     if guess < target:
#         print("Too low, try again!")
#     else:
#         print("Too high, try again!")
#     guess = int(input("Guess again: "))

# print("Congratulations! You guessed the correct number:", target)

#  --------- Messing around with a while loop ---------
# import random

# balls = 0
# strikes = 0
# outs = 0
# walk = 3
# runs = 0
# innings = 1


# while innings < 4:
#     roll = random.randint(1, 6)
#     print("Roll:", roll)
#     if roll == 1 or roll == 3 or roll == 5:
#         balls += 1
#         print(f"Balls: {balls}, Strikes: {strikes}")
#         print('')
#         if balls == 4:
#             balls = 0
#             strikes = 0
#             walk += 1
#             print("*** Walk ***: " + str(walk) )
#             if walk >= 4:
#                 runs += 1
#                 balls = 0
#                 strikes = 0
#                 print("#### RUN SCORED ####")
#                 print('')
#     else:
#         strikes += 1
#         print(f"Balls: {balls}, Strikes: {strikes}")
#         print('')
#         if strikes == 3:
#             outs += 1
#             strikes = 0
#             balls = 0
#             print("*** OUT ***: " + str(outs))
#             print('')
#         if outs == 3:
#             strikes = 0
#             balls = 0
#             outs = 0
#             walks = 3
#             print('')
#             print("Inning over!")
#             print(f"!!!! Inning: {innings} !!!!")
#             print(f"Total runs: {runs}")
#             print('')
#             innings += 1

#  --------- END  ---------
   
   

# --- FOR LOOPS ---
   
# players = ["Stacey", "David", "Lacey", "Cody"]

# for player in players:
#    print(player)
# print('')

# for x in 'Wisconsin':
#    print(x)
# print('')

# for x in 'Wisconsin':
#    if x == 'c':
#       break
#    print(x)
# print('')


# # --- range ---
# for x in range(6):
#    print(x + 1) 
# print('')

# for x in range(2, 7):
#    print(x)
# print('')

# for x in range(5, 101, 5):
#    print(x)
# else:
#    print('Hello world')
# print('')


for num in range(1, 11):
   print(num)
print('')

for x in range(1,6):
   print(x * x)
print('')

fruits = list(['Apples', 'Banana', 'Mango', 'Pineapple', 'Tomato'])

for fruit in fruits:
   print(fruit)
print('')

for x in 'String':
   print(x)
print('')

numbers = [1,2,3,4,5,6,7,8,9]
for x in numbers:
   if x % 2 == 0:
      print(x)
print('')

greetingNames = ['Mom', 'Dad', 'STacey', 'Cody', 'Tammy', 'GG']

for x in greetingNames:
   print(f'Hello {x}, welcome to python!')
print('')

numbers = [10, 5, 20, 15, 25, 30]

max_number = numbers[0]  # Assume the first number is the maximum

for number in numbers:
    if number > max_number:
        max_number = number

print("The maximum number is:", max_number)



