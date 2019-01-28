from random import *

Valuables = { 1  : 'permanent'}

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
            '12th Level' : {},
            '13th Level' : {},
            '14th Level' : {},
            '15th Level' : {},
            '16th Level' : {},
            '17th Level' : {},
            '18th Level' : {},
            '19th Level' : {},
            '20th Level' : {}}

y = 1
for x in range(int(y)) :
    x = randint(1,7)
    print (x)
    for x in Permanent['2nd Level'][x] :
        Valuables[1] = x
        print (Valuables[1])          
