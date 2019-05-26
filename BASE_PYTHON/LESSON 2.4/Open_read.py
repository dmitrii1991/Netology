cook_book = {}
recipe = []
name = ""
i = 0
with open('recipes.txt',"r", encoding="utf-8") as recipes:
	for line in recipes:

		if  len(line) > 2 and "|"  not in line:
			name = line[0:len(line)-1]
			cook_book[name] = {}
		elif "|"  in line:
			lines = line[0:len(line)-1].split("|")
			recipe += [{'ingridient_name': lines[0], 'quantity': lines[1], 'measure': lines[2]}]
		elif len(line) == 1:
			cook_book[name] = recipe
			recipe = []
	cook_book[name] = recipe


from pprint import pprint
pprint(cook_book)



def get_shop_list_by_dishes(dishes, person_count):
    list_ind = {}
    for dish in dishes:                                                  # блюда
       for ind in  cook_book[dish]:                                     # индигриенты
          if ind['ingridient_name'] in list_ind.keys():
             a = list_ind[ind["ingridient_name"]]["quantity"]
             list_ind[ind['ingridient_name']]= {'measure': ind['ingridient_name'], 'quantity': a+int(ind['quantity'])*person_count}
          else:
            list_ind[ind['ingridient_name']]= {'measure': ind['ingridient_name'], 'quantity': int(ind['quantity'])*person_count}
    pprint(list_ind)

get_shop_list_by_dishes(['Омлет','Запеченный картофель'], 3)
