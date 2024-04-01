# py playball.py

import random
print('')

count = {
   'balls': 2,
   'strikes': 2,
   'outs': 2
}

team = {
   'home': "Brewers",
   'visitors': "Reds",
}

atBat = team['home']

# ------------------------ Functions
def switchAtBat():
   global atBat
   if atBat == team['home']:
      atBat = team['visitors']
   else:
      atBat = team['home']
   
def reset_current_count():
   count['balls'] = 0
   count['strikes'] = 0

def reset_count():
   count['balls'] = 0
   count['strikes'] = 0
   count['outs'] = 0

rolled_dice = random.randint(1,6)
print(f"Dice result: {rolled_dice}") # Print

# ------------------------ End Functions

if rolled_dice == 1 or rolled_dice == 3 or rolled_dice == 5:
   count['balls'] += 1
   if count['balls'] == 4:
      reset_current_count()
   call = f'Balls: {count["balls"]}\nStrikes: {count["strikes"]}\nOuts: {count["outs"]}'
   print("Ball")
   print("")   
   print(call) # Print
else:
   count['strikes'] += 1
   if count['strikes'] == 3:
      count['outs'] +=1
      reset_current_count()
      if count['outs'] == 3:
         reset_count()
         switchAtBat()
   call = f'Balls: {count["balls"]}\nStrikes: {count["strikes"]}\nOuts: {count["outs"]}'
   print("Strike")
   print("")   
   print(call) # Print
   
print('')
print(atBat) # Print

