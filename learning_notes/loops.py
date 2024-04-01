
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
import random

balls = 0
strikes = 0
outs = 0
walk = 3
runs = 0
innings = 1


while innings < 4:
    roll = random.randint(1, 6)
    print("Roll:", roll)
    if roll == 1 or roll == 3 or roll == 5:
        balls += 1
        print("Balls:", balls)
        print('')
        if balls == 4:
            balls == 0
            strikes == 0
            walk += 1
            print("*** Walk ***: " + str(walk) )
            if walk >= 4:
                runs += 1
                print("#### RUN SCORED ####")
    else:
        strikes += 1
        print("Strikes:", strikes)
        print('')
        if strikes == 3:
            outs += 1
            strikes = 0
            balls = 0
            print("*** OUT ***: " + str(outs))
            print('')
        if outs == 3:
            strikes = 0
            balls = 0
            outs = 0
            print("Inning over!")
            print(f"Inning: {innings}")
            print(f"total runs: {runs}")
            innings += 1

#  --------- END  ---------
   
   

# --- FOR LOOPS ---
   
# players = ["Stacey", "David", "Lacey", "Cody"]

# for x in players:
#    print(x)

# for x in "Wisconsin":
#    print(x)

# for x in players:
#    if x == 'Lacey':
#       break
#    print(x)

