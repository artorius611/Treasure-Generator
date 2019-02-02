import Consumable_Role
from random import *

Arcane = { '1st Level' : { 1 : 'Air Bubble' ,
                           2 : 'Alarm' ,
                           3 : 'Ant Haul' ,
                           4 : 'Burning Hands' ,
                           5 : 'Charm' ,
                           6 : 'Color Spray' ,
                           7 : 'Command' ,
                           8 : 'Create Water' ,
                           9 : 'Fear' ,
                           10 : 'Feather Fall' ,
                           11 : 'Fleet Step' ,
                           12 : 'Floating Disk' ,
                           13 : 'Goblin Pox' ,
                           14 : 'Grease' ,
                           15 : 'Grim Tendrils' ,
                           16 : 'Gust of Wind' ,
                           17 : 'Illusory Disguise' ,
                           18 : 'Illusory Object' ,
                           19 : 'Item Facade' ,
                           20 : 'Jump' ,
                           21 : 'Lock' ,
                           22 : 'Longstrider' ,
                           23 : 'Mage Armor' ,
                           24 : 'Magic Aura' ,
                           25 : 'Magic Missile' ,
                           26 : 'Magic Weapon' ,
                           27 : 'Mending' ,
                           28 : 'Negate Aroma' ,
                           29 : 'Ray of Enfeeblment' ,
                           30 : 'Shocking Grasp' ,
                           31 : 'Sleep' ,
                           32 : 'Spider Sting' ,
                           33 : 'Summon Monster' ,
                           34 : 'True Strike' ,
                           35 : 'Unseen Servant' ,
                           36 : 'Ventriloquism' } , 
            '2nd Level' : { 1 : 'Acid Arrow' ,
                            2 : 'Blur' ,
                            3 : 'Comprehend Language' ,
                            4 : 'Continual Flame' ,
                            5 : 'Create Food' ,
                            6 : 'Darkness' ,
                            7 : 'Darkvision' ,
                            8 : 'Deafness' ,
                            9 : 'Endure Elements' ,
                            10 : 'Enlarge' ,
                            11 : 'False Life' ,
                            12 : 'Flaming Sphere' ,
                            13 : 'Gentle Repose' ,
                            14 : 'Glitterdust' ,
                            15 : 'Hideous Laughter' ,
                            16 : 'Humanoid Form' ,
                            17 : 'Illusory Creature' ,
                            18 : 'Invisibility' ,
                            19 : 'Knock' ,
                            20 : 'Magic Mouth' ,
                            21 : 'Mirror Image' ,
                            22 : 'Misdirection' ,
                            23 : 'Obscuring Mist' ,
                            24 : 'Pest form' ,
                            25 : 'Phantom Steed' ,
                            26 : 'Resist Energy' ,
                            27 : 'See Invisibility' ,
                            28 : 'Shrink' ,
                            29 : 'Spectral Hand' ,
                            30 : 'Telekinetic Maneuver' ,
                            31 : 'Touch of Idiocy' ,
                            32 : 'Water Breathing' ,
                            33 : 'Water Walk' ,
                            34 : 'Web'} ,
            '3rd Level' : { 1 : 'Bind Undead' ,
                            2 : 'Blindness' ,
                            3 : 'Clairaudience' ,
                            4 : 'Dispel Magic' ,
                            5 : 'Dream Message' ,
                            6 : 'Earthbind' ,
                            7 : 'Enthrall' ,
                            8 : 'Feet to Fins' ,
                            9 : 'Fireball' ,
                            10 : 'Ghostly Weapon' ,
                            11 : 'Haste' ,
                            12 : 'Hypontic Pattern' ,
                            13 : 'Invisibility Sphere' ,
                            14 : 'Levitate' ,
                            15 : 'Lightning Bolt' ,
                            16 : 'Locate' ,
                            17 : 'Meld into Stone' ,
                            18 : 'Mind Reading' ,
                            19 : 'Nondetection' ,
                            20 : 'Paralyze' ,
                            21 : 'Secret Page' ,
                            22 : 'Shrink Item' ,
                            23 : 'Slow' ,
                            24 : 'Stinking Cloud' ,
                            25 : 'Vampiric Touch' ,
                            26 : 'Wall of Wind'} ,
            '4th Level' : { 1 : 'Aerial Form' ,
                            2 : 'Blink' ,
                            3 : 'Clairvoyance' ,
                            4 : 'Confusion' ,
                            5 : 'Creation' ,
                            6 : 'Detect Scrying' ,
                            7 : 'Dimension Door' ,
                            8 : 'Dimensional Anchor' ,
                            9 : 'Discern Lies' ,
                            10 : 'Enervation' ,
                            11 : 'Fire Shield' ,
                            12 : 'Fly' ,
                            13 : 'Freedom of Movement' ,
                            14 : 'Gaseous Form' ,
                            15 : 'Globe of Invulnerability' ,
                            16 : 'Hallucinatory Terrain' ,
                            17 : 'Nightmare' ,
                            18 : 'Outcast Curse' ,
                            19 :'Phantasmal Killer' ,
                            20 : 'Private Sanctum' ,
                            21 : 'Resilient Sphere' ,
                            22 : 'Rope Trick' ,
                            23 : 'Shape Stone' ,
                            24 : 'Solid Fog' ,
                            25 : 'Spell Immunity' ,
                            26 : 'Stonekin' ,
                            27 : 'Suggestion' ,
                            28 : 'Telepathy' ,
                            29 : 'Veil' ,
                            30 : 'Wall of Fire' ,
                            31 : 'Weapon Storm'} ,
            '5th Level' : { 1 : 'Banishment' ,
                            2 : 'Black Tentacles' ,
                            3 : 'Chromatic Wall ',
                            4 : 'Cloak of Colors' ,
                            5 : 'Cloudkill' ,
                            6 : 'Cone of Cold' ,
                            7 : 'Control Water' ,
                            8 : 'Crushing Despair',
                            9 : 'Drop Dead' ,
                            10 : 'Elemental Form' ,
                            11 : 'False Vision' ,
                            12 : 'Hallucination' ,
                            13 : 'Illusory Scene' ,
                            14 : 'Mariners Curse' ,
                            15 : 'Mind Probe' ,
                            16 : 'Passwall' ,
                            17 : 'Prying Eye' ,
                            18 : 'Sending' ,
                            19 : 'Shadow Siphon' ,
                            20 : 'Shadow Walk' ,
                            21 : 'Telekinetic Haul' ,
                            22 : 'Telepathic Bond' ,
                            23 : 'Tongues' ,
                            24 : 'Wall of Ice' ,
                            25 : 'Wall of Stone'} ,
            '6th Level' : { 1 : 'Baleful Polymorph' ,
                            2 : 'Chain Lightning' ,
                            3 : 'Collective Transposition' ,
                            4 : 'Disintergate' ,
                            5 : 'Dominate' ,
                            6 : 'Dragon Form' ,
                            7 : 'Feeblemind' ,
                            8 : 'Flesh to Stone' ,
                            9 : 'Mislead' ,
                            10 : 'Phantasmal Calamity' ,
                            11 : 'Purple Worm Sting' ,
                            12 : 'Repulsion' ,
                            13 : 'Scrying' ,
                            14 : 'Spellwrack' ,
                            15 : 'Teleport' ,
                            16 : 'True Seeing' ,
                            17 : 'Vampiric Exsanguination' ,
                            18 : 'Vibrant Pattern' ,
                            19 : 'Wall of Force'} ,
            '7th Level' : { 1 : 'Contingency' ,
                            2 : 'Dimensional Lock' ,
                            3 : 'Duplicate Foe' ,
                            4 : 'Energy Aegis' ,
                            5 : 'Fiery Body' ,
                            6 : 'Lengs Sting' ,
                            7 : 'Magnificent Mansion' ,
                            8 : 'Mask of Terror' ,
                            9 : 'Plane Shift' ,
                            10 : 'Power Word Blind' ,
                            11 : 'Prismatic Spray' ,
                            12 : 'Project Image' ,
                            13 : 'Reverse Gravity' ,
                            14 : 'Spell Tuning' ,
                            15 : 'Warp Mind'} ,
            '8th Level' : { 1 : 'Antimagic Field' ,
                            2 : 'Disappearance' ,
                            3 : 'Discern Location' ,
                            4 : 'Dream Council' ,
                            5 : 'Earthquake' ,
                            6 : 'Horrid Wilting' ,
                            7 : 'Maze' ,
                            8 : 'Mind Blank' ,
                            9 : 'Monstrosity Form' ,
                            10 : 'Polar Ray' ,
                            11 : 'Power Word Stun' ,
                            12 : 'Prismatic Wall' ,
                            13 : 'Scintillating Pattern' ,
                            14 : 'Uncontrollable Dance' ,
                            15 : 'Unrelenting Observation'} ,
            '9th Level' : { 1 : 'Disjunction' ,
                            2 : 'Foresight' ,
                            3 : 'Implosion' ,
                            4 : 'Meteor Swarm' ,
                            5 : 'Power word Kill' ,
                            6 : 'Prismatic Sphere' ,
                            7 : 'Resplendent Mansion' ,
                            8 : 'Shapechange' ,
                            9 : 'Weird'} ,
            '10th Level' : { 1 : 'Gate' ,
                             2 : 'Time Stop' ,
                             3 : 'Wish'}}
class spell_roll() :
    #Determining what Type of Magic
    def __init__ (self) :
        # Arcane = 1 , Divine = 2, Occult = 3, Primal = 4
        a = 1
        for x in range(int(a)) :
            x = randint(1,4)
            if x == 1 : 
                if 'Wand of 1st Level spell' in Consumable_Role.Con_treasure:
                    a = 1      
                    for x in range(int(a)) :
                        x = randint(1,36)
                        b = 1  
                        magic = Arcane['1st Level'][x]
                        for x in range(int(b)) :
                            x = randint(1,10)
                            charges = x 
                            wand = ("Wand of",magic,charges,"charges left")
                            Consumable_Role.Con_treasure.append(wand)
                            Consumable_Role.Con_treasure.remove('Wand of 1st Level spell')
                elif 'Wand of 2nd Level spell' in Consumable_Role.Con_treasure:
                    a = 1     
                    for x in range(int(a)) :
                        x = randint(1,34)
                        b = 1  
                        magic = Arcane['2nd Level'][x]
                        for x in range(int(b)) :
                            x = randint(1,10)
                            charges = x 
                            wand = ("Wand of",magic,charges,"charges left")
                            Consumable_Role.Con_treasure.append(wand)
                            Consumable_Role.Con_treasure.remove('Wand of 2nd Level spell')
                elif 'Wand of 3rd Level spell' in Consumable_Role.Con_treasure:
                    a = 1     
                    for x in range(int(a)) :
                        x = randint(1,26)
                        b = 1  
                        magic = Arcane['3rd Level'][x]
                        for x in range(int(b)) :
                            x = randint(1,10)
                            charges = x 
                            wand = ("Wand of",magic,charges,"charges left")
                            Consumable_Role.Con_treasure.append(wand)
                            Consumable_Role.Con_treasure.remove('Wand of 3rd Level spell')
                elif 'Wand of 4th Level spell' in Consumable_Role.Con_treasure:
                    a = 1  
                    for x in range(int(a)) :
                        x = randint(1,31)
                        b = 1  
                        magic = Arcane['4th Level'][x]
                        for x in range(int(b)) :
                            x = randint(1,10)
                            charges = x 
                            wand = ("Wand of",magic,charges,"charges left")
                            Consumable_Role.Coin.append(wand)
                            Consumable_Role.Con_treasure.remove('Wand of 4th Level spell')

                if 'Scroll of 1st level spell' in Consumable_Role.Con_treasure:
                    a = 1  
                    for x in range(int(a)) :
                        x = randint(1,36)
                        b = 1  
                        magic = Arcane['1st Level'][x]
                        for x in range(int(b)) :
                            x = randint(1,10)
                            charges = x 
                            scroll = ('Scroll of',magic)
                            Consumable_Role.Con_treasure.append(scroll)
                            Consumable_Role.Con_treasure.remove('Scroll of 1st level spell')
                elif 'Scroll of 2nd level spell' in Consumable_Role.Con_treasure:
                    a = 1  
                    for x in range(int(a)) :
                        x = randint(1,34)
                        b = 1  
                        magic = Arcane['2nd Level'][x]
                        for x in range(int(b)) :
                            x = randint(1,10)
                            charges = x 
                            scroll = ('Scroll of',magic)
                            Consumable_Role.Con_treasure.append(scroll) 
                            Consumable_Role.Con_treasure.remove('Scroll of 2nd level spell') 
                elif 'Scroll of 3rd level spell' in Consumable_Role.Con_treasure:
                    a = 1  
                    for x in range(int(a)) :
                        x = randint(1,26)
                        b = 1  
                        magic = Arcane['3rd Level'][x]
                        for x in range(int(b)) :
                            x = randint(1,10)
                            charges = x 
                            scroll = ('Scroll of',magic)
                            Consumable_Role.Con_treasure.append(scroll) 
                            Consumable_Role.Con_treasure.remove('Scroll of 3rd level spell')
                elif 'Scroll of 4th level spell' in Consumable_Role.Con_treasure:
                    a = 1  
                    for x in range(int(a)) :
                        x = randint(1,31)
                        b = 1  
                        magic = Arcane['4th Level'][x]
                        for x in range(int(b)) :
                            x = randint(1,10)
                            charges = x 
                            scroll = ('Scroll of',magic)
                            Consumable_Role.Con_treasure.append(scroll)
                            Consumable_Role.Con_treasure.remove('Scroll of 4th level spell') 
                elif 'Scroll of 5th level spell' in Consumable_Role.Con_treasure:
                    a = 1  
                    for x in range(int(a)) :
                        x = randint(1,25)
                        b = 1  
                        magic = Arcane['5th Level'][x]
                        for x in range(int(b)) :
                            x = randint(1,10)
                            charges = x 
                            scroll = ('Scroll of',magic)
                            Consumable_Role.Con_treasure.append(scroll)
                            Consumable_Role.Con_treasure.remove('Scroll of 5th level spell') 
                elif 'Scroll of 6th level spell' in Consumable_Role.Con_treasure:
                    a = 1  
                    for x in range(int(a)) :
                        x = randint(1,19)
                        b = 1  
                        magic = Arcane['6th Level'][x]
                        for x in range(int(b)) :
                            x = randint(1,10)
                            charges = x 
                            scroll = ('Scroll of',magic)
                            Consumable_Role.Con_treasure.append(scroll) 
                            Consumable_Role.Con_treasure.remove('Scroll of 6th level spell')
                elif 'Scroll of 7th level spell' in Consumable_Role.Con_treasure:
                    a = 1  
                    for x in range(int(a)) :
                        x = randint(1,15)
                        b = 1  
                        magic = Arcane['7th Level'][x]
                        for x in range(int(b)) :
                            x = randint(1,10)
                            charges = x 
                            scroll = ('Scroll of',magic)
                            Consumable_Role.Con_treasure.append(scroll)
                            Consumable_Role.Con_treasure.remove('Scroll of 7th level spell') 
                elif 'Scroll of 8th level spell' in Consumable_Role.Con_treasure:
                    a = 1  
                    for x in range(int(a)) :
                        x = randint(1,15)
                        b = 1  
                        magic = Arcane['8th Level'][x]
                        for x in range(int(b)) :
                            x = randint(1,10)
                            charges = x 
                            scroll = ('Scroll of',magic)
                            Consumable_Role.Con_treasure.append(scroll)
                            Consumable_Role.Con_treasure.remove('Scroll of 8th level spell') 
                elif 'Scroll of 9th level spell' in Consumable_Role.Con_treasure:
                    a = 1  
                    for x in range(int(a)) :
                        x = randint(1,9)
                        b = 1  
                        magic = Arcane['9th Level'][x]
                        for x in range(int(b)) :
                            x = randint(1,10)
                            charges = x 
                            scroll = ('Scroll of',magic)
                            Consumable_Role.Con_treasure.append(scroll) 
                            Consumable_Role.Con_treasure.remove('Scroll of 9th level spell')
