from random import *

Perm_treasure = []
Permanent = {'2nd Level' : { 1 : 'Expert Light Wooden Sturdy Shield' ,
                             2 : 'Wand of 1st Level spell' ,
                             3 : 'Bracers of Armor 1st',
                             4 : 'Broach of Shielding' ,
                             5 : 'Expert Handwraps of Mighty Fists' ,
                             6 : 'Hand of the Mage' , 
                             7 : 'Hat of disguise'},
             '3rd Level' : { 1 : '+1 Magic light or medium Armor' ,
                             2 : 'Cold Iron Warhammer' ,
                             3 : 'Silver Dagger' ,
                             4 : '+1 Light or Medium Armor Potency' ,
                             5 : 'Lesser Mentalists Staff' ,
                             6 : 'Lesser Staff of Fire' ,
                             7 : 'Minor Staff of Healing' ,
                             8 : 'Bracers of Missle Deflection' ,
                             9 : 'Doubling Rings'},
             '4th Level' : { 1 : 'Bag of Holding Type 1' ,
                             2 : '+1 Magic Heavy Armor' ,
                             3 : 'Ghost Touch' ,
                             4 : '+1 Heavy Armor Potency' ,
                             5 : 'Returning' ,
                             6 : 'Slick' ,
                             7 : '+1 Weapon Potency' ,
                             8 : 'Expert Light Steel Sturdy Shield' ,
                             9 : 'Wand of 2nd Level Spell' ,
                             10 : '+1 Magic Weapon' ,
                             11 : 'Bracers of Armor 2nd' ,
                             12 : '+1 Handwraps of Mighty Fists'} ,
             '5th Level' : { 1 : 'Ghoul Hide' ,
                             2 : 'Divine Prayer Beads' ,
                             3 : 'Skeleton Key' ,
                             4 : 'Thurible of Revelation' ,
                             5 : 'Distrupting' ,
                             6 : 'Glamered' ,
                             7 : 'Shifting' ,
                             8 : 'Expert Heavy Wooden Sturdy Shield' ,
                             9 : 'Lesser Staff of Abjuration' ,
                             10 : 'Lesser Staff of Conjuration' ,
                             11 : 'Lesser Staff of Divination' ,
                             12 : 'Lesser Staff of Enchantment' ,
                             13 : 'Lesser Staff of Evocation' ,
                             14 : 'Lesser Staff of Illsuion' ,
                             15 : 'Lesser Staff of Necromancy' ,
                             16 : 'Lesser Staff of Transmutation' ,
                             17 : 'Verdant Staff' ,
                             18 : 'Dagger of Venom' ,
                             19 : 'Fighters Fork' ,
                             20 : 'Clandestine Cloak' ,
                             21 : 'Coyote Cloak' ,
                             22 : 'Crafters Eyepiece' ,
                             23 : 'Hat of the Magi' ,
                             24 : 'Necklace of Fireballs Type 1' ,
                             25 : 'Persona Mask' ,
                             26 : 'Pyhlactery of the Occult' , 
                             27 : 'Ring of the Ram' ,
                             28 : 'Tracker Goggles'},
             '6th Level' : { 1 : 'Chime of Opening' ,
                             2 : 'Primeval Mistletoe' ,
                             3 : 'Traverlers Any-Tool' ,
                             4 : 'Wounding' ,
                             5 : 'Lions Shield' ,
                             6 : 'Spellguard Shield' ,
                             7 : 'Bloodletting Kukri' ,
                             8 : 'Boots of Elvenkind' ,
                             9 : 'Choker of Elocution' ,
                             10 : 'Dancing Scarf' ,
                             11 : 'Demon Mask ' ,
                             12 : 'Eyes of the Eagle' ,
                             13 : 'Googles of Night' ,
                             14 : 'Greater Hat of Disguise' ,
                             15 : 'Lesser Ring of Energy' ,
                             16 : 'Ring of Lies' ,
                             17 : 'Slippers of Spider-Climb' ,
                             18 : 'Tourmaline Spehere Aeon Stone'},
             '7th Level' : { 1 : '+2 Magic Armor' ,
                             2 : 'Bag of Holding Type 2' ,
                             3 : 'Bottled Air' ,
                             4 : '+2 Armor Potency' ,
                             5 : 'Expert Heavy Steel Sturdy Shield' ,
                             6 : 'Mentalists Staff' ,
                             7 : 'Staff of Fire' ,
                             8 : 'Lesser Staff of Healing' ,
                             9 : 'Alchecmist Goggles' ,
                             10 : 'Boots of Bounding' ,
                             11 : 'Gloves of Storing' ,
                             12 : 'Healers Gloves' ,
                             13 : 'Lesser Ring of Wizardry' ,
                             14 : 'Master Handwraps of Mighty Fists' ,
                             15 : 'Necklace of Fireballs Type 2' , 
                             16 : 'Phylactery of Faithfulness'},
             '8th Level' : { 1 : '+2 Weapon Potency' ,
                             2 : 'Invisibility' ,
                             3 : '+2 Magic Weapon' ,
                             4 : 'Bracers of Armor 4th' ,
                             5 : 'Clear Spindle Aeon Stone' ,
                             6 : '+2 Handwraps of Mighty Fists' ,
                             7 : 'Lesser Spell Duelists Gloves' ,
                             8 : 'Lesser Spell Duelists Wand' ,
                             9 : 'Horeshoes of Speed'},
             '9th Level' : { 1 : 'Rhino Hide' ,
                             2 : 'Collar of Inconspicuousness' ,
                             3 : 'Horn of Blasting' ,
                             4 : 'Immovable Rod' ,
                             5 : 'Adamantine Battleaxe' ,
                             6 : 'Corrosive' ,
                             7 : 'Energy Resistance' ,
                             8 : 'Flaming' ,
                             8 : 'Frost' ,
                             10 : 'Shock' ,
                             11 : 'Dragonslayers Shield' ,
                             12 : 'Forge Warden' ,
                             13 : 'MasterHeavy Steel Sturdy Shield' ,
                             14 : 'Staff of Abjuration' ,
                             15 : 'Staff of Conjuration' ,
                             16 : 'Staff of Divination' ,
                             17 : 'Staff of Enchantment' ,
                             18 : 'Staff of Evocation' ,
                             19 : 'Staff of Illusion' ,
                             20 : 'Staff of Necromancy' ,
                             21 : 'Staff of Transmutation' ,
                             22 : 'Gloom Blade' ,
                             23 : 'Armbands of Athleticism' ,
                             24 : 'Belt of the Five Kings' ,
                             25 : 'Cloak of the Bat' ,
                             26 : 'Knapsack of Halflingkind' ,
                             27 : 'Necklace of Fireballs Type 3' ,
                             28 : 'Ring of Wizardry'},
            '10th level' : { 1 : 'Breatplate of Command' ,
                             2 : 'Celestial Armor' ,
                             3 : 'Demon Armor' ,
                             4 : 'Electric Eelskin' ,
                             5 : 'Maestros Instrument' ,
                             6 : 'Greater Invisibility' ,
                             7 : 'Master Light Adamantine Sturdy Shield' ,
                             8 : 'Flame Toungue' ,
                             9 : 'Oathbow' ,
                             10 : 'Cloak of Elvenkind' ,
                             11 : 'Daredevil Boots' ,
                             12 : 'Druids Vestments' ,
                             13 : 'Gold Nodule Aeon Stone' ,
                             14 : 'Greater Goggles of Night' ,
                             15 : 'Messengers Ring' ,
                             16 : 'Ring of Energy Resistance' ,
                             17 : 'Ring of Counterspells' ,
                             18 : 'Ring of Maniacal Devices'},
            '11th Level' : { 1 : '+3 Magic Armor' ,
                             2 : 'Bag of Holding Type 3' ,
                             3 : 'Greater Divine Prayer Beads' ,
                             4 : 'Anarchic' ,
                             5 : '+3 Armor Potency' ,
                             6 : 'Axiomatic' ,
                             7 : 'Holy' ,
                             8 : 'Unholy' ,
                             9 : 'Arrow-Catching Shield' ,
                             10 : 'Greater Verdant Staff' ,
                             11 : 'Greater Staff of Fire' ,
                             12 : 'Staff of Healing' ,
                             13 : 'Greater Verdant Staff' ,
                             14 : 'Cape of the Mountbank' ,
                             15 : 'Gorget of the Primal Roar' ,
                             16 : 'Greater Doubling Rings' ,
                             17 : 'Necklace of the Fireballs Type 4' ,
                             18 : 'Robe of the Archmage'},
            '12th Level' : { 1 :'Mail of Luck' ,
                             2 : 'Doctors Marvelous Medicine' ,
                             3 : 'Master Eleven Chain' ,
                             4 : 'Mithril Chain Shirt' ,
                             5 : 'Fortification' ,
                             6 : '+3 Weapon Potency' ,
                             7 : 'Master Heavy Adimantine Sturdy Shield' ,
                             8 : '+3 Magic Weapon' ,
                             9 : 'Bracers of Armor 6th' ,
                             10 : 'Greater Ring of the Ram' ,
                             11 : 'Greater Ring of Wizardry',
                             12 : '+3 Handwraps of Mighty Fists', 
                             13 : 'Pink Rhomboid Aeon Stone' ,
                             14 : 'Ring of Climbing' ,
                             15 : 'Ring of Swimming' ,
                             16 : 'Spell Duelists Gloves' ,
                             17 : 'Spell Duelists Wand' ,
                             18 : 'Winged Boots'},
            '13th Level' : { 1 : 'Plate of the Deep' ,
                             2 : 'Barding of the Zephyr' ,
                             3 : 'Bag of Holding 4' ,
                             4 : 'Greater Skeleton Key',
                             5 : 'Greater Energy Resistance' ,
                             6 : 'Greater Slick' ,
                             7 : 'Keen' ,
                             8 : 'Spell Storing' ,
                             9 : 'Floating Shield' ,
                             10 : 'Greater Staff of Abjuration' ,
                             11 : 'Greater Staff of Conjuration' ,
                             12 : 'Greater Staff of Divination' ,
                             13 : 'Greater Staff of Enchantment' ,
                             14 : 'Greater Staff of Evocation' ,
                             15 : 'Greater Staff of Illusion' ,
                             16 : 'Greater Staff of Necromancy' ,
                             17 : 'Greater Staff of Transmutation' ,
                             18 : 'Dwarven Thrower' ,
                             19 : 'Greater Boots of Elvenkind' ,
                             20 : 'Greater Choker ofELocution' ,
                             21 : 'Greater Clandestine Cloak' ,
                             22 : 'Greater Coyote Cloak' ,
                             23 : 'Greater Crafters Eyepiece' ,
                             24 : 'Phylactery of Faithfulness' ,
                             25 : 'Greater Ring of Lies' ,
                             26 : 'Greater Trackers Goggles' ,
                             27 : 'Necklace of Fireballs type 5' ,
                             28 : 'Pale Lavender Ellipsoid Aeon Stone'},
            '14th Level' : { 1 : 'Greater Horsehoes of Speed' ,
                             2 : 'Antimagic' ,
                             3 : 'Dancing' ,
                             4 : 'Greater Corrosive' ,
                             5 : 'Greater Flaming' ,
                             6 : 'Greater Frost' ,
                             7 : 'Greater Shadow' ,
                             8 : 'Greater Shock' ,
                             9 : 'Holy Avenger' ,
                             10 : 'Anklets of Alacrity' ,
                             11 : 'Belt of Giant Strength' ,
                             12 : 'Belt of Regeneration' ,
                             13 : 'Circlet of Persuasion' ,
                             14 : 'Diadem of Intellect' ,
                             15 : 'Greater boots of bounding' ,
                             16 : 'Greater Cloak of the Bat' ,
                             17 : 'Greater Dancing Scarf' ,
                             18 : 'Greater Demon Mask' ,
                             19 : 'Greater Hat of the Magi' ,
                             20 : 'Greater Phylactery of the Occult' ,
                             21 : 'Greater Ring of Energy Resistance' ,
                             22 : 'Headband of Inspiring Wisdom' ,
                             23 : 'Major ring of Wizardry' ,
                             24 : 'Greater Primeol Mistletoe'},
            '15th Level' : { 1 : '+4 Magic Armor' ,
                             2 : '+4 Armor Potency' ,
                             3 : 'Greater Disrupting' ,
                             4 : 'Void' ,
                             5 : 'Greater Staff of Healing' ,
                             6 : 'Greater Healers Gloves' ,
                             7 : 'Greater Persona Mask' ,
                             8 : 'Legendary Handwraps of Mighty Fists' ,
                             9 : 'Necklace of Fireballs Type 6'},
            '16th Level' : { 1 : 'Greater Thurible of Revelation' ,
                             2 : 'Speed' ,
                             3 : '+ 4 Weapon Potency' ,
                             4 : 'Staff of Power' ,
                             5 : 'Bracers of Armor 8th' ,
                             6 : 'Greater Alchemist Goggles' ,
                             7 : 'Greater Spell Duelists Gloves' ,
                             8 : 'Greater Spell Duelists Wand' ,
                             9 : '+4 Handwras of Mighty Fists' ,
                             10 : 'Orange Prism Aeon Stone'},
            '17th Level' : { 1 : 'Ethereal' ,
                             2 : 'Vorpal' ,
                             3 : 'Legendary Heavy Steel Sturdy Shield' ,
                             4 : 'Reflecting Shield' ,
                             5 : 'Greater Armbands of Athelticism' ,
                             6 : 'Greater Daredevils Boots' ,
                             7 : 'Greater Messengers Ring' ,
                             8 : 'Necklace of Fireballs Type 7' ,
                             9 : 'Robe of Eyes' ,
                             10 : 'Whisper of the first lie'},
            '18th Level' : { 1 : 'Greater Doctors Marvelous Medicine' ,
                             2 : 'Possible Tome' ,
                             3 : 'Virtuosos instrument' ,
                             4 : 'Orichalcum Starknife' ,
                             5 : 'Greater Fortification' ,
                             6 : 'Indesructable Shield' ,
                             7 : 'Legendary Heavy Adamantine Sturdy Shield' ,
                             8 : 'Greater CLoack of Elvenkind' ,
                             9 : 'Greater Ring of ManiacalDevices'},
            '19th Level' : { 1 : '+5 Magic Armor' ,
                             2 : 'Legendary Elven Chain' ,
                             3 : '+5 Armor Potency' ,
                             4 : 'Luck Blade' ,
                             5 : 'Mattock of the Titans' ,
                             6 : 'Sky Hammer' ,
                             7 : 'Greater Robe of the Archmage' ,
                             8 : 'Inexplicable Apparatus' ,
                             9 : 'Lavender and Green Elipsoid Aeon Stone' ,
                             10 :'Third Eye'},
            '20th Level' : {1 : '+5 Weapon potency' ,
                            2 : '+5 Magic Weapon' ,
                            3 : 'Bracers of Armor +5' ,
                            4 : '+5 Handwraps of Mighty Fists' ,
                            5 : 'Supreme Spell Duelists Gloves' ,
                            6 : 'Supreme Spell Duelists Wand' ,
                            7 : 'Greater Whisper of the First Lie'}}

class Level_one () :
    def __init__ (self) :
        y = 1
        for x in range(int(y)) :
            x = randint(1,7)
            Perm_treasure.append(Permanent['2nd Level'][x])
class Level_one_extra () :
    def __init__ (self) :
        y = 1
        for x in range(int(y)) :
            x = randint(1,7)
            Perm_treasure.append(Permanent['2nd Level'][x])
class Level_two () : 
    def __init__ (self) :
        a = 2
        b = 1
        for x in range(int(a)) :
            x = randint(1,7)
            Perm_treasure.append(Permanent['2nd Level'][x])
        for x in range(int(b)) :
            x = randint(1,9) 
            Perm_treasure.append(Permanent['3rd Level'][x])  
class Level_two_extra () : 
    def __init__ (self) :
        a = 1
        for x in range(int(a)) :
            x = randint(1,7)
            Perm_treasure.append(Permanent['2nd Level'][x])
class Level_three () : 
    def __init__ (self) :
        a = 3
        b = 2
        for x in range(int(a)) :
            x = randint(1,9)
            Perm_treasure.append(Permanent['3rd Level'][x])
        for x in range(int(b)) :
            x = randint(1,12) 
            Perm_treasure.append(Permanent['4th Level'][x])  
class Level_three_extra () : 
    def __init__ (self) :
        a = 1
        for x in range(int(a)) :
            x = randint(1,9)
            Perm_treasure.append(Permanent['3rd Level'][x]) 
class Level_four () : 
    def __init__ (self) :
        a = 2
        b = 2
        for x in range(int(a)) :
            x = randint(1,12)
            Perm_treasure.append(Permanent['4th Level'][x])
        for x in range(int(b)) :
            x = randint(1,28) 
            Perm_treasure.append(Permanent['5th Level'][x])  
class Level_four_extra () : 
    def __init__ (self) :
        a = 1
        for x in range(int(a)) :
            x = randint(1,12)
            Perm_treasure.append(Permanent['4th Level'][x])
class Level_five () : 
    def __init__ (self) :
        a = 2
        b = 1
        c = 1
        for x in range(int(a)) :
            x = randint(1,28)
            Perm_treasure.append(Permanent['5th Level'][x])
        for x in range(int(c)) :
            x = randint(1,12)
            Perm_treasure.append(Permanent['4th Level'][x])        
        for x in range(int(b)) :
            x = randint(1,18) 
            Perm_treasure.append(Permanent['6th Level'][x])  
class Level_five_extra () : 
    def __init__ (self) :
        a = 1
        for x in range(int(a)) :
            x = randint(1,28)
            Perm_treasure.append(Permanent['5th Level'][x]) 
class Level_six () : 
    def __init__ (self) :
        a = 2
        b = 2
        for x in range(int(a)) :
            x = randint(1,18)
            Perm_treasure.append(Permanent['6th Level'][x])
        for x in range(int(b)) :
            x = randint(1,16) 
            Perm_treasure.append(Permanent['7th Level'][x])  
class Level_six_extra () : 
    def __init__ (self) :
        a = 1
        for x in range(int(a)) :
            x = randint(1,18)
            Perm_treasure.append(Permanent['6th Level'][x]) 
class Level_seven () : 
    def __init__ (self) :
        a = 2
        b = 2
        for x in range(int(a)) :
            x = randint(1,16)
            Perm_treasure.append(Permanent['7th Level'][x])
        for x in range(int(b)) :
            x = randint(1,9) 
            Perm_treasure.append(Permanent['8th Level'][x])  
class Level_seven_extra () : 
    def __init__ (self) :
        a = 1
        for x in range(int(a)) :
            x = randint(1,16)
            Perm_treasure.append(Permanent['7th Level'][x])
class Level_eight () : 
    def __init__ (self) :
        a = 2
        b = 2
        for x in range(int(a)) :
            x = randint(1,9)
            Perm_treasure.append(Permanent['8th Level'][x])
        for x in range(int(b)) :
            x = randint(1,28) 
            Perm_treasure.append(Permanent['9th Level'][x])  
class Level_eight_extra () : 
    def __init__ (self) :
        a = 1
        for x in range(int(a)) :
            x = randint(1,9)
            Perm_treasure.append(Permanent['8th Level'][x]) 
class Level_nine () : 
    def __init__ (self) :
        a = 2
        b = 2
        for x in range(int(a)) :
            x = randint(1,28)
            Perm_treasure.append(Permanent['9th Level'][x])
        for x in range(int(b)) :
            x = randint(1,18) 
            Perm_treasure.append(Permanent['10th Level'][x])  
class Level_nine_extra () : 
    def __init__ (self) :
        a = 1
        for x in range(int(a)) :
            x = randint(1,28)
            Perm_treasure.append(Permanent['9th Level'][x]) 
class Level_ten () : 
    def __init__ (self) :
        a = 2
        b = 2
        for x in range(int(a)) :
            x = randint(1,18)
            Perm_treasure.append(Permanent['10th Level'][x])
        for x in range(int(b)) :
            x = randint(1,18) 
            Perm_treasure.append(Permanent['11th Level'][x])  
class Level_ten_extra () : 
    def __init__ (self) :
        a = 1
        for x in range(int(a)) :
            x = randint(1,18)
            Perm_treasure.append(Permanent['10th Level'][x]) 
class Level_eleven () : 
    def __init__ (self) :
        a = 2
        b = 2
        for x in range(int(a)) :
            x = randint(1,18)
            Perm_treasure.append(Permanent['11th Level'][x])
        for x in range(int(b)) :
            x = randint(1,18) 
            Perm_treasure.append(Permanent['12th Level'][x])  
class Level_eleven_extra () : 
    def __init__ (self) :
        a = 1
        for x in range(int(a)) :
            x = randint(1,18)
            Perm_treasure.append(Permanent['11th Level'][x]) 
class Level_twelve () : 
    def __init__ (self) :
        a = 2
        b = 2
        for x in range(int(a)) :
            x = randint(1,18)
            Perm_treasure.append(Permanent['12th Level'][x])
        for x in range(int(b)) :
            x = randint(1,28) 
            Perm_treasure.append(Permanent['13th Level'][x])  
class Level_twelve_extra () : 
    def __init__ (self) :
        a = 1
        for x in range(int(a)) :
            x = randint(1,18)
            Perm_treasure.append(Permanent['12th Level'][x]) 
class Level_thirteen () : 
    def __init__ (self) :
        a = 2
        b = 2
        for x in range(int(a)) :
            x = randint(1,28)
            Perm_treasure.append(Permanent['13th Level'][x])
        for x in range(int(b)) :
            x = randint(1,24) 
            Perm_treasure.append(Permanent['14th Level'][x])  
class Level_thirteen_extra () : 
    def __init__ (self) :
        a = 1
        for x in range(int(a)) :
            x = randint(1,28)
            Perm_treasure.append(Permanent['13th Level'][x]) 
class Level_fourteen () : 
    def __init__ (self) :
        a = 2
        b = 2
        for x in range(int(a)) :
            x = randint(1,24)
            Perm_treasure.append(Permanent['14th Level'][x])
        for x in range(int(b)) :
            x = randint(1,9) 
            Perm_treasure.append(Permanent['15th Level'][x])  
class Level_fourteen_extra () : 
    def __init__ (self) :
        a = 1
        for x in range(int(a)) :
            x = randint(1,24)
            Perm_treasure.append(Permanent['14th Level'][x]) 
class Level_fifteen () : 
    def __init__ (self) :
        a = 2
        b = 2
        for x in range(int(a)) :
            x = randint(1,9)
            Perm_treasure.append(Permanent['15th Level'][x])
        for x in range(int(b)) :
            x = randint(1,10) 
            Perm_treasure.append(Permanent['16th Level'][x])  
class Level_fifteen_extra () : 
    def __init__ (self) :
        a = 1
        for x in range(int(a)) :
            x = randint(1,9)
            Perm_treasure.append(Permanent['15th Level'][x]) 
class Level_sixteen () : 
    def __init__ (self) :
        a = 2
        b = 2
        for x in range(int(a)) :
            x = randint(1,10)
            Perm_treasure.append(Permanent['16th Level'][x])
        for x in range(int(b)) :
            x = randint(1,10) 
            Perm_treasure.append(Permanent['17th Level'][x])  
class Level_sixteen_extra () : 
    def __init__ (self) :
        a = 1
        for x in range(int(a)) :
            x = randint(1,10)
            Perm_treasure.append(Permanent['16th Level'][x]) 
class Level_seventeen () : 
    def __init__ (self) :
        a = 2
        b = 2
        for x in range(int(a)) :
            x = randint(1,10)
            Perm_treasure.append(Permanent['17th Level'][x])
        for x in range(int(b)) :
            x = randint(1,9) 
            Perm_treasure.append(Permanent['18th Level'][x])  
class Level_seventeen_extra () : 
    def __init__ (self) :
        a = 1
        for x in range(int(a)) :
            x = randint(1,10)
            Perm_treasure.append(Permanent['17th Level'][x]) 
class Level_eighteen () : 
    def __init__ (self) :
        a = 2
        b = 2
        for x in range(int(a)) :
            x = randint(1,9)
            Perm_treasure.append(Permanent['18th Level'][x])
        for x in range(int(b)) :
            x = randint(1,10) 
            Perm_treasure.append(Permanent['19th Level'][x])  
class Level_eighteen_extra () : 
    def __init__ (self) :
        a = 1
        for x in range(int(a)) :
            x = randint(1,9)
            Perm_treasure.append(Permanent['18th Level'][x]) 
class Level_nineteen () : 
    def __init__ (self) :
        a = 2
        b = 2
        for x in range(int(a)) :
            x = randint(1,10)
            Perm_treasure.append(Permanent['19th Level'][x])
        for x in range(int(b)) :
            x = randint(1,7) 
            Perm_treasure.append(Permanent['20th Level'][x])  
class Level_nineteen_extra () : 
    def __init__ (self) :
        a = 1
        for x in range(int(a)) :
            x = randint(1,10)
            Perm_treasure.append(Permanent['19th Level'][x]) 
class Level_tewenty () : 
    def __init__ (self) :
        a = 2
        for x in range(int(a)) :
            x = randint(1,7)
            Perm_treasure.append(Permanent['20th Level'][x])
class Level_twenty_extra () : 
