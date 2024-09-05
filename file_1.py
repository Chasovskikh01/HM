import os.path
import os


def acointing(file:str) -> int:
	return sum(1 for _ in open('1.txt', 'rt', encoding = 'utf-8'))



# # 1 Задача
with open('recept.txt', encoding = 'utf-8') as file:
	cook_book = {}
	for i in file:
		recept_name = i.strip()
		ingridient_count = file.readline()
		ingridient = []
		for p in range(int(ingridient_count)):
			recept = file.readline().strip().split(' | ')
			product, quantity, word = recept
			ingridient.append({'product': product, 'quantity': quantity, 'measure': word})
		file.readline()
		cook_book[recept_name] = ingridient



# 2 Задача
def get_shop_list_by_dishes(person_count: int, dishes: list):
    result = {}
    for dish in dishes:
        if dish in cook_book:
            for consist in cook_book[dish]:
                if consist['product'] in result:
                    result[consist['product']]['quantity'] += consist['quantity'] * person_count
                else:
                    result[consist['product']] = {'measure': consist['measure'],'quantity': (consist['quantity'] * person_count)}
        else:
            print('Такого блюда нет в книге')
    print(result)
get_shop_list_by_dishes(2, ['Запеченный картофель', 'Омлет'])




# 3 Задача
def rewriting(file_for_writing: str, base_path, location):
	files = []
	for i in list(os.listdir(os.path.join(base_path, location))):
		files.append([acounting(os.path.join(base_path, location, i)), os.path.join(base_path, location, i), i])
	for file_from_list in sorted(files):
		opening_files = opne(file_for_writing, 'a')
		opening_files.write(f'{file_from_list[2]}\n')
		opening_files.write(f'{file_from_list[0]}\n')
		with open(file_from_list[1], 'r', encoding = 'utf-8') as file:
			counting = 1
			for line in file:
				opening_files.write(f'строка № {counting} в файле {file_from_list[2]} : {line}')
				counting += 1
		opening_files.write(f'\n')
		opening_files.close()



file_for_writing = os.path.abspath('C:\\Users\\chaso\\Desktop\\lern Python\\MH\\1.txt')
base_path = os.getcwd()
location = os.path.abspath('C:\\Users\\chaso\\Desktop\\lern Python\\MH')
rewriting(file_for_writing, base_path, location) 

