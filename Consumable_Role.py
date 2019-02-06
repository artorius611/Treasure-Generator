from random import *
import Spells

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
                              23 : 'Scroll of Level 1 Spell' ,
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
                              16 : 'Retruning Clasp' ,
                              17 : 'Wand of Level 1 Spell'},
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
                              17 : 'Scroll of Level 2 Spell' ,
                              18 : 'Feather Step Stone' ,
                              19 : 'Monkey Pin' ,
                              20 : 'Savior Spike'},
              '4th Level' : { 1 : 'Climbing Bolt' ,
                              2 : 'Viper Arrow' ,
                              3 : 'Fan Feather Token' ,
                              4 : 'Lesser Elixir of Life' ,
                              5 : 'Sea Touch Elixir' ,
                              6 : 'Fear  Gem', 
                              7 : 'Wand of Level 2 Spell'},
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
                              17 : 'Scroll of Level 3 Spell' ,
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
                              10 : 'Wand of Level 3 Spell'},
              '7th Level' : { 1 : 'Spellstrike Ammunition 3rd' ,
                              2 : 'Anchor Feather Token' ,
                              3 : 'Candle of Revealing' ,
                              4 : 'Giant Wasp Venom' ,
                              5 : 'Malyass Root Paste' ,
                              6 : 'Potion of Disguise' ,
                              7 : 'Young Dragons Breath Potion' ,
                              8 : 'Scroll of Level 4 Spell' ,
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
                              12 : 'Wand of Level 4 Spell'},
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
                              12 : 'Scroll of Level 5 Spell' ,
                              13 : 'Gallows Tooth' ,
                              14 : 'Iron Medallion' ,
                              15 : 'Vanishing Coin'},
             '10th Level' : { 1 : 'Penetrating Ammunition' ,
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
                              5 : 'Scroll of Level 6 Spell' ,
                              6 : 'Mending Lattice'},
             '12th Level' : { 1 : 'Greater Explosive Ammunition' ,
                              2 : 'Greater Elixir of Life' ,
                              3 : 'Slumber Poison' ,
                              4 : 'Adult Dragons Breath Potion' ,
                              5 : 'Major Healing Potion' ,
                              6 : 'Alabaster Reliquary' ,
                              7 : 'Dazinf Tremblant' ,
                              8 : 'Obsidian Reliquary'},
             '13th Level' : { 1 : 'Spellstrike Ammunition 6th' ,
                              2 : 'Greater Bestial Mutagen' ,
                              3 : 'Greater Bullheaded Mutagen' ,
                              4 : 'Greater Cognitive Mutagen' ,
                              5 : 'Greater Juggernaut Mutagen' ,
                              6 : 'Greater Quicksilver Mutagen' ,
                              7 : 'Greater Silvertounge Mutagen' ,
                              8 : 'Deathcap Powder' ,
                              9 : 'Purple Worm Venom' ,
                              10 : 'Greater Potion of Resistance' ,
                              11 : 'Panacea' ,
                              12 : 'Scroll of Level 7 Spell' ,
                              13 : 'Sunstone Beads'},
             '14th Level' : { 1 : 'Ghost Ammunition' ,
                              2 : 'Stone Bullet' ,
                              3 : 'Greater Potion of Flying' ,
                              4 : 'TrueSight Potion' ,
                              5 : 'Vipers Fang'},
             '15th Level' : { 1 : 'Disintergration Bolt' ,
                              2 : 'Spellstrike Ammunition 7th' ,
                              3 : 'Obfuscation Oil' ,
                              4 : 'Dragon Bile' ,
                              5 : 'Insanity Mist' ,
                              6 : 'Scroll of Level 8 Spell' ,
                              7 : 'Ghost Dust'},
             '16th Level' : { 1 : 'True Elixir of Life' ,
                              2 : 'Brimstone Fumes' ,
                              3 : 'Nightmare Vapor'},
             '17th Level' : { 1 : 'Spellstrike Ammunition 8th' ,
                              2 : 'True Bestial Mutagen' ,
                              3 : 'True Bullhead Mutagen' ,
                              4 : 'True Cognitive Mutagen' ,
                              5 : 'True Juggernaut Mutagen' ,
                              6 : 'True Quicksilver Mutagen' ,
                              7 : 'True Silvertounge Mutagen' ,
                              8 : 'Hemlock' ,
                              9 : 'Wyrm Dragons Breath Potion' ,
                              10 :'Scroll of Level 9 Spell' ,
                              11 : 'Spell Sliver'},
             '18th Level' : { 1 : 'Kings Sleep'},
             '19th Level' : { 1 : 'Spellstrike Ammunition 9th' ,
                              2 : 'Black Lotus Extract'},
             '20th Level' : { 1 : 'Elixir of Rejuvination' ,
                              2 : 'Antimagic Oil' ,
                              3 : 'Tears of Death' ,
                              4 : 'Philosophers Stone'}}

magic_type = 0
consumable_type = 0
max_spell_level = 0

class Level_one () :
    def __init__ (self) :
        for x in range(int(12)) :
            x = randint(1, len(Consumable['1st Level']))
            Con_treasure.append(Consumable['1st Level'][x])
            if x == 23: 
                Spells.spell_roll()
        for x in range(int(4)) :
            x = randint(1, len(Consumable['2nd Level']))
            Con_treasure.append(Consumable['2nd Level'][x])
            if x == 17: 
                Spells.spell_roll()
        for x in range(int(2)) :
            x = randint(1, len(Consumable['3rd Level'])) 
            Con_treasure.append(Consumable['3rd Level'][x])
            if x == 17: 
                Spells.spell_roll()
class Level_one_extra () :
    def __init__ (self) :
        x = randint(1, len(Consumable['1st Level']))
        Con_treasure.append(Consumable['1st Level'][x])
        if x == 23: 
                Spells.spell_roll()
        for x in range(2) :
            x = randint(1,2)
            if x == 1 :
                x = randint(1, len(Consumable['2nd Level']))
                Con_treasure.append(Consumable['2nd Level'][x])
                if x == 17: 
                    Spells.spell_roll()
            else :
                x = randint(1, len(Consumable['3rd Level'])) 
                Con_treasure.append(Consumable['3rd Level'][x])
                if x == 17: 
                    Spells.spell_roll()
class Level_two () : 
    def __init__ (self) :
        x = randint(1, len(Consumable['1st Level']))
        Con_treasure.append(Consumable['1st Level'][x])
        if x == 23: 
            Spells.spell_roll()  
        x = randint(1, len(Consumable['2nd Level']))
        Con_treasure.append(Consumable['2nd Level'][x])
        if x == 17: 
            Spells.spell_roll()          
        x = randint(1, len(Consumable['3rd Level'])) 
        Con_treasure.append(Consumable['3rd Level'][x]) 
        if x == 17: 
            Spells.spell_roll()            
class Level_two_extra () : 
    def __init__ (self) :
        for x in range(int(1)) :
            x = randint(1, len(Consumable['2nd Level']))
            Con_treasure.append(Consumable['2nd Level'][x])
            if x == 17: 
                Spells.spell_roll()           
        for x in range(2) :
            x = randint(1,2)
            if x == 1 :
                x = randint(1, len(Consumable['2nd Level']))
                Con_treasure.append(Consumable['2nd Level'][x])
                if x == 17: 
                    Spells.spell_roll()                   
            else :
                x = randint(1, len(Consumable['3rd Level'])) 
                Con_treasure.append(Consumable['3rd Level'][x])
                if x == 17: 
                    Spells.spell_roll()                   
class Level_three () : 
    def __init__ (self) :
        for x in range(int(2)) :
            x = randint(1, len(Consumable['2nd Level']))
            Con_treasure.append(Consumable['2nd Level'][x])
            if x == 17: 
                Spells.spell_roll()          
        for x in range(int(6)) :
            x = randint(1, len(Consumable['3rd Level'])) 
            Con_treasure.append(Consumable['3rd Level'][x])
            if x == 17: 
                Spells.spell_roll()         
        for x in range(int(4)) :
            x = randint(1, len(Consumable['4th Level'])) 
            Con_treasure.append(Consumable['4th Level'][x]) 
            if x == 7: 
                Spells.spell_roll()               
class Level_three_extra () : 
    def __init__ (self) :
        x = randint(1, len(Consumable['3rd Level'])) 
        Con_treasure.append(Consumable['3rd Level'][x])
        if x == 17: 
            Spells.spell_roll()         
        for x in range(2) :
            x = randint(1,2)
            if x == 1 :
                x = randint(1, len(Consumable['3rd Level'])) 
                Con_treasure.append(Consumable['3rd Level'][x])
                if x == 17: 
                    Spells.spell_roll()                 
            else :
                x = randint(1, len(Consumable['4th Level'])) 
                Con_treasure.append(Consumable['4th Level'][x])
                if x == 7: 
                    Spells.spell_roll()                  
class Level_four () : 
    def __init__ (self) :
        for x in range(int(2)) :
            x = randint(1, len(Consumable['3rd Level'])) 
            Con_treasure.append(Consumable['3rd Level'][x])
            if x == 17: 
                Spells.spell_roll()           
        for x in range(int(4)) :
            x = randint(1, len(Consumable['4th Level'])) 
            Con_treasure.append(Consumable['4th Level'][x])
            if x == 7: 
                Spells.spell_roll()         
        for x in range(int(4)) :
            x = randint(1, len(Consumable['5th Level'])) 
            Con_treasure.append(Consumable['5th Level'][x])
            if x == 17: 
                Spells.spell_roll()           
class Level_four_extra () : 
    def __init__ (self) :
        x = randint(1, len(Consumable['4th Level'])) 
        Con_treasure.append(Consumable['4th Level'][x])
        if x == 7: 
            Spells.spell_roll()        
        for x in range(2) :
            x = randint(1,2)
            if x == 1 :
                x = randint(1, len(Consumable['4th Level'])) 
                Con_treasure.append(Consumable['4th Level'][x])
                if x == 7: 
                    Spells.spell_roll()                
            else :
                x = randint(1, len(Consumable['5th Level'])) 
                Con_treasure.append(Consumable['5th Level'][x])
                if x == 17: 
                    Spells.spell_roll()           
class Level_five () : 
    def __init__ (self) :
        for x in range(int(2)) :
            x = randint(1, len(Consumable['4th Level'])) 
            Con_treasure.append(Consumable['4th Level'][x])
            if x == 7: 
                Spells.spell_roll()         
        for x in range(int(6)) :
            x = randint(1, len(Consumable['5th Level'])) 
            Con_treasure.append(Consumable['5th Level'][x])
            if x == 17: 
                Spells.spell_roll()         
        for x in range(int(2)) :
            x = randint(1, len(Consumable['6th Level'])) 
            Con_treasure.append(Consumable['6th Level'][x])
            if x == 10: 
                Spells.spell_roll()        
class Level_five_extra () : 
    def __init__ (self) :
        x = randint(1, len(Consumable['5th Level'])) 
        Con_treasure.append(Consumable['5th Level'][x])
        if x == 17: 
            Spells.spell_roll()  
        for x in range(2) :
            x = randint(1,2)
            if x == 1 :
                x = randint(1, len(Consumable['5th Level'])) 
                Con_treasure.append(Consumable['5th Level'][x])
                if x == 17: 
                    Spells.spell_roll()             
            else :
                x = randint(1, len(Consumable['6th Level'])) 
                Con_treasure.append(Consumable['6th Level'][x])
                if x == 10: 
                    Spells.spell_roll()            
class Level_six () : 
    def __init__ (self) :
        for x in range(int(2)) :
            x = randint(1, len(Consumable['5th Level'])) 
            Con_treasure.append(Consumable['5th Level'][x])
            if x == 17: 
                Spells.spell_roll() 
        for x in range(int(4)) :
            x = randint(1, len(Consumable['6th Level'])) 
            Con_treasure.append(Consumable['6th Level'][x])
            if x == 10: 
                Spells.spell_roll()
        for x in range(int(2)) :
            x = randint(1, len(Consumable['7th Level'])) 
            Con_treasure.append(Consumable['7th Level'][x])
            if x == 8: 
                Spells.spell_roll()    
class Level_six_extra () : 
    def __init__ (self) :
        x = randint(1, len(Consumable['6th Level'])) 
        Con_treasure.append(Consumable['6th Level'][x])
        if x == 10: 
            Spells.spell_roll()    
        for x in range(2) :
            x = randint(1,2)
            if x == 1 :
                x = randint(1, len(Consumable['6th Level'])) 
                Con_treasure.append(Consumable['6th Level'][x])
                if x == 10: 
                    Spells.spell_roll()            
            else :
                x = randint(1, len(Consumable['7th Level'])) 
                Con_treasure.append(Consumable['7th Level'][x])
                if x == 8: 
                    Spells.spell_roll()              
class Level_seven () : 
    def __init__ (self) :
        for x in range(int(2)) :
            x = randint(1, len(Consumable['6th Level'])) 
            Con_treasure.append(Consumable['6th Level'][x])
            if x == 10: 
                Spells.spell_roll()     
        for x in range(int(2)) :
            x = randint(1, len(Consumable['7th Level'])) 
            Con_treasure.append(Consumable['7th Level'][x])
            if x == 8: 
                Spells.spell_roll()    
        for x in range(int(4)) :
            x = randint(1, len(Consumable['8th Level'])) 
            Con_treasure.append(Consumable['8th Level'][x])
            if x == 12: 
                Spells.spell_roll() 
class Level_seven_extra () : 
    def __init__ (self) :
        x = randint(1, len(Consumable['7th Level'])) 
        Con_treasure.append(Consumable['7th Level'][x])
        if x == 8: 
            Spells.spell_roll()        
        for x in range(2) :
            x = randint(1,2)
            if x == 1 :
                x = randint(1, len(Consumable['7th Level'])) 
                Con_treasure.append(Consumable['7th Level'][x])
                if x == 8: 
                    Spells.spell_roll()               
            else :
                x = randint(1, len(Consumable['8th Level'])) 
                Con_treasure.append(Consumable['8th Level'][x])
                if x == 12: 
                    Spells.spell_roll()                
class Level_eight () : 
    def __init__ (self) :
        for x in range(int(2)) :
            x = randint(1, len(Consumable['7th Level'])) 
            Con_treasure.append(Consumable['7th Level'][x])
            if x == 8: 
                Spells.spell_roll()     
        for x in range(int(4)) :
            x = randint(1, len(Consumable['8th Level'])) 
            Con_treasure.append(Consumable['8th Level'][x])
            if x == 12: 
                Spells.spell_roll()      
        for x in range(int(2)) :
            x = randint(1, len(Consumable['9th Level'])) 
            Con_treasure.append(Consumable['9th Level'][x])
            if x == 12: 
                Spells.spell_roll()         
class Level_eight_extra () : 
    def __init__ (self) :
        x = randint(1, len(Consumable['8th Level'])) 
        Con_treasure.append(Consumable['8th Level'][x])
        if x == 12: 
            Spells.spell_roll()    
        for x in range(2) :
            x = randint(1,2)
            if x == 1 :
                x = randint(1, len(Consumable['8th Level'])) 
                Con_treasure.append(Consumable['8th Level'][x])
                if x == 12: 
                    Spells.spell_roll()                  
            else :
                x = randint(1, len(Consumable['9th Level'])) 
                Con_treasure.append(Consumable['9th Level'][x])
                if x == 12: 
                    Spells.spell_roll()              
class Level_nine () : 
    def __init__ (self) :
        for x in range(int(2)) :
            x = randint(1, len(Consumable['8th Level'])) 
            Con_treasure.append(Consumable['8th Level'][x])
            if x == 12: 
                Spells.spell_roll() 
        for x in range(int(4)) :
            x = randint(1, len(Consumable['9th Level'])) 
            Con_treasure.append(Consumable['9th Level'][x])
            if x == 12: 
                Spells.spell_roll()    
        for x in range(int(2)) :
            x = randint(1, len(Consumable['10th Level'])) 
            Con_treasure.append(Consumable['10th Level'][x]) 
class Level_nine_extra () : 
    def __init__ (self) :
        x = randint(1, len(Consumable['9th Level'])) 
        Con_treasure.append(Consumable['9th Level'][x])
        if x == 12: 
            Spells.spell_roll()
        for x in range(2) :
            x = randint(1,2)
            if x == 1 :
                for x in range(int(b)) :
                    x = randint(1, len(Consumable['9th Level'])) 
                    Con_treasure.append(Consumable['9th Level'][x])
                    if x == 12: 
                        Spells.spell_roll()                
            else :
                for x in range(int(c)) :
                    x = randint(1, len(Consumable['10th Level'])) 
                    Con_treasure.append(Consumable['10th Level'][x])
class Level_ten () : 
    def __init__ (self) :
        for x in range(int(2)) :
            x = randint(1, len(Consumable['9th Level'])) 
            Con_treasure.append(Consumable['9th Level'][x])
            if x == 12: 
                Spells.spell_roll()     
        for x in range(int(4)) :
            x = randint(1, len(Consumable['10th Level'])) 
            Con_treasure.append(Consumable['10th Level'][x])
        for x in range(int(2)) :
            x = randint(1, len(Consumable['11th Level'])) 
            Con_treasure.append(Consumable['11th Level'][x])
            if x == 5: 
                Spells.spell_roll()        
class Level_ten_extra () : 
    def __init__ (self) :
        x = randint(1, len(Consumable['10th Level'])) 
        Con_treasure.append(Consumable['10th Level'][x])
        for x in range(2) :
            x = randint(1,2)
            if x == 1 :
                x = randint(1, len(Consumable['10th Level'])) 
                Con_treasure.append(Consumable['10th Level'][x])
            else :
                x = randint(1, len(Consumable['11th Level'])) 
                Con_treasure.append(Consumable['11th Level'][x])
                if x == 5: 
                    Spells.spell_roll()         
class Level_eleven () : 
    def __init__ (self) :
        for x in range(int(2)) :
            x = randint(1, len(Consumable['10th Level']))
            Con_treasure.append(Consumable['10th Level'][x])
        for x in range(int(4)) :
            x = randint(1, len(Consumable['11th Level']))
            Con_treasure.append(Consumable['11th Level'][x])
            if x == 5: 
                Spells.spell_roll()       
        for x in range(int(2)) :
            x = randint(1, len(Consumable['12th Level']))
            Con_treasure.append(Consumable['12th Level'][x]) 
class Level_eleven_extra () : 
    def __init__ (self) :
        x = randint(1, len(Consumable['11th Level']))
        Con_treasure.append(Consumable['11th Level'][x])
        if x == 5: 
            Spells.spell_roll()       
        for x in range(2) :
            x = randint(1,2)
            if x == 1 :
                x = randint(1, len(Consumable['11th Level']))
                Con_treasure.append(Consumable['11th Level'][x])
                if x == 5: 
                    Spells.spell_roll()                  
            else :
                x = randint(1, len(Consumable['12th Level']))
                Con_treasure.append(Consumable['12th Level'][x])
class Level_twelve () : 
    def __init__ (self) :
        for x in range(int(6)) :
            x = randint(1, len(Consumable['12th Level']))
            Con_treasure.append(Consumable['12th Level'][x])
        for x in range(int(2)) :
            x = randint(1, len(Consumable['13th Level']))
            Con_treasure.append(Consumable['13th Level'][x])
            if x == 12: 
                Spells.spell_roll()      
class Level_twelve_extra () : 
    def __init__ (self) :
        x = randint(1, len(Consumable['12th Level']))
        Con_treasure.append(Consumable['12th Level'][x])
        for x in range(2) :
            x = randint(1,2)
            if x == 1 :
                x = randint(1, len(Consumable['12th Level']))
                Con_treasure.append(Consumable['12th Level'][x])
            else :
                x = randint(1, len(Consumable['13th Level']))
                Con_treasure.append(Consumable['13th Level'][x])
                if x == 12: 
                    Spells.spell_roll()             
class Level_thirteen () : 
    def __init__ (self) :
        for x in range(int(2)) :
            x = randint(1, len(Consumable['12th Level']))
            Con_treasure.append(Consumable['12th Level'][x])
        for x in range(int(4)) :
            x = randint(1, len(Consumable['13th Level']))
            Con_treasure.append(Consumable['13th Level'][x])
            if x == 12: 
                Spells.spell_roll()        
        for x in range(int(2)) :
            x = randint(1, len(Consumable['14th Level']))
            Con_treasure.append(Consumable['14th Level'][x]) 
class Level_thirteen_extra () : 
    def __init__ (self) :
        x = randint(1, len(Consumable['13th Level']))
        Con_treasure.append(Consumable['13th Level'][x])
        if x == 12: 
            Spells.spell_roll()     
        for x in range(2) :
            x = randint(1,2)
            if x == 1 :
                x = randint(1, len(Consumable['13th Level']))
                Con_treasure.append(Consumable['13th Level'][x])
                if x == 12: 
                    Spells.spell_roll()                
            else :
                x = randint(1, len(Consumable['14th Level']))
                Con_treasure.append(Consumable['14th Level'][x])
class Level_fourteen () : 
    def __init__ (self) :
        for x in range(int(2)) :
            x = randint(1, len(Consumable['13th Level']))
            Con_treasure.append(Consumable['13th Level'][x])
            if x == 12: 
                Spells.spell_roll()    
        for x in range(int(4)) :
            x = randint(1, len(Consumable['14th Level']))
            Con_treasure.append(Consumable['14th Level'][x])
        for x in range(int(2)) :
            x = randint(1, len(Consumable['15th Level']))
            Con_treasure.append(Consumable['15th Level'][x])
            if x == 6: 
                Spells.spell_roll()       
class Level_fourteen_extra () : 
    def __init__ (self) :
        x = randint(1, len(Consumable['14th Level']))
        Con_treasure.append(Consumable['14th Level'][x])
        for x in range(2) :
            x = randint(1,2)
            if x == 1 :
                x = randint(1, len(Consumable['14th Level']))
                Con_treasure.append(Consumable['14th Level'][x])
            else :
                x = randint(1, len(Consumable['15th Level']))
                Con_treasure.append(Consumable['15th Level'][x])
                if x == 6: 
                    Spells.spell_roll()                
class Level_fifteen () : 
    def __init__ (self) :
        for x in range(int(2)) :
            x = randint(1, len(Consumable['14th Level']))
            Con_treasure.append(Consumable['14th Level'][x])
        for x in range(int(4)) :
            x = randint(1, len(Consumable['15th Level']))
            Con_treasure.append(Consumable['15th Level'][x])
            if x == 6: 
                Spells.spell_roll()        
        for x in range(int(2)) :
            x = randint(1, len(Consumable['16th Level']))
            Con_treasure.append(Consumable['16th Level'][x]) 
class Level_fifteen_extra () : 
    def __init__ (self) :
        x = randint(1, len(Consumable['15th Level']))
        Con_treasure.append(Consumable['15th Level'][x])
        if x == 6: 
            Spells.spell_roll()     
        for x in range(2) :
            x = randint(1,2)
            if x == 1 :
                x = randint(1, len(Consumable['15th Level']))
                Con_treasure.append(Consumable['15th Level'][x])
                if x == 6: 
                    Spells.spell_roll()               
            else :
                x = randint(1, len(Consumable['16th Level']))
                Con_treasure.append(Consumable['16th Level'][x])
class Level_sixteen () : 
    def __init__ (self) :
        for x in range(int(4)) :
            x = randint(1, len(Consumable['16th Level']))
            Con_treasure.append(Consumable['16th Level'][x])
        for x in range(int(2)) :
            x = randint(1, len(Consumable['17th Level']))
            Con_treasure.append(Consumable['17th Level'][x])
            if x == 6: 
                Spells.spell_roll()      
class Level_sixteen_extra () : 
    def __init__ (self) :
        x = randint(1, len(Consumable['16th Level']))
        Con_treasure.append(Consumable['16th Level'][x])
        for x in range(2) :
            x = randint(1,2)
            if x == 1 :
                x = randint(1, len(Consumable['16th Level']))
                Con_treasure.append(Consumable['16th Level'][x])
            else :
                x = randint(1, len(Consumable['17th Level']))
                Con_treasure.append(Consumable['17th Level'][x])
                if x == 6: 
                    Spells.spell_roll()                             
class Level_seventeen () : 
    def __init__ (self) :
        for x in range(int(4)) :
            x = randint(1, len(Consumable['17th Level']))
            Con_treasure.append(Consumable['17th Level'][x])
            if x == 6: 
                Spells.spell_roll()                  
        for x in range(int(2)) :
            x = randint(1, len(Consumable['18th Level']))
            Con_treasure.append(Consumable['18th Level'][x]) 
class Level_seventeen_extra () : 
    def __init__ (self) :
        x = randint(1, len(Consumable['17th Level']))
        Con_treasure.append(Consumable['17th Level'][x])
        if x == 6: 
            Spells.spell_roll()                  
        for x in range(2) :
            x = randint(1,2)
            if x == 1 :
                x = randint(1, len(Consumable['17th Level']))
                Con_treasure.append(Consumable['17th Level'][x])
                if x == 6: 
                    Spells.spell_roll()                            
            else :
                Con_treasure.append(Consumable['18th Level'][1])
class Level_eighteen () : 
    def __init__ (self) :
        for x in range(int(4)) :
            x = randint(1, len(Consumable['18th Level']))
            Con_treasure.append(Consumable['18th Level'][1])
        for x in range(int(2)) :
            x = randint(1,2)
            Con_treasure.append(Consumable['19th Level'][x])
class Level_eighteen_extra () : 
    def __init__ (self) :
        Con_treasure.append(Consumable['18th Level'][1])
        for x in range(2) :
            x = randint(1,2)
            if x == 1 :
                Con_treasure.append(Consumable['18th Level'][1])
            else :
                x = randint(1, len(Consumable['19th Level']))
                Con_treasure.append(Consumable['19th Level'][x])
class Level_nineteen () : 
    def __init__ (self) :
        for x in range(int(4)) :
            x = randint(1, len(Consumable['19th Level']))
            Con_treasure.append(Consumable['19th Level'][x])
        for x in range(int(2)) :
            x = randint(1, len(Consumable['20th Level']))
            Con_treasure.append(Consumable['20th Level'][x]) 
class Level_nineteen_extra () : 
    def __init__ (self) :
        x = randint(1, len(Consumable['19th Level']))
        Con_treasure.append(Consumable['19th Level'][x])
        for x in range(2) :
            x = randint(1,2)
            if x == 1 :
                x = randint(1, len(Consumable['19th Level']))
                Con_treasure.append(Consumable['19th Level'][x])
            else :
                x = randint(1, len(Consumable['20th Level']))
                Con_treasure.append(Consumable['20th Level'][x])
class Level_twenty () : 
    def __init__ (self) :
        for x in range(int(4)) :
            x = randint(1, len(Consumable['20th Level']))
            Con_treasure.append(Consumable['20th Level'][x])
class Level_twenty_extra () : 
    def __init__ (self) :
        b = 1
        c = 1
        for x in range(int(b)) :
            x = randint(1,4)
            Con_treasure.append(Consumable['20th Level'][x])
        for x in range(2) :
            x = randint(1,2)
            if x == 1 :
                for x in range(int(b)) :
                    x = randint(1,2)
                    Con_treasure.append(Consumable['19th Level'][x])
            else :
                for x in range(int(c)) :
                    x = randint(1,4) 
                    Con_treasure.append(Consumable['20th Level'][x])                                                                                                                                                                                    
