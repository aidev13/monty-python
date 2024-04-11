import sys
import random
from enum import Enum

def playRPS():
   class RPS(Enum):
      ROCK = 1
      PAPER = 2
      SCISSORS = 3

   print('')

   player_choice = input("Enter...\n1 for rock,\n2 for paper,\n3 for scissors:\n\n")
   if player_choice not in ['1', '2', '3']:
      print("You must enter 1, 2 or 3...")
      return playRPS()

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

   print("Play Again?")

   while True:   
      playAgain = input("\nPlay again?\nY for yes or \nN for no:\n")
      if playAgain.lower() not in ['y', 'n']:
         print('')
         print("Please choose \"y\" for yes \"n\" for no" )
         continue
      else:
         break
   
   if playAgain.lower() == 'y':
      return playRPS()
   else:
      print('')
      sys.exit('BYE! Play again soon!')



playRPS()