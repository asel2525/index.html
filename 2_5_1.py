example = {
	   'iceberg': ['cold', 15, {'a', 'b'}, 33.98, 15/2, False],
	   'fire': ['hot', 46, ['cha', 'ching'], 81.13],
	   'earth': ['solid', 100, (13, 31, 1), 90.01, {'b':'c'}]
	   }

elements = ['fire', 'storm', 'cloud', 'iceberg', 'volcano', 'earth']

def func(dict, lst):
    for i in lst:
        try:
            summ = 0
            for j in dict[i]:
                try:
                    summ += j
                except TypeError:
                    continue
            print(f'{i} == {summ}')
        except KeyError:
            print(f'ключа {i} не существует')

(func(example, elements))

from random import randint

names = ['dhhgfjjhsa.txt', 'hhdsdahffh.txt', 'afdgdhjsds.txt',
         'sggjghddss.txt', 'fjdjgdghdf.txt', 'sjssahjfga.txt',
         'agsgdjhhfj.txt', 'gafadhadda.txt', 'hdagajfhhj.txt',
         'fhjhafhdfa.txt']

name = names[randint(0, len(names)) - 1]
print(name)
with open(name, 'w') as new_file:
    pass


def func(file_names):
    for i in file_names:
        try:
            with open(i, 'r+') as f:
                f.write('Asel')
        except FileNotFoundError:
            print(f'Файла {i} не существует')


func(names)
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
list_super = []
list_2 = []
list_3 = []
for i in lst:
    if i % 2 == 0 and i % 3 == 0:
        list_super.append(i)
    elif i % 3 == 0:
        list_2.append(i)
    elif i % 2 == 0:
        list_3.append(i)

print(list_super)
print(list_2)
print(list_3)

array = '72 101 108 108 111'
array_2 = array.split()
gener_list = [chr(int(i)) for i in array_2]
print(gener_list)
