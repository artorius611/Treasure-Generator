from random import *
import Consumable_Role
import Permanent_Role

party = input('How many people are in the party?   ')
level = input('What is the Level of the party?   ')
base_party = 4
gold = 0

if int(level) == 1 :
    Consumable_Role.Level_one()
    Permanent_Role.Level_one()
    gold = 32
    while base_party < int(party) :
        base_party += 1
        gold += 8
        Consumable_Role.Level_one_extra()
        Permanent_Role.Level_one_extra()
    else :
        print (Consumable_Role.Con_treasure)
        print (Permanent_Role.Perm_treasure)
        print ('Gold :', gold)
        
elif int(level) == 2 :
    Consumable_Role.Level_two()
    Permanent_Role.Level_two()
    gold = 64
    while base_party < int(party) :
        base_party += 1
        gold += 16
        Consumable_Role.Level_two_extra()
        Permanent_Role.Level_two_extra()
    else :
        print (Consumable_Role.Con_treasure)
        print (Permanent_Role.Perm_treasure)
        print ('Gold :', gold)
else :
    print ('Your Level is too High')
