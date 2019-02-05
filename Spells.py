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
Divine = { '1st Level' : { 1 : 'Air Bubble',
                           2 : 'Alarm' ,
                           3 : 'Bane' ,
                           4 : 'Bless' ,
                           5 : 'Command' ,
                           6 : 'Create Water' ,
                           7 : 'Detect Alighnment' ,
                           8 : 'Detect Poison' ,
                           9 : 'Disrupting Weapon' ,
                           10 : 'Fear' ,
                           11 : 'Harm' ,
                           12 : 'Heal' ,
                           13 : 'Lock' ,
                           14 : 'Magic Weapon' ,
                           15 : 'Mending' ,
                           16 : 'Protection' ,
                           17 : 'Purify Food and Drink' ,
                           18 : 'Ray of Enfeeblment' ,
                           19 : 'Sanctuary' ,
                           20 : 'Summon Monster' ,
                           21 : 'Ventriloquism'} ,
            '2nd Level' : { 1 : 'Augury' ,
                            2 : 'Calm Emotions' ,
                            3 : 'Continual Flame' ,
                            4 : 'Create Food' ,
                            5 : 'Darkness' ,
                            6 : 'Deafness' ,
                            7 : 'Death Knell' ,
                            8 : 'Endure Elements' ,
                            9 : 'Faerie Fire' ,
                            10 : 'Gentle Repose' ,
                            11 : 'Ghoulish Cravings' ,
                            12 : 'Remove Fear' ,
                            13 : 'Resist Energy' ,
                            14 : 'Restoration' ,
                            15 : 'Restore Senses' ,
                            16 : 'See Invisibility' ,
                            17 : 'Shield Other' ,
                            18 : 'Silence' ,
                            19 : 'Sound Burst' ,
                            20 : 'Spiritual Weapon' ,
                            21 : 'Status' ,
                            22 : 'Undetectable Alignment' ,
                            23 : 'Water Breathing' ,
                            24 : 'Water Walk'},
            '3rd Level' : { 1 : 'Bind Undead' ,
                            2 : 'Blindness' ,
                            3 : 'Circle of Protection' ,
                            4 : 'Crisis of Faith' ,
                            5 : 'Dispel Magic' ,
                            6 : 'Dream Message' ,
                            7 : 'Heroism' ,
                            8 : 'Locate' ,
                            9 : 'Neutralize Poison' ,
                            10 : 'Remove Disease' ,
                            11 : 'Sanctified Light' ,
                            12 : 'Vampiric Touch' ,
                            13 : 'Zone of Truth' ,} ,
            '4th Level' : { 1 : 'Air Walk' ,
                            2 : 'Dimensional Anchor' ,
                            3 : 'Discern Lies' ,
                            4 : 'Divine Wrath' ,
                            5 : 'Enervation' ,
                            6 : 'Freedom of Movement' ,
                            7 : 'Globe of Invulnerability' ,
                            8 : 'Outcasts Curse' ,
                            9 : 'Read Omens' ,
                            10 : 'Remove Curse' ,
                            11 : 'Spell Immunity' ,
                            12 : 'Talking Corpse'} ,
            '5th Level' : { 1 : 'Abyssal Plague' ,
                            2 : 'Banishment' ,
                            3 : 'Breath of Life' ,
                            4 : 'Death ward' ,
                            5 : 'Flame Strike' ,
                            6 : 'Prying Eye' ,
                            7 : 'Sending' ,
                            8 : 'Shadow Blast' ,
                            9 : 'Spiritual Guardian'} ,
            '6th Level' : { 1 : 'Blade Barrier' ,
                            2 : 'Field of Life' ,
                            3 : 'Raise Dead' ,
                            4 : 'Repulsion' ,
                            5 : 'Righteous Might' ,
                            6 : 'Spellwrack' ,
                            7 : 'Spirit Blast' ,
                            8 : 'Stone tell' ,
                            9 : 'Stone to Flesh' ,
                            10 : 'True Seeing' ,
                            11 : 'Vampiric Excanguination'} ,
            '7th Level' : { 1 : 'Dimensional Lock' ,
                            2 : 'Divine Decree' ,
                            3 : 'Energy Aegis' ,
                            4 : 'Ethereal Jaunt' ,
                            5 : 'Finger of Death' ,
                            6 : 'Lengs Sting' ,
                            7 : 'Plane Shift' ,
                            8 : 'Regenerate' ,
                            9 : 'Weakening Ground'} ,
            '8th Level' : { 1 : 'Antimagic Field' ,
                            2 : 'Discern Location' ,
                            3 : 'Divine Aura' ,
                            4 : 'Divine Inspiration' ,
                            5 : 'Moment of Renewal ' ,
                            6 : 'Wind Walk'} ,
            '9th Level' : { 1 : 'Bind Soul' ,
                            2 : 'Crusade' ,
                            3 : 'Foresight' ,
                            4 : 'Overwhelming Presence' ,
                            5 : 'Revival' ,
                            6 : 'Wail of the Banshee' ,
                            7 : 'Weapon of Judgment'} ,
            '10th Level' : { 1 : 'Avatar' ,
                             2 : 'Gate' ,
                             3 : 'Miracle'}}
Occult = { '1st Level' : { 1 : 'Alarm' ,
                           2 : 'Bane' ,
                           3 : 'Bless' ,
                           4 : 'Charm' ,
                           5 : 'Color Spray' ,
                           6 : 'Command' ,
                           7 : 'Detect Alignment' ,
                           8 : 'Fear' ,
                           9 : 'FLoating Disk' ,
                           10 : 'Grim Tendrils' ,
                           11 : 'Illusory Disguise' ,
                           12 : 'Illusory object' ,
                           13 : 'Item Facade' ,
                           14 : 'Lock' ,
                           15 : 'Mage Armor' ,
                           16 : 'Magic Aura' ,
                           17 : 'Magic Missile' ,
                           18 : 'Magic Weapon' ,
                           19 : 'Mending' ,
                           20 : 'Mindlink' ,
                           21 : 'Phantom Pain' ,
                           22 : 'Protection' ,
                           23 : 'Ray of Enfeeblement' ,
                           24 : 'Sleep' ,
                           25 : 'Soothe' ,
                           26 : 'Summon Monster' ,
                           27 : 'True Strike' ,
                           28 : 'Unseen Servant' ,
                           29 : 'Ventriloquism'} ,
            '2nd Level' : { 1 : 'Augury' ,
                            2 : 'Blur' ,
                            3 : 'Calm Emotion' ,
                            4 : 'Comprehend Language' ,
                            5 : 'Continual Flame' ,
                            6 : 'Darkness' ,
                            7 : 'Darkvision' ,
                            8 : 'Deafness' ,
                            9 : 'Death Knell' ,
                            10 : 'Faerie Fire' ,
                            11 : 'False Life' ,
                            12 : 'Gentle Repose' ,
                            13 : 'Ghoulish Cravings' ,
                            14 : 'Hideous Laughter' ,
                            15 : 'Humanoid Form' ,
                            16 : 'Illusory Creature' ,
                            17 : 'Invisibility' ,
                            18 : 'Knock' ,
                            19 : 'Magic Mouth' ,
                            20 : 'Mirror Image' ,
                            21 : 'Misdirection' ,
                            22 : 'Paranoia' ,
                            23 : 'Phantom Steed' ,
                            24 : 'Remove Fear' ,
                            25 : 'Remove Paralysis' ,
                            26 : 'Resist Energy' ,
                            27 : 'Restoration' ,
                            28 : 'Restore Senses' ,
                            29 : 'See Invisibility' ,
                            30 : 'Silence' ,
                            31 : 'Sound Burst' ,
                            32 : 'Spectral Hand' ,
                            33 : 'Spiritual Weapon' ,
                            34 : 'Status' ,
                            35 : 'Telekinetic Maneuver' ,
                            36 : 'Touch of Idiocry' ,
                            37 : 'Undetectable Alignment'}, 
            '3rd Level' : { 1 : 'Bind Undead' ,
                            2 : 'Blindness' ,
                            3 : 'Circle of Protection' ,
                            4 : 'Clairaudience' ,
                            5 : 'Dispel Magic' ,
                            6 : 'Dream Message' ,
                            7 : 'Enthrall' ,
                            8 : 'Ghostly Weapon' ,
                            9 : 'Haste' ,
                            10 : 'Heorism' ,
                            11 : 'Hypercognition' ,
                            12 : 'Hypnotic Pattern' ,
                            13 : 'Invisbility Sphere' ,
                            14 : 'Levitate' ,
                            15 : 'Locate' ,
                            16 : 'Mind Reading' ,
                            17 : 'Nondetection' ,
                            18 : 'Paralyze' ,
                            19 : 'Secret Page' ,
                            20 : 'Slow' ,
                            21 : 'Vampiric Touch' ,
                            22 : 'Zone of Truth'} ,
            '4th Level' : { 1 : 'Blink' ,
                            2 : 'Clairvoyance' ,
                            3 : 'Confusion' ,
                            4 : 'Detect Scrying' ,
                            5 : 'Dimension Door' ,
                            6 : 'Dimensional Anchor' ,
                            7 : 'Discern Lies' ,
                            8 : 'Enervation' ,
                            9 : 'Fly' ,
                            10 : 'Gaseous Form' ,
                            11 : 'Globe of Invulnerability' ,
                            12 : 'Hallucinatory Terrain' ,
                            13 : 'Modify Memory' ,
                            14 : 'Nightmare' ,
                            15 : 'Outcasts Curse' ,
                            16 : 'Phantasmal Killer' ,
                            17 : 'Private Sanctum' ,
                            18 : 'Read Omens' ,
                            19 : 'Remove Curse' ,
                            20 : 'Resilient Sphere' ,
                            21 : 'Rope Trick' ,
                            22 : 'Spell Immunity' ,
                            23 : 'Suggestion' ,
                            24 : 'Talking Corpse' ,
                            25 : 'Telepathy' ,
                            26 : 'Veil'} ,
            '5th Level' : { 1 : 'Abyssal Plague' ,
                            2 : 'Banishment' ,
                            3 : 'Black Tentacles' ,
                            4 : 'Chromatic Wall' ,
                            5 : 'Cloak of Colors' ,
                            6 : 'Crushing Despair' ,
                            7 : 'Death Ward' ,
                            8 : 'Drop Dead' ,
                            9 : 'False Vision' ,
                            10 : 'Hallucination' ,
                            11 : 'Illusory Scene' ,
                            12 : 'Mariners Curse' ,
                            13 : 'Mind Probe' ,
                            14 : 'Prying Eye' ,
                            15 : 'Sending' ,
                            16 : 'Shadow Blast' ,
                            17 : 'Shadow Siphon' ,
                            18 : 'Shadow Walk' ,
                            19 : 'Synaptic Pulse' ,
                            20 : 'Synesthesia' ,
                            21 : 'Telekinetic Haul' ,
                            22 : 'Telepathic Bond' ,
                            23 : 'Tongues'} ,
            '6th Level' : { 1 : 'Collective TRansposition' ,
                            2 : 'Dominate' ,
                            3 : 'Feeblemind' ,
                            4 : 'Mislead' ,
                            5 : 'Phantasmal Calamity' ,
                            6 : 'Repulsion' ,
                            7 : 'Scrying' ,
                            8 : 'Spellwrack' ,
                            9 : 'Spirit Blast' ,
                            10 : 'Teleport' ,
                            11 : 'True Seeing' ,
                            12 : 'Vampiric Exsanguination' ,
                            13 : 'Vibrant Pattern' ,
                            14 : 'Wall of Force'} ,
            '7th Level' : { 1 : 'Dimensional Lock' ,
                            2 : 'Duplicate Foe' ,
                            3 : 'Energy Aegis' ,
                            4 : 'Ethereal Jaunt' ,
                            5 : 'Lengs Sting' ,
                            6 : 'Magnificent Mansion' ,
                            7 : 'Mask of Terror' ,
                            8 : 'Plane Shift' ,
                            9 : 'Possession' ,
                            10 : 'Prismatic Spray' ,
                            11 : 'Project Image' ,
                            12 : 'Retrocognition',
                            13 : 'Reverse GRavity' ,
                            14 : 'Visions of Danger' ,
                            15 : 'Warp Mind'} ,
            '8th Level' : { 1 : 'Antimagic' ,
                            2 : 'Disappearance' ,
                            3 : 'Discern Location' ,
                            4 : 'Dream Council' ,
                            5 : 'Maze' ,
                            6 : 'Mind Blank' ,
                            7 : 'Prismatic Wall' ,
                            8 : 'Scintillating Pattern' ,
                            9 : 'Spiritual Epidemic' ,
                            10 : 'Uncontrollable Dance' ,
                            11 : 'Unrelenting Observation'} ,
            '9th Level' : { 1 : 'Bind Soul' ,
                            2 : 'Foresight' ,
                            3 : 'Overwhelming Presence' ,
                            4 : 'Prismatic Sphere' ,
                            5 : 'Resplendant Mansion' ,
                            6 : 'Unfathomable Song' ,
                            7 : 'Wail of the Banshee' ,
                            8 : 'Weird'} ,
            '10th Level' : { 1 : 'Alter Reality' ,
                             2 : 'Fabricated Truth' ,
                             3 : 'Gate' ,
                             4 : 'Time Stop'}}
Primal = { '1st Level' : { 1 : 'Air Bubble' ,
                           2 : 'Alarm' ,
                           3 : 'Ant Haul' ,
                           4 : 'Burning Hands' ,
                           5 : 'Charm' ,
                           6 : 'Create Water' ,
                           7 : 'Detect Poison' ,
                           8 : 'Fear' ,
                           9 : 'Feather Fall' ,
                           10 : 'Fleet Step' ,
                           11 : 'Goblin Pox' ,
                           12 : 'Grease' ,
                           13 : 'Gust of Wind' ,
                           14 : 'Heal' ,
                           15 : 'Jump' ,
                           16 : 'LongStrider' ,
                           17 : 'Magic Fang' ,
                           18 : 'Mending' ,
                           19 : 'Negate Aroma', 
                           20 : 'Pass without Trace' ,
                           21 : 'Purify Food and Drink' ,
                           22 : 'Shillelagh' ,
                           23 : 'Shocking Grasp' ,
                           24 : 'Spider Grasp' ,
                           25 : 'Summon Natures ally',
                           26 : 'Ventriloquism'} ,
            '2nd Level' : { 1 : 'Acid Arrow' ,
                            2 : 'Animal Messenger' ,
                            3 : 'Barksin' ,
                            4 : 'Continual Flame' ,
                            5 : 'Create Food' ,
                            6 : 'Darkness' ,
                            7 : 'Darkvision' ,
                            8 : 'Deafness' ,
                            9 : 'Endure Elements' ,
                            10 : 'Enlarge' ,
                            11 : 'Entagle' ,
                            12 : 'Faerie Fire' ,
                            13 : 'Flaming Sphere' ,
                            14 : 'Gentle Repose' ,
                            15 : 'Glitterdust' ,
                            16 : 'Humanoid Form' ,
                            17 : 'Obscuring Mist' ,
                            18 : 'Pest Form' ,
                            19 : 'Phantom Steed' ,
                            20 : 'Remove Fear' ,
                            21 : 'Remove Paralysis' ,
                            22 : 'Resist Energy' ,
                            23 : 'Restoration' ,
                            24 : 'Restore Senses',
                            25 : 'Shape Wood' ,
                            26 : 'Shrink' ,
                            27 : 'Speak with Animals',
                            28 : 'Spider Climb' ,
                            29 : 'Status' ,
                            30 : 'Tree Shape' ,
                            31 : 'Water Breathing' ,
                            32 : 'Water Walk' ,
                            33 : 'Web'}, 
            '3rd Level' : { 1 : 'Animal Form' ,
                            2 : 'Blindness' ,
                            3 : 'Dispel Magic' ,
                            4 : 'Earthbind' ,
                            5 : 'Feet to fins' ,
                            6 : 'Fireball' ,
                            7 : 'Haste' ,
                            8 : 'Insect form' ,
                            9 : 'Meld into Stone' ,
                            10 : 'Neutralize Poison' ,
                            11 : 'Nondetection' ,
                            12 : 'Remove Disease' ,
                            13 : 'Searing Light' ,
                            14 : 'Slow' ,
                            15 : 'Stinking Cloud' ,
                            16 : 'Wall of Thorns' ,
                            17 : 'Wall of Wind'} , 
            '4th Level' : { 1 : 'Aerial Form' ,
                            2 : 'Air Walk' ,
                            3 : 'Creation' ,
                            4 : 'Dinosaur Form' ,
                            5 : 'Fire Shield' ,
                            6 : 'Fly' ,
                            7 : 'Freedom of Movement' ,
                            8 : 'Gaseous Form' ,
                            9 : 'Hallucinatory Terrain' ,
                            10 : 'Shape Stone' ,
                            11 : 'Solid Fog' ,
                            12 : 'Speak with Plants' ,
                            13 : 'Stoneskin' ,
                            14 : 'Wall of Fire' ,
                            15 : 'Weapon Storm'} ,
            '5th Level' : { 1 : 'Banishment' ,
                            2 : 'Cloudkill' ,
                            3 : 'Cone of Cold' ,
                            4 : 'Control Water' ,
                            5 : 'Death Ward' ,
                            6 : 'Elemental Form' ,
                            7 : 'Mariners Curse' ,
                            8 : 'Moon frenzy' ,
                            9 : 'Passwall' ,
                            10 : 'Plant Form' ,
                            11 : 'Tree Stride' ,
                            12 : 'Wall of Ice', 
                            13 : 'Wall of Stone'} ,
            '6th Level' : { 1 : 'Baleful Polymorph' ,
                            2 : 'Chain Lightning' ,
                            3 : 'Dragon Form', 
                            4 : 'Field of Life' ,
                            5 : 'Fire Seeds' ,
                            6 : 'Flesh to Stone' ,
                            7 : 'Purple Worm Sting' ,
                            8 : 'Stone Tell' ,
                            9 : 'Tangling Creepers' ,
                            10 : 'True Seeing'} ,
            '7th Level' : { 1 : 'Energy Aegis' ,
                            2 : 'Fiery Body' ,
                            3 : 'Finger of Death' ,
                            4 : 'Lengs Sting' ,
                            5 : 'Mask of Terror' ,
                            6 : 'Plane of Terror',
                            7 : 'Regenerate' ,
                            8 : 'Sunburst' ,
                            9 : 'Unfettered Pack' ,
                            10 : 'Volcanic Eruption'} ,
            '8th Level' : { 1 : 'Earthquake' ,
                            2 : 'Horrid Wilting' ,
                            3 : 'Moment of Renewal' ,
                            4 : 'Monstrosity Form' ,
                            5 : 'Polar Ray' ,
                            6 : 'Punishing Winds' ,
                            7 : 'Wind Walk'} ,
            '9th Level' : { 1 : 'Disjunction' ,
                            2 : 'Implosion' ,
                            3 : 'Meteor Swarm' ,
                            4 : 'Natures Enmity' ,
                            5 : 'Shapechange' ,
                            6 : 'Storm of Vengeance'} ,
            '10th Level' : { 1 : 'Nature Incarnate' ,
                             2 : 'Primal Herd' ,
                             3 : 'Primal Phenomenon'}}  
class spell_roll() :
    #Determining what Type of Magic
    def __init__ (self) :
        # Arcane = 1 , Divine = 2, Occult = 3, Primal = 4
        x = randint(1,4)
        if x == 1 : 
            if 'Wand of 1st Level spell' in Consumable_Role.Con_treasure:
                x = randint(1, len(Arcane['1st Level']))
                magic = Arcane['1st Level'][x]
                charges = randint(1,10)
                wand = ("Wand of",magic,charges,"charges left")
                Consumable_Role.Con_treasure.append(wand)
                Consumable_Role.Con_treasure.remove('Wand of 1st Level spell')
            elif 'Wand of 2nd Level spell' in Consumable_Role.Con_treasure:
                x = randint(1, len(Arcane['2nd Level']))
                magic = Arcane['2nd Level'][x]
                charges = randint(1,10)
                wand = ("Wand of",magic,charges,"charges left")
                Consumable_Role.Con_treasure.append(wand)
                Consumable_Role.Con_treasure.remove('Wand of 2nd Level spell')
            elif 'Wand of 3rd Level spell' in Consumable_Role.Con_treasure:
                x = randint(1, len(Arcane['3rd Level']))
                magic = Arcane['3rd Level'][x]
                charges = randint(1,10)
                wand = ("Wand of",magic,charges,"charges left")
                Consumable_Role.Con_treasure.append(wand)
                Consumable_Role.Con_treasure.remove('Wand of 3rd Level spell')
            elif 'Wand of 4th Level spell' in Consumable_Role.Con_treasure:
                x = randint(1, len(Arcane['4th Level']))
                magic = Arcane['4th Level'][x]
                charges = randint(1,10)
                wand = ("Wand of",magic,charges,"charges left")
                Consumable_Role.Coin.append(wand)
                Consumable_Role.Con_treasure.remove('Wand of 4th Level spell')

            if 'Scroll of 1st level spell' in Consumable_Role.Con_treasure:
                x = randint(1, len(Arcane['1st Level']))
                magic = Arcane['1st Level'][x]
                scroll = ('Scroll of',magic)
                Consumable_Role.Con_treasure.append(scroll)
                Consumable_Role.Con_treasure.remove('Scroll of 1st level spell')
            elif 'Scroll of 2nd level spell' in Consumable_Role.Con_treasure:
                x = randint(1, len(Arcane['2nd Level']))
                magic = Arcane['2nd Level'][x]
                scroll = ('Scroll of',magic)
                Consumable_Role.Con_treasure.append(scroll) 
                Consumable_Role.Con_treasure.remove('Scroll of 2nd level spell') 
            elif 'Scroll of 3rd level spell' in Consumable_Role.Con_treasure:
                x = randint(1, len(Arcane['3rd Level']))
                magic = Arcane['3rd Level'][x]
                scroll = ('Scroll of',magic)
                Consumable_Role.Con_treasure.append(scroll) 
                Consumable_Role.Con_treasure.remove('Scroll of 3rd level spell')
            elif 'Scroll of 4th level spell' in Consumable_Role.Con_treasure:
                x = randint(1, len(Arcane['4th Level']))
                magic = Arcane['4th Level'][x]
                scroll = ('Scroll of',magic)
                Consumable_Role.Con_treasure.append(scroll)
                Consumable_Role.Con_treasure.remove('Scroll of 4th level spell') 
            elif 'Scroll of 5th level spell' in Consumable_Role.Con_treasure:
                x = randint(1, len(Arcane['5th Level']))
                magic = Arcane['5th Level'][x]
                scroll = ('Scroll of',magic)
                Consumable_Role.Con_treasure.append(scroll)
                Consumable_Role.Con_treasure.remove('Scroll of 5th level spell') 
            elif 'Scroll of 6th level spell' in Consumable_Role.Con_treasure:
                x = randint(1, len(Arcane['6th Level']))
                magic = Arcane['6th Level'][x]
                scroll = ('Scroll of',magic)
                Consumable_Role.Con_treasure.append(scroll) 
                Consumable_Role.Con_treasure.remove('Scroll of 6th level spell')
            elif 'Scroll of 7th level spell' in Consumable_Role.Con_treasure:
                x = randint(1, len(Arcane['7th Level']))
                magic = Arcane['7th Level'][x]
                scroll = ('Scroll of',magic)
                Consumable_Role.Con_treasure.append(scroll)
                Consumable_Role.Con_treasure.remove('Scroll of 7th level spell') 
            elif 'Scroll of 8th level spell' in Consumable_Role.Con_treasure:
                x = randint(1, len(Arcane['8th Level']))
                magic = Arcane['8th Level'][x]
                scroll = ('Scroll of',magic)
                Consumable_Role.Con_treasure.append(scroll)
                Consumable_Role.Con_treasure.remove('Scroll of 8th level spell') 
            elif 'Scroll of 9th level spell' in Consumable_Role.Con_treasure:
                x = randint(1, len(Arcane['9th Level']))  
                magic = Arcane['9th Level'][x]
                scroll = ('Scroll of',magic)
                Consumable_Role.Con_treasure.append(scroll) 
                Consumable_Role.Con_treasure.remove('Scroll of 9th level spell')
        elif x == 2 :
            if 'Wand of 1st Level spell' in Consumable_Role.Con_treasure:
                x = randint(1, len(Divine['1st Level']))
                magic = Divine['1st Level'][x]
                charges = randint(1,10)
                wand = ("Wand of",magic,charges,"charges left")
                Consumable_Role.Con_treasure.append(wand)
                Consumable_Role.Con_treasure.remove('Wand of 1st Level spell')
            elif 'Wand of 2nd Level spell' in Consumable_Role.Con_treasure:
                x = randint(1, len(Divine['2nd Level']))
                magic = Divine['2nd Level'][x]
                charges = randint(1,10)
                wand = ("Wand of",magic,charges,"charges left")
                Consumable_Role.Con_treasure.append(wand)
                Consumable_Role.Con_treasure.remove('Wand of 2nd Level spell')
            elif 'Wand of 3rd Level spell' in Consumable_Role.Con_treasure:
                x = randint(1, len(Divine['3rd Level']))
                magic = Divine['3rd Level'][x]
                charges = randint(1,10)
                wand = ("Wand of",magic,charges,"charges left")
                Consumable_Role.Con_treasure.append(wand)
                Consumable_Role.Con_treasure.remove('Wand of 3rd Level spell')
            elif 'Wand of 4th Level spell' in Consumable_Role.Con_treasure:
                x = randint(1, len(Divine['4th Level']))
                magic = Divine['4th Level'][x]
                charges = randint(1,10)
                wand = ("Wand of",magic,charges,"charges left")
                Consumable_Role.Coin.append(wand)
                Consumable_Role.Con_treasure.remove('Wand of 4th Level spell')

            if 'Scroll of 1st level spell' in Consumable_Role.Con_treasure:
                x = randint(1, len(Divine['1st Level']))
                magic = Divine['1st Level'][x]
                scroll = ('Scroll of',magic)
                Consumable_Role.Con_treasure.append(scroll)
                Consumable_Role.Con_treasure.remove('Scroll of 1st level spell')
            elif 'Scroll of 2nd level spell' in Consumable_Role.Con_treasure:
                x = randint(1, len(Divine['2nd Level']))
                magic = Divine['2nd Level'][x]
                scroll = ('Scroll of',magic)
                Consumable_Role.Con_treasure.append(scroll) 
                Consumable_Role.Con_treasure.remove('Scroll of 2nd level spell') 
            elif 'Scroll of 3rd level spell' in Consumable_Role.Con_treasure:
                x = randint(1, len(Divine['3rd Level']))
                magic = Divine['3rd Level'][x]
                scroll = ('Scroll of',magic)
                Consumable_Role.Con_treasure.append(scroll) 
                Consumable_Role.Con_treasure.remove('Scroll of 3rd level spell')
            elif 'Scroll of 4th level spell' in Consumable_Role.Con_treasure:
                x = randint(1, len(Divine['4th Level']))
                magic = Divine['4th Level'][x]
                scroll = ('Scroll of',magic)
                Consumable_Role.Con_treasure.append(scroll)
                Consumable_Role.Con_treasure.remove('Scroll of 4th level spell') 
            elif 'Scroll of 5th level spell' in Consumable_Role.Con_treasure:
                x = randint(1, len(Divine['5th Level']))
                magic = Divine['5th Level'][x]
                scroll = ('Scroll of',magic)
                Consumable_Role.Con_treasure.append(scroll)
                Consumable_Role.Con_treasure.remove('Scroll of 5th level spell') 
            elif 'Scroll of 6th level spell' in Consumable_Role.Con_treasure:
                x = randint(1, len(Divine['6th Level']))
                magic = Divine['6th Level'][x]
                scroll = ('Scroll of',magic)
                Consumable_Role.Con_treasure.append(scroll) 
                Consumable_Role.Con_treasure.remove('Scroll of 6th level spell')
            elif 'Scroll of 7th level spell' in Consumable_Role.Con_treasure:
                x = randint(1, len(Divine['7th Level']))
                magic = Divine['7th Level'][x]
                scroll = ('Scroll of',magic)
                Consumable_Role.Con_treasure.append(scroll)
                Consumable_Role.Con_treasure.remove('Scroll of 7th level spell') 
            elif 'Scroll of 8th level spell' in Consumable_Role.Con_treasure:
                x = randint(1, len(Divine['8th Level']))
                magic = Divine['8th Level'][x]
                scroll = ('Scroll of',magic)
                Consumable_Role.Con_treasure.append(scroll)
                Consumable_Role.Con_treasure.remove('Scroll of 8th level spell') 
            elif 'Scroll of 9th level spell' in Consumable_Role.Con_treasure:
                x = randint(1, len(Divine['9th Level']))  
                magic = Divine['9th Level'][x]
                scroll = ('Scroll of',magic)
                Consumable_Role.Con_treasure.append(scroll) 
                Consumable_Role.Con_treasure.remove('Scroll of 9th level spell')
        elif x == 3 :
            if 'Wand of 1st Level spell' in Consumable_Role.Con_treasure:
                x = randint(1, len(Occult['1st Level']))
                magic = Occult['1st Level'][x]
                charges = randint(1,10)
                wand = ("Wand of",magic,charges,"charges left")
                Consumable_Role.Con_treasure.append(wand)
                Consumable_Role.Con_treasure.remove('Wand of 1st Level spell')
            elif 'Wand of 2nd Level spell' in Consumable_Role.Con_treasure:
                x = randint(1, len(Occult['2nd Level']))
                magic = Occult['2nd Level'][x]
                charges = randint(1,10)
                wand = ("Wand of",magic,charges,"charges left")
                Consumable_Role.Con_treasure.append(wand)
                Consumable_Role.Con_treasure.remove('Wand of 2nd Level spell')
            elif 'Wand of 3rd Level spell' in Consumable_Role.Con_treasure:
                x = randint(1, len(Occult['3rd Level']))
                magic = Occult['3rd Level'][x]
                charges = randint(1,10)
                wand = ("Wand of",magic,charges,"charges left")
                Consumable_Role.Con_treasure.append(wand)
                Consumable_Role.Con_treasure.remove('Wand of 3rd Level spell')
            elif 'Wand of 4th Level spell' in Consumable_Role.Con_treasure:
                x = randint(1, len(Occult['4th Level']))
                magic = Occult['4th Level'][x]
                charges = randint(1,10)
                wand = ("Wand of",magic,charges,"charges left")
                Consumable_Role.Coin.append(wand)
                Consumable_Role.Con_treasure.remove('Wand of 4th Level spell')

            if 'Scroll of 1st level spell' in Consumable_Role.Con_treasure:
                x = randint(1, len(Occult['1st Level']))
                magic = Occult['1st Level'][x]
                scroll = ('Scroll of',magic)
                Consumable_Role.Con_treasure.append(scroll)
                Consumable_Role.Con_treasure.remove('Scroll of 1st level spell')
            elif 'Scroll of 2nd level spell' in Consumable_Role.Con_treasure:
                x = randint(1, len(Occult['2nd Level']))
                magic = Occult['2nd Level'][x]
                scroll = ('Scroll of',magic)
                Consumable_Role.Con_treasure.append(scroll) 
                Consumable_Role.Con_treasure.remove('Scroll of 2nd level spell') 
            elif 'Scroll of 3rd level spell' in Consumable_Role.Con_treasure:
                x = randint(1, len(Occult['3rd Level']))
                magic = Occult['3rd Level'][x]
                scroll = ('Scroll of',magic)
                Consumable_Role.Con_treasure.append(scroll) 
                Consumable_Role.Con_treasure.remove('Scroll of 3rd level spell')
            elif 'Scroll of 4th level spell' in Consumable_Role.Con_treasure:
                x = randint(1, len(Occult['4th Level']))
                magic = Occult['4th Level'][x]
                scroll = ('Scroll of',magic)
                Consumable_Role.Con_treasure.append(scroll)
                Consumable_Role.Con_treasure.remove('Scroll of 4th level spell') 
            elif 'Scroll of 5th level spell' in Consumable_Role.Con_treasure:
                x = randint(1, len(Occult['5th Level']))
                magic = Occult['5th Level'][x]
                scroll = ('Scroll of',magic)
                Consumable_Role.Con_treasure.append(scroll)
                Consumable_Role.Con_treasure.remove('Scroll of 5th level spell') 
            elif 'Scroll of 6th level spell' in Consumable_Role.Con_treasure:
                x = randint(1, len(Occult['6th Level']))
                magic = Occult['6th Level'][x]
                scroll = ('Scroll of',magic)
                Consumable_Role.Con_treasure.append(scroll) 
                Consumable_Role.Con_treasure.remove('Scroll of 6th level spell')
            elif 'Scroll of 7th level spell' in Consumable_Role.Con_treasure:
                x = randint(1, len(Occult['7th Level']))
                magic = Occult['7th Level'][x]
                scroll = ('Scroll of',magic)
                Consumable_Role.Con_treasure.append(scroll)
                Consumable_Role.Con_treasure.remove('Scroll of 7th level spell') 
            elif 'Scroll of 8th level spell' in Consumable_Role.Con_treasure:
                x = randint(1, len(Occult['8th Level']))
                magic = Occult['8th Level'][x]
                scroll = ('Scroll of',magic)
                Consumable_Role.Con_treasure.append(scroll)
                Consumable_Role.Con_treasure.remove('Scroll of 8th level spell') 
            elif 'Scroll of 9th level spell' in Consumable_Role.Con_treasure:
                x = randint(1, len(Occult['9th Level']))  
                magic = Occult['9th Level'][x]
                scroll = ('Scroll of',magic)
                Consumable_Role.Con_treasure.append(scroll) 
                Consumable_Role.Con_treasure.remove('Scroll of 9th level spell')
        elif x == 4 :
            if 'Wand of 1st Level spell' in Consumable_Role.Con_treasure:
                x = randint(1, len(Primal['1st Level']))
                magic = Primal['1st Level'][x]
                charges = randint(1,10)
                wand = ("Wand of",magic,charges,"charges left")
                Consumable_Role.Con_treasure.append(wand)
                Consumable_Role.Con_treasure.remove('Wand of 1st Level spell')
            elif 'Wand of 2nd Level spell' in Consumable_Role.Con_treasure:
                x = randint(1, len(Primal['2nd Level']))
                magic = Primal['2nd Level'][x]
                charges = randint(1,10)
                wand = ("Wand of",magic,charges,"charges left")
                Consumable_Role.Con_treasure.append(wand)
                Consumable_Role.Con_treasure.remove('Wand of 2nd Level spell')
            elif 'Wand of 3rd Level spell' in Consumable_Role.Con_treasure:
                x = randint(1, len(Primal['3rd Level']))
                magic = Primal['3rd Level'][x]
                charges = randint(1,10)
                wand = ("Wand of",magic,charges,"charges left")
                Consumable_Role.Con_treasure.append(wand)
                Consumable_Role.Con_treasure.remove('Wand of 3rd Level spell')
            elif 'Wand of 4th Level spell' in Consumable_Role.Con_treasure:
                x = randint(1, len(Primal['4th Level']))
                magic = Primal['4th Level'][x]
                charges = randint(1,10)
                wand = ("Wand of",magic,charges,"charges left")
                Consumable_Role.Coin.append(wand)
                Consumable_Role.Con_treasure.remove('Wand of 4th Level spell')

            if 'Scroll of 1st level spell' in Consumable_Role.Con_treasure:
                x = randint(1, len(Primal['1st Level']))
                magic = Primal['1st Level'][x]
                scroll = ('Scroll of',magic)
                Consumable_Role.Con_treasure.append(scroll)
                Consumable_Role.Con_treasure.remove('Scroll of 1st level spell')
            elif 'Scroll of 2nd level spell' in Consumable_Role.Con_treasure:
                x = randint(1, len(Primal['2nd Level']))
                magic = Primal['2nd Level'][x]
                scroll = ('Scroll of',magic)
                Consumable_Role.Con_treasure.append(scroll) 
                Consumable_Role.Con_treasure.remove('Scroll of 2nd level spell') 
            elif 'Scroll of 3rd level spell' in Consumable_Role.Con_treasure:
                x = randint(1, len(Primal['3rd Level']))
                magic = Primal['3rd Level'][x]
                scroll = ('Scroll of',magic)
                Consumable_Role.Con_treasure.append(scroll) 
                Consumable_Role.Con_treasure.remove('Scroll of 3rd level spell')
            elif 'Scroll of 4th level spell' in Consumable_Role.Con_treasure:
                x = randint(1, len(Primal['4th Level']))
                magic = Primal['4th Level'][x]
                scroll = ('Scroll of',magic)
                Consumable_Role.Con_treasure.append(scroll)
                Consumable_Role.Con_treasure.remove('Scroll of 4th level spell') 
            elif 'Scroll of 5th level spell' in Consumable_Role.Con_treasure:
                x = randint(1, len(Primal['5th Level']))
                magic = Primal['5th Level'][x]
                scroll = ('Scroll of',magic)
                Consumable_Role.Con_treasure.append(scroll)
                Consumable_Role.Con_treasure.remove('Scroll of 5th level spell') 
            elif 'Scroll of 6th level spell' in Consumable_Role.Con_treasure:
                x = randint(1, len(Primal['6th Level']))
                magic = Primal['6th Level'][x]
                scroll = ('Scroll of',magic)
                Consumable_Role.Con_treasure.append(scroll) 
                Consumable_Role.Con_treasure.remove('Scroll of 6th level spell')
            elif 'Scroll of 7th level spell' in Consumable_Role.Con_treasure:
                x = randint(1, len(Primal['7th Level']))
                magic = Primal['7th Level'][x]
                scroll = ('Scroll of',magic)
                Consumable_Role.Con_treasure.append(scroll)
                Consumable_Role.Con_treasure.remove('Scroll of 7th level spell') 
            elif 'Scroll of 8th level spell' in Consumable_Role.Con_treasure:
                x = randint(1, len(Primal['8th Level']))
                magic = Primal['8th Level'][x]
                scroll = ('Scroll of',magic)
                Consumable_Role.Con_treasure.append(scroll)
                Consumable_Role.Con_treasure.remove('Scroll of 8th level spell') 
            elif 'Scroll of 9th level spell' in Consumable_Role.Con_treasure:
                x = randint(1, len(Primal['9th Level']))  
                magic = Primal['9th Level'][x]
                scroll = ('Scroll of',magic)
                Consumable_Role.Con_treasure.append(scroll) 
                Consumable_Role.Con_treasure.remove('Scroll of 9th level spell')
