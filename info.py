class equipment () :
    gear = { 'melee' : { 'simple' : ['club' ,'dagger' ,'gauntlet' ,'light maec' ,'mace' ,'morningstar','sickle' ,'spear' ,'spiked gauntlet' ,'staff'], 
                         'uncommon simple' : ['clan dagger' ,'katar'],
                         'martial' : ['bastard sword' ,'battle axe' ,'bo staff' ,'falchion' ,'flail' ,'glaive' ,'greataxe' ,'greatclub' ,'greatpick' ,'greatsword','guisame' ,'halberd' ,'hatchet' ,'lance' ,'light hammer' ,'light pick' ,'longsword' ,'main-gauche' ,'maul' ,'pick' ,'ranseur' ,'rapier' ,'sap' ,'scimitar' ,'scythe' ,'shortsword' ,'starknife' ,'trident' ,'war flail' ,'warhammer' ,'whip'] ,
                         'uncommon martial' : ['dogslicer' ,'elven curved blade' , "filcher's fork" ,'gnome hooked hammer' ,'horsechopper' ,'kama' ,'katana' ,'kukri' ,'nunchaku' ,'orc knuckle dagger' ,'sai' ,'spiked chain' ,'temple sword'] ,
                         'uncommon advanced' : ['dwarven waraxe' ,'gnome flickmace' ,'orc necksplitter' ,'sawtooth saber']
                        } ,
             'ranged' : { 'simple' : ['blowgun' ,'crosbow' ,'dart' ,'hand crosbow' ,'heavy crossbow' ,'javelin' ,'sling'],
                          'martial' : ['composite longbow' ,'composite shortbow' ,'longbow' ,'shortbow'],
                          'uncommon martial' : ['halfling sling staff' ,'shuriken']
                        }
            }

class Con_treasure () :
    con_loot = { 1 : { 'ammunition' : ['Shining blowgun dart','Shining bolt' ,'Shining Dart', 'Shining javelin' ,'Shining sling bullet' ,'Shining arrow' ,'Shining Shuriken'] ,
                      'bomb' : ["Lesser Acid Flask" ,"Lesser Alchemist's Fire" ,"Lesser Bottled Lightning" ,"Lesser Tanglefoot Bag" ,"Lesser Thunderstone" ,] ,
                      'elixir' : ["Lesser Antidote" ,"Lesser Bestial Mutagen" ,"Lesser Cognitive Mutagen" ,"Lesser Eagle-eye Elixir" ,"Lesser Elixir of Life" ,"Lesser Juggernaut Mutagen" ,"Lesser Leaper's Elixir" ,"Lesser Quicksilver Mutagen" ,"Lesser Serene Mutagen" ,"Lesser Silvertongue Mutagen" ] ,
                      'consumable' : ["Feather Token - Ladder" ,"Holy Water" ,"Runestone" , "Unholy Water" , ] ,
                      'oil' : "Nectar of Purification" ,
                      'poison' : ["Arsenic" ,"Giant Centipede Venom"] ,
                      'potion' : "Minor Healing Potion" ,
                      'scroll' : "Scroll of 1st-Level Spell" ,
                      'snare' : ["Alarm Snare" ,"Caltrop Snare" ,"Hampering Snare" ,"Marking Snare" ,"Signaling Snare" ,"Spike Snare" ] ,
                      'talisman' : ["Owlbear Claw " ,"Potency Crystal" , "Wolf Fang"] ,
                      'tool' : ["Lessser Smokestick" ,"Snake Oil" ,"Sunrod " ,"Tinderwig" ]
                    } ,
               2 : {  'consumable' : 'Feather Token - Holly bush' ,
                       'elixir' : ["Lesser Bravo's Brew" ,"Cat's Eye Elixir" ,"Lesser Comprehension Elixir" ,"Lesser Darkvision Elixir" ,"Infiltrator's Elixir"] ,
                       'oil' : ["Oil of Potency" ,"Oil of Weightlessness"] ,
                       'poison' : ["Belladona"  ,"Black adder venom" ,"Lethargy Venom"],
                       'talisman' : ["Bronze Bull Pendant" ,"Crying Angel Pendant" ,"Effervescent ampoule" ,"Hunter's Bane" ,"Jadecat" ,"Mesmerizing Opal" ,"Monkey Pin" ,"Onyx Panther" ,"Savior Spike"] ,
                       'tool' : "Silversheen"  }
                  }
class Perm_treasure () :
    perm_loot = {} 

class Gold () :
    g_level = { 1 : 40 ,
                2 : 70 ,
                3 : 120 ,
                4 : 200 ,
                5 : 320 ,
                6 : 500 ,
                7 : 720 ,
                8 : 1000 ,
                9 : 1400 ,
                10 : 2000,
                11 : 2800,
                12 : 4000,
                13 : 6000,
                14 : 9000 ,
                15 : 13000,
                16 : 20000,
                17 : 30000,
                18 : 48000,
                19 : 80000,
                20 : 14000}
class Spells () :
    spells = { 'arcane' : { 0 : ['Acid Splash','Chill Touch','Dancing Lights','Daze','Detect Magic','Electric Arc','Ghost Sound','Light','Mage Hand','Message','Prestidigitation','Produce Flame','Ray of Frost','Read Aura','Shield','Sigil','Tanglefoot','Telekenetic Projectile'],
                           1 : ['Air Bubble','Alarm','Ant Ahul','Burning Hands','Charm','Color Spray','Comman','Create Water','Fear','Feather Fall','Fleet Step','Floating Disk','Goblin Pox','Grease','Grim Tendrils','Gust of Wind','Hydraulic Push','Illusory Disguise','Item Facade','Jump','Lock','Longstrider','Mage Armor','Magic Missile','Magic Weapon','Mending','Negate Aroma','Pest Form','Ray of Enfeeblement','Shocking Grasp','Sleep','Spider Sting','Summon Animal','Summon Construct','True Strike','Unseen Servant','Ventriloquism']
                         } ,
              'divine' : {0 : [''],
                          1 : ['']
                          } ,
              'occult' : { 0 : [''],
                           1 : ['']
                         } ,
              'primal' : { 0 : [''],
                           1 : ['']
                         }
                    }         
