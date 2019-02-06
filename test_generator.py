
from random import *
import Consumable_Role
import Permanent_Role
import Spells
import learning

party = input('How many people are in the party?   ')
level = input('What is the Level of the party?   ')
base_party = 4
gold = 0

if int(level) == 1 :
    learning.Consumables()
    Permanent_Role.Level_one()
    gold = 32
    while base_party < int(party) :
        base_party += 1
        gold += 8
        Consumable_Role.Level_one_extra()
        Permanent_Role.Level_one()
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
        Permanent_Role.Level_one()
    else :
        print (Consumable_Role.Con_treasure)
        #print (Permanent_Role.Perm_treasure)
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
elif int(level) == 11 :
    Consumable_Role.Level_eleven()
    Permanent_Role.Level_eleven()
    gold = 2800
    while base_party < int(party) :
        base_party += 1
        gold += 700
        Consumable_Role.Level_eleven_extra()
        Permanent_Role.Level_eleven_extra()
    else :
        print (Consumable_Role.Con_treasure)
        print (Permanent_Role.Perm_treasure)
        print ('Gold :', gold)
elif int(level) == 12 :
    Consumable_Role.Level_twelve()
    Permanent_Role.Level_twelve()
    gold = 4000
    while base_party < int(party) :
        base_party += 1
        gold += 1000
        Consumable_Role.Level_twelve_extra()
        Permanent_Role.Level_twelve_extra()
    else :
        print (Consumable_Role.Con_treasure)
        print (Permanent_Role.Perm_treasure)
        print ('Gold :', gold)
elif int(level) == 13 :
    Consumable_Role.Level_thirteen()
    Permanent_Role.Level_thirteen()
    gold = 6000
    while base_party < int(party) :
        base_party += 1
        gold += 1500
        Consumable_Role.Level_thirteen_extra()
        Permanent_Role.Level_thirteen_extra()
    else :
        print (Consumable_Role.Con_treasure)
        print (Permanent_Role.Perm_treasure)
        print ('Gold :', gold)
elif int(level) == 14 :
    Consumable_Role.Level_fourteen()
    Permanent_Role.Level_fourteen()
    gold = 9000
    while base_party < int(party) :
        base_party += 1
        gold += 2250
        Consumable_Role.Level_fourteen_extra()
        Permanent_Role.Level_fourteen_extra()
    else :
        print (Consumable_Role.Con_treasure)
        print (Permanent_Role.Perm_treasure)
        print ('Gold :', gold)
elif int(level) == 15 :
    Consumable_Role.Level_fifteen()
    Permanent_Role.Level_fifteen()
    gold = 13000
    while base_party < int(party) :
        base_party += 1
        gold += 3250
        Consumable_Role.Level_fifteen_extra()
        Permanent_Role.Level_fifteen_extra()
    else :
        print (Consumable_Role.Con_treasure)
        print (Permanent_Role.Perm_treasure)
        print ('Gold :', gold)
elif int(level) == 16 :
    Consumable_Role.Level_sixteen()
    Permanent_Role.Level_sixteen()
    gold = 20000
    while base_party < int(party) :
        base_party += 1
        gold += 5000
        Consumable_Role.Level_sixteen_extra()
        Permanent_Role.Level_sixteen_extra()
    else :
        print (Consumable_Role.Con_treasure)
        print (Permanent_Role.Perm_treasure)
        print ('Gold :', gold)
elif int(level) == 17 :
    Consumable_Role.Level_seventeen()
    Permanent_Role.Level_seventeen()
    gold = 30000
    while base_party < int(party) :
        base_party += 1
        gold += 7500
        Consumable_Role.Level_seventeen_extra()
        Permanent_Role.Level_seventeen_extra()
    else :
        print (Consumable_Role.Con_treasure)
        print (Permanent_Role.Perm_treasure)
        print ('Gold :', gold)
elif int(level) == 18 :
    Consumable_Role.Level_eighteen()
    Permanent_Role.Level_eighteen()
    gold = 48000
    while base_party < int(party) :
        base_party += 1
        gold += 12000
        Consumable_Role.Level_eighteen_extra()
        Permanent_Role.Level_eighteen_extra()
    else :
        print (Consumable_Role.Con_treasure)
        print (Permanent_Role.Perm_treasure)
        print ('Gold :', gold)
elif int(level) == 19 :
    Consumable_Role.Level_nineteen()
    Permanent_Role.Level_nineteen()
    gold = 80000
    while base_party < int(party) :
        base_party += 1
        gold += 20000
        Consumable_Role.Level_nineteen_extra()
        Permanent_Role.Level_nineteen_extra()
    else :
        print (Consumable_Role.Con_treasure)
        print (Permanent_Role.Perm_treasure)
        print ('Gold :', gold)
elif int(level) == 20 :
    Consumable_Role.Level_twenty()
    Permanent_Role.Level_twenty()
    gold = 140000
    while base_party < int(party) :
        base_party += 1
        gold += 35000
        Permanent_Role.Level_twenty_extra()
        Permanent_Role.Level_twenty_extra()
    else :
        print (Consumable_Role.Con_treasure)
        print (Permanent_Role.Perm_treasure)
        print ('Gold :', gold)                                        
else :
    print ('Your Level is too High')
