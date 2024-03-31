#  --- dictionaires are like an object in JS which stores key-value pairs ---

# example 1
player = {
   'fullName': "David Liebherr",
   'poisition': "DH",
   'throws': 'Right',
   'bats': 'Right',
   'hits': 425,
   'atbat': 851
}
# example 2 - contructor function
player2 = dict(
   fullName = 'Cody Liebherr',
   position = 'Catcher',
   throws = 'Left',
   bats = 'Left',
   hits = 256,
   atbat = 873,
)

team = dict(
   pitcher = dict (
         fullName = 'Dad Liebherr',
         throws = 'Left',
         bats = 'Left',
         hits = 256,
         atbat = 873,
          ),
   catcher = dict (
         fullName = 'Cody Liebherr',
         throws = 'Left',
         bats = 'Left',
         hits = 156,
         atbat = 463,
          ),
   base_1st = dict (
         fullName = 'Stacey Liebherr',
         throws = 'Right',
         bats = 'Right',
         hits = 452,
         atbat = 873,
          ),
   base_2nd = dict (
         fullName = 'Tammi Marshall',
         throws = 'Left',
         bats = 'Left',
         hits = 16,
         atbat = 273,
          ),
   short_stop = dict (
         fullName = 'GG Marshall',
         throws = 'Rtght',
         bats = 'Left',
         hits = 684,
         atbat = 982,
          ),
   base_3rd = dict (
         fullName = 'Travis Enders',
         throws = 'Right',
         bats = 'Right',
         hits = 1,
         atbat = 352,
          ),  
)

def batting_average(batter):
   hits = batter['hits']
   atbat = batter['atbat']
   avg = hits / atbat
   rounded_avg = round(avg, 3)
   stmt = f"{batter['fullName']}'s Avg: {rounded_avg}"
   return  stmt

# print(team.get('pitcher')['hits'])
# print(team['pitcher']['atbat'])

# print(player)
# print('')
# print(player2)
# print('')
# print(batting_average(team['short_stop']))
# print('')
# print(team['base_1st']['fullName'], team['base_1st']['hits'])

# --- ADDING ITEMS ----

player['strikeouts'] = 78

# --- LIST ALL KEYS AND VALUES ---

# print(team.keys())
# print(team.values())


# --- LIST ALL KEYS AND VALUES AS A TUPLE ---

# print(team['pitcher'].items())

# --- VERIFY A KEY EXIST IN A DICT ---

# print('right_field' in team) # prints False
# print('short_stop' in team) # prints True

# print('')

# --- CHANGING VALUES IN A DICT ---

# print(team['catcher'])
# print('')

x = team['catcher']['fullName'] = 'Chris Enders'
# print(x)
# print('')

# print(team['catcher'])
# print('')

team.update({
   'left_field':  dict (
         fullName = 'Bop Marshall',
         throws = 'Left',
         bats = 'Left',
         hits = 256,
         atbat = 873,
          )
})

# print('')
# print(team)

# --- REMOVING AND CLEARING ITEMS ---

# print(len(team))
# print(team.pop("catcher")) # returns the value and removes the item from the dist
# print(len(team))
# print('')
# print(team.popitem()) # returns teh last item, as a tuple, in the dist and removes it from the dist
# print('')
# print(team)
# print(len(team))

# --- DELETE AND CLEAR ITEMS ---

# print('')
# print(team)
# print('')
# print('')
# del team['left_field']
# print(team)

# print('')
# team['pitcher'].clear()
# print(team)

# --- COPY DICTIONARIES ---

# player_copy = player2.copy()
# player2['walks'] = 54
# print(player2)
# # print(player)

# player_copy_2 = dict(player)
# print(player_copy_2)


# --- NESTED DICT ---

# NOTE: im grabbing the dict from the top of the page
team_members = {
   "player_1" : player,
   "player_2" : player2
}

# print("Hits: " + str(team_members['player_1']['hits']) + " atbats: " + str(team_members['player_1']['atbat']))
# print(batting_average(team_members['player_1']))



# ---- SETS ----

# A set is an unordered collection of unique elements. This means that a set CANNOT HAVE DUPLICATE ELEMENTS, and the order in which the elements are stored is not guaranteed. Sets are mutable, meaning you can add or remove elements from them.

# You can create a set in Python using curly braces {} or the set([]) constructor.

set1 = set((False,1,2,3, 4)) # you can use [] or () inside the set construtor function
set2 = {True, 4,5,6, 0}

# Union of two sets
union_set = set1 | set2  # or set1.union(set2) ... joins two sets together
print(union_set)

# Intersection of two sets
intersection_set = set1 & set2  # or set1.intersection(set2) ... displays common elements
print(intersection_set)

# Difference between two sets
difference_set = set2 - set1  # or set1.difference(set2) .. displays the unnique elements of a given set
print(difference_set)

# Symmetric difference between two sets
symmetric_difference_set = set1 ^ set2  # or set1.symmetric_difference(set2) ... will removing common elements
print(symmetric_difference_set)

# NOTE!, True is a dupe of 1 (True = 1) while False is a dupe of 0 (False = 0)

# Adding to a set
set2.add(7)
print(set2)
print(set2)

# addding more than one element to a set
set3 = {8,9,10}
set2.update(set3)
print(set2)

