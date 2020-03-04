import generator
import info

print ("What is the Party's Level?\n")
g_level = int(input(''))
print ("How many people are in teh party?\n")
p_level = int(input(''))

if g_level ==1:
	Con_list = []
	low_count = 1
	high_count =1
	while low_count >= 3 :
		low_count+=1
		Con_list.append(generator.Con_lot_mid())
	while high_count>=2 :
		high_count+=1
		Con_list.append(generator.Con_lot_high())
	print (Con_list)

elif g_level <=2 or g_level >= 19 :
	Con_list = []
	low_count = 1
	mid_count = 1
	high_count = 1
	while low_count >= 2 :
		low_count+=1
		Con_list.append(Con_mod())
	while mid_count >=2 :
		mid_count +=1
		Con_list.append(generator.Con_lot_mid())
	while high_count >=2 : 
		high_count+=1
    Con_list.append(generator.Con_lot_high())
  print (Con_list)
else : 
  mid_count = 1
  while mid_count >=4 :
    Con_list.append(generator.Con_lot_mid())
  print (Con_list)
