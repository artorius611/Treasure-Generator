
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
elif int(level) == 3 :
    Consumable_Role.Level_three()
    Permanent_Role.Level_three()
    gold = 120
    while base_party < int(party) :
        base_party += 1
        gold += 30
        Consumable_Role.Level_three_extra()
        Permanent_Role.Level_three_extra()
    else :
        print (Consumable_Role.Con_treasure)
        print (Permanent_Role.Perm_treasure)
        print ('Gold :', gold)
elif int(level) == 4 :
    Consumable_Role.Level_four()
    Permanent_Role.Level_four()
    gold = 200
    while base_party < int(party) :
        base_party += 1
        gold += 50
        Consumable_Role.Level_four_extra()
        Permanent_Role.Level_four_extra()
    else :
        print (Consumable_Role.Con_treasure)
        print (Permanent_Role.Perm_treasure)
        print ('Gold :', gold)
elif int(level) == 5 :
    Consumable_Role.Level_five()
    Permanent_Role.Level_five()
    gold = 320
    while base_party < int(party) :
        base_party += 1
        gold += 80
        Consumable_Role.Level_five_extra()
        Permanent_Role.Level_five_extra()
    else :
        print (Consumable_Role.Con_treasure)
        print (Permanent_Role.Perm_treasure)
        print ('Gold :', gold)
elif int(level) == 6 :
    Consumable_Role.Level_six()
    Permanent_Role.Level_six()
    gold = 500
    while base_party < int(party) :
        base_party += 1
        gold += 125
        Consumable_Role.Level_six_extra()
        Permanent_Role.Level_six_extra()
    else :
        print (Consumable_Role.Con_treasure)
        print (Permanent_Role.Perm_treasure)
        print ('Gold :', gold)
elif int(level) == 7 :
    Consumable_Role.Level_seven()
    Permanent_Role.Level_seven()
    gold = 720
    while base_party < int(party) :
        base_party += 1
        gold += 180
        Consumable_Role.Level_seven_extra()
        Permanent_Role.Level_seven_extra()
    else :
        print (Consumable_Role.Con_treasure)
        print (Permanent_Role.Perm_treasure)
        print ('Gold :', gold)
elif int(level) == 8 :
    Consumable_Role.Level_eight()
    Permanent_Role.Level_eight()
    gold = 1000
    while base_party < int(party) :
        base_party += 1
        gold += 250
        Consumable_Role.Level_eight_extra()
        Permanent_Role.Level_eight_extra()
    else :
        print (Consumable_Role.Con_treasure)
        print (Permanent_Role.Perm_treasure)
        print ('Gold :', gold)
elif int(level) == 9 :
    Consumable_Role.Level_nine()
    Permanent_Role.Level_nine()
    gold = 1400
    while base_party < int(party) :
        base_party += 1
        gold += 350
        Consumable_Role.Level_nine_extra()
        Permanent_Role.Level_nine_extra()
    else :
        print (Consumable_Role.Con_treasure)
        print (Permanent_Role.Perm_treasure)
        print ('Gold :', gold)
elif int(level) == 10 :
    Consumable_Role.Level_ten()
    Permanent_Role.Level_ten()
    gold = 2000
    while base_party < int(party) :
        base_party += 1
        gold += 500
        Consumable_Role.Level_ten_extra()
        Permanent_Role.Level_ten_extra()
    else :
        print (Consumable_Role.Con_treasure)
        print (Permanent_Role.Perm_treasure)
        print ('Gold :', gold)                                        
else :
    print ('Your Level is too High')
