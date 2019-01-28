from random import *
import Consumable_Role
import Permanent_Role

party = input('How many people are in the party?   ')
level = input('What is the Level of the party?   ')
if int(party) >= 4 :
    if int(level) == 1 :
        Consumable_Role.Level_one()
        Permanent_Role.Level_one()
    else :
        print (level, 'is not a correct level')
else :
    print ('you got a big party')
