from random import *

Con_treasure = []
Consumable = {'1st Level' : { 1 : 'Light Ammunition',
                              2 : 'Acid Flask',
                              3 : 'Alchemists Fire' ,
                              4 : 'Bottled Lightning' ,
                              5 : 'Liquid Ice' ,
                              6 : 'Tanglefoot Bag' ,
                              7 : 'Thunderstone',
                              8 : 'Bird Feather' ,
                              9 : 'Holy Water' ,
                              10 : 'Ladder feather tolken' ,
                              11 : 'unholy water' ,
                              12 : 'Antidote' ,
                              13 : 'Antiplague' ,
                              14 : 'Cheetahs Elixir' ,
                              15 : 'Darkvision Elixir' ,
                              16 : 'Eagle-eye Elixir' ,
                              17 : 'Minor Elixir of Life' ,
                              18 : 'Runestone' ,
                              19 : 'Nector of purification' ,
                              20 : 'Arsenic' ,
                              21 : 'Giant Centipede Venom' ,
                              22 : 'Minor Healing potion' ,
                              23 : 'Scroll of 1st level spell' ,
                              24 : 'Silversheen' ,
                              25 : 'Smokestick' ,
                              26 : 'Sunrod' ,
                              27 : 'Tindertwig (10)' ,
                              28 : 'Jade Cat' ,
                              29 : 'Owlbear Claw' ,
                              30 : 'Potency Crystal' ,
                              31 : 'Wolf Fang' ,
                              32 : 'Dull Gray Aeon Stone'},
              '2nd Level' : { 1 : 'Sleep Arrow' ,
                              2 : 'Holly Bush Feather Token' ,
                              3 : 'Comprehension' ,
                              4 : 'Infiltrators Elixir' ,
                              5 : 'Salamander Elixir' ,
                              6 : 'Stone Fist Elixir' ,
                              7 : 'Winter Wolf Elixir' ,
                              8 : 'Everburning Torch' ,
                              9 : 'Wayfinder' ,
                              10 : 'Oil of Potency' ,
                              11 : 'Oil of Weightlessness' ,
                              12 : 'Belladonna' ,
                              13 : 'Sleep Poison' ,
                              14 : 'Black Adder Venom' ,
                              15 : 'Bloodseeker Beak' ,
                              16 : 'Retruning Clasp'},
              '3rd Level' : { 1 : 'Beacon Shot' ,
                              2 : 'Spellstrike Ammunition 1st' ,
                              3 : 'Vine Arrow' , 
                              4 : 'Chest Feather Token' ,
                              5 : 'Bombers Eye Elixir' ,
                              6 : 'Bravos Brew' ,
                              7 : 'Cats Eye Elixir' ,
                              8 : 'Greater Darkvision Elixir' ,
                              9 : 'Mistform Elixir' ,
                              10 : 'Oil of Mending' ,
                              11 : 'Cytillesh Oil' ,
                              12 : 'Graveroot' ,
                              13 : 'Barkskin Potion' ,
                              14 : 'Invisibillity Potion' ,
                              15 : 'Lesser Healing Potion' ,
                              16 : 'Potion of Water Breathing' ,
                              17 : 'Scroll of 2nd Level Spell' ,
                              18 : 'Feather Step Stone' ,
                              19 : 'Monkey Pin' ,
                              20 : 'Savior Spike'},
              '4th Level' : { 1 : 'Climbing Bolt' ,
                              2 : 'Viper Arrow' ,
                              3 : 'Fan Feather Token' ,
                              4 : 'Lesser Elixir of Life' ,
                              5 : 'Sea Touch Elixir' ,
                              6 : 'Fear  Gem'},
              '5th Level' : { 1 : 'Spellstrike Ammunition 2nd' ,
                              2 : 'Dust of Appearance' ,
                              3 : 'Greater Antidote' ,
                              4 : 'Greater Antiplague' ,
                              5 : 'Lesser Bestial Mutagen' ,
                              6 : 'Lesser Bullhead Mutagen' ,
                              7 : 'Lesser Cognitive Mutagen' ,
                              8 : 'Lesser Juggernaut Mutagen' ,
                              9 : 'Lesser Quicksilver Mutagen' ,
                              10 : 'Lesser Silvertongue Mutagen' ,
                              11 : 'Salve of Antiparalysis' ,
                              12 : 'Salve of Slipperiness' ,
                              13 : 'Hunting Spider Venom' ,
                              14 : 'Lesser Potion of Resistance' ,
                              15 : 'Moderate Healing Potion' ,
                              16 : 'Potion of Leaping ' ,
                              17 : 'Scroll of 3rd Level Spell' ,
                              18 : 'Bronze Bull pendant' ,
                              19 : 'Onyx Panther'},
              '6th Level' : { 1 : 'Tree Feather Token' ,
                              2 : 'True Darkvision Elixir' , 
                              3 : 'Greater Oil of Weightlessness' ,
                              4 : 'Giant Scorpion Venom' ,
                              5 : 'Potion of Quickness' , 
                              6 : 'Potion of Swimming' ,
                              7 : 'Grim Trophy' ,
                              8 : 'Mesmerizing Opal' ,
                              9 : 'Mummified Bat' ,
                              10 : 'Wand of 3rd Level Spell'},
              '7th Level' : { 1 : 'Spellstrike Ammunition 3rd' ,
                              2 : 'Anchor Feather Token' ,
                              3 : 'Candle of Revealing' ,
                              4 : 'Giant Wasp Venom' ,
                              5 : 'Malyass Root Paste' ,
                              6 : 'Potion of Disguise' ,
                              7 : 'Young Dragons Breath Potion' ,
                              8 : 'Scroll of 4th Level Spell' ,
                              9 : 'Effervescent Ampule' ,
                              10 : 'Murderers Knot' , 
                              11 : 'Swift Block Cabochon'},
              '8th Level' : { 1 : 'Explosive Ammunition' ,
                              2 : 'Javelin of lighting' ,
                              3 : 'Swan Boat Feather Token' ,
                              4 : 'Elixir of Life' ,
                              5 : 'Candle of Truth' ,
                              6 : 'Baleful Oil' ,
                              7 : 'Blessed Oil' ,
                              8 : 'Nettleweed Residue' ,
                              9 : 'Wyvern Poison' ,
                              10 : 'Greater Healing Potion' ,
                              11 : 'Potion of Flying' , 
                              12 : 'Wand of 4th Level Spell' ,
                              },
              '9th Level' : { 1 : 'Spellstrike Ammunition 4th' ,
                              2 : 'Dust of Disappearing' ,
                              3 : 'Whip Feather Token' ,
                              4 : 'Bestial Mutagen' ,
                              5 : 'Cognitive Mutagen' ,
                              6 : 'Juggernaut Mutagen' ,
                              7 : 'Quicksilver Mutagen' ,
                              8 : 'Silvertoungue Mutagen' ,
                              9 : 'Lich Dust' ,
                              10 : 'Spider Root' ,
                              11 : 'Potion of Resistance' ,
                              12 : 'Scroll of 5th Level Spell' ,
                              13 : 'Gallows Tooth' ,
                              14 : 'Iron Medallion' ,
                              15 : 'Vanishing Coin'},
             '10th level' : { 1 : 'Penetrating Ammunition' ,
                              2 : 'Storm Arrow' ,
                              3 : 'Elemental Gem' ,
                              4 : 'True Antidote' ,
                              5 : 'True Antiplague' ,
                              6 : 'Oil of Keen Edges' ,
                              7 : 'Shadow Essence' ,
                              8 : 'Wolfsbane' ,
                              9 : 'Greater Potion of Disguise' ,
                              10 : 'Potion of Toungue' ,
                              11 : 'Emerald Grasshopper'},
             '11th Level' : { 1 : 'Spellstrike Ammunition 5th' ,
                              2 : 'Oil of Animation', 
                              3 : 'Greater Salve of Antiparalysis' ,
                              4 : 'Blightburn Resin' ,
                              5 : 'Scroll of 6th Level Spell' ,
                              6 : 'Mending Lattice'},
             '12th Level' : {},
             '13th Level' : {},
             '14th Level' : {},
             '15th Level' : {},
             '16th Level' : {},
             '17th Level' : {},
             '18th Level' : {},
             '19th Level' : {},
             '20th Level' : {}}

class Level_one () :
    def __init__ (self) :
        a = 12
        b = 4
        c = 2
        for x in range(int(a)) :
            x = randint(1,32)
            Con_treasure.append(Consumable['1st Level'][x])
        for x in range(int(b)) :
            x = randint(1,16)
            Con_treasure.append(Consumable['2nd Level'][x])
        for x in range(int(c)) :
            x = randint(1,20) 
            Con_treasure.append(Consumable['3rd Level'][x])

class Level_one_extra () :
    def __init__ (self) :
        a = 1
        b = 1
        c = 1
        for x in range(int(a)) :
            x = randint(1,32)
            Con_treasure.append(Consumable['1st Level'][x])
        for x in range(2) :
            x = randint(1,2)
            if x == 1 :
                for x in range(int(b)) :
                    x = randint(1,16)
                    Con_treasure.append(Consumable['2nd Level'][x])
            else :
                for x in range(int(c)) :
                    x = randint(1,20) 
                    Con_treasure.append(Consumable['3rd Level'][x])

class Level_two () : 
    def __init__ (self) :
        a = 2
        b = 8
        c = 4
        for x in range(int(a)) :
            x = randint(1,32)
            Con_treasure.append(Consumable['1st Level'][x])
        for x in range(int(b)) :
            x = randint(1,16)
            Con_treasure.append(Consumable['2nd Level'][x])
        for x in range(int(c)) :
            x = randint(1,20) 
            Con_treasure.append(Consumable['3rd Level'][x]) 

class Level_two_extra () : 
    def __init__ (self) :
        b = 1
        c = 1
        for x in range(int(b)) :
            x = randint(1,16)
            Con_treasure.append(Consumable['2nd Level'][x])
        for x in range(2) :
            x = randint(1,2)
            if x == 1 :
                for x in range(int(b)) :
                    x = randint(1,16)
                    Con_treasure.append(Consumable['2nd Level'][x])
            else :
                for x in range(int(c)) :
                    x = randint(1,20) 
                    Con_treasure.append(Consumable['3rd Level'][x])
