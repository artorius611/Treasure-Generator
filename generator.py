import random
import info
print ("What is the Party's Level?\n")
g_level = int(input(''))
class Con_loot_low () :
    g_level -= 1
    con_loot = info.Con_treasure.con_loot
    def __init__ (self):
        con_list_choice = []
        self.con_list = {}
        for k in self.con_loot.keys() :
            con_list_choice.append(k)
        con_sel = len(con_list_choice)
        self.con_list = self.con_loot[con_sel]
        con_loot_low = self.con_loot[g_level-1]
        con_list_choice = []
        for k in con_loot_low.keys() :
            con_list_choice.append(k)
        con_sel = len(con_list_choice)
        con_choice = con_list_choice[random.randint(0,con_sel-1)]
        con_table_low = con_loot_low[con_choice]
        self.con_table_lenth = len(con_table_low)   
        while con_choice == 'scroll' :
            spells = info.Spells.spells
            #created empty list for spell key values
            spell_type = []
            #created empty dictionary for spells and there level
            spell_list = {}
            for k in spells.keys() :
                spell_type.append(k)
            spell_sel = spell_type[random.randint(0,3)]
            spell_list = spells[spell_sel]
            fin_list = spell_list[g_level]
            fin_length = len(fin_list)
            con_table_low = fin_list[random.randint(1,fin_length-1)]

class Con_lot_mid () :
    g_level = 1
    con_loot = info.Con_treasure.con_loot
    def __init__ (self):
        con_list_choice = []
        self.con_list = {}
        for k in self.con_loot.keys() :
            con_list_choice.append(k)
        con_sel = len(con_list_choice)
        self.con_list = self.con_loot[con_sel]
        con_loot_low = self.con_loot[g_level]
        con_list_choice = []
        for k in con_loot_low.keys() :
            con_list_choice.append(k)
        con_sel = len(con_list_choice)
        con_choice = con_list_choice[random.randint(0,con_sel-1)]
        con_table_low = con_loot_low[con_choice]
        self.con_table_lenth = len(con_table_low)
        while con_choice == 'scroll' :
            spells = info.Spells.spells
            #created empty list for spell key values
            spell_type = []
            #created empty dictionary for spells and there level
            spell_list = {}
            for k in spells.keys() :
                spell_type.append(k)
            spell_sel = spell_type[random.randint(0,3)]
            spell_list = spells[spell_sel]
            fin_list = spell_list[g_level]
            fin_length = len(fin_list)
            con_table_low = fin_list[random.randint(1,fin_length-1)]

class Con_lot_high () :
    g_level += 1
    con_loot = info.Con_treasure.con_loot
    def __init__ (self):
        con_list_choice = []
        self.con_list = {}
        for k in self.con_loot.keys() :
            con_list_choice.append(k)
        con_sel = len(con_list_choice)
        self.con_list = self.con_loot[con_sel]
        con_loot_low = self.con_loot[g_level]
        con_list_choice = []
        for k in con_loot_low.keys() :
            con_list_choice.append(k)
        con_sel = len(con_list_choice)
        con_choice = con_list_choice[random.randint(0,con_sel-1)]
        con_table_low = con_loot_low[con_choice]
        self.con_table_lenth = len(con_table_low)
        while con_choice == 'scroll' :
            spells = info.Spells.spells
            #created empty list for spell key values
            spell_type = []
            #created empty dictionary for spells and there level
            spell_list = {}
            for k in spells.keys() :
                spell_type.append(k)
            spell_sel = spell_type[random.randint(0,3)]
            spell_list = spells[spell_sel]
            fin_list = spell_list[g_level]
            fin_length = len(fin_list)
            con_table_low = fin_list[random.randint(1,fin_length-1)]

