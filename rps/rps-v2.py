import sys
import random
from enum import Enum

class RPS(Enum):
   ROCK = 1
   PAPER = 2
   SCISSORS = 3

playAgain = True

while playAgain:

   print('')
   player_choice = input("Enter...\n1 for rock,\n2 for paper,\n3 for scissors:\n\n")
   player = int(player_choice)

   if player < 1 or player > 3:
      print("You must enter 1, 2 or 3...")
      player_choice = input("Enter...\n1 for rock,\n2 for paper,\n3 for scissors:\n")
      player = int(player_choice)

   ai_choice = random.choice('123')
   system = int(ai_choice)

   print('')
   print('You chose ' + str(RPS(player)).replace('RPS.', '') + '!')
   print('Python chose ' + str(RPS(system)).replace('RPS.', '') + '!')
   print('')

   if player == 1 and system == 3:
      print('🎉 You Won')
   elif player == 2 and system == 1:
      print('🎉 You Won')
   elif player == 3 and system == 2:
      print('🎉 You Won')
   elif player == system:
      print("😶 Tie")
   else:
      print('🐍 Python Won!')
      
   playAgain = input("\nPlay again?\nY for yes or \nN for no:\n")
   if playAgain == "y":
      continue
   elif playAgain == "n":
      print('')
      print('Thank you for playing!')
      break
   else:
      print('Please select yes or no...')
      print('')
      playAgain = input("\nPlay again?\nY for yes or \nN for no:\n")

sys.exit('BYE! Play again soon!')