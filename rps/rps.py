import sys
import random

print('')

player_choice = input("Enter...\n1 for rock,\n2 for paper,\n3 for scissors:\n\n")
player = int(player_choice)

if player < 1 or player > 3:
   sys.exit("You must enter 1, 2 or 3...")

ai_choice = random.choice('123')

system = int(ai_choice)
print('')
print('You chose ' + player_choice + '!')
print('Python chose ' + ai_choice + '!')
print('')

if player == 1 and system == 3:
   print('You Won')
elif player == 2 and system == 1:
   print('You Won')
elif player == 3 and system == 2:
   print('You Won')
elif player == system:
   print("Tie")
else:
   print('Python Won!')
   




