#import packed.module_one as module_new
# или импорт только методов и ф-ий из модуля
#from packed.module_one import print_name
# FUNCTION   def name():

# LIST ['str', 5, True, ['a', 'b'], {'a': 1, 'b': 2}]
# LIST [] - список изменяемые упорядоченные неуникальные значения
# TUPLE () - кортеж неизменяемые упорядоченные неуникальные значения
# SET {} - множества изменяемые неупорядоченные уникальные значения
# RANGE () - диапазон неизменяемые упорядоченные уникальные значения
# DICT {} - словарь изменяемые неупорядоченные уникальные значения
# STR " " - строка неизменяемые упорядоченные неуникальные значения

# module_new.print_name("OKK")
#print_name("str")
"""
method LIST  len(list) ,  del list[2], append, pop, remove, isert, sort,
index, clear, copy, extend, reverse,

copy list
1) new_list = old_list[:]
2) new_list = old_list.copy()
3) new_list = list(old_list)




my_list = [1, 8, 2, 5, 'st', [3, 8]]
new_list = [8, 'c', False]
# print(my_list)
# my_list.pop(-1)
# my_list.pop(-1)
# print(my_list.add(new_list))
# print(my_list.sort(reverse=True))

# DICT
#
my_dict = {'a': 1, 'b': 'c', 'f': {'g': 9, 10: 'ok'}}
my_dict['b'] = 'new'
my_dict['e'] = 'new2'
del my_dict['b']

print(my_dict['f']['g'])
print(len(my_dict))
print(my_dict.get('name'))  # return None, not Error

print(my_dict.get('name', 'Pupkin'))
print(my_dict)
my_new_dict = my_dict.copy()
print(my_new_dict)
#convert
var_list = [['one', 1], ['two', 2]]
var_dict = dict(var_list)
print(var_dict)

key_1 = input('введите 1 ключ: ')
val_1 = input('введите 1 значение: ')
key_2 = input('введите 2 ключ: ')
val_2 = input('введите 2 значение: ')
dict_input = {key_1: val_1, key_2: val_2}
print(dict_input)


# TUPLE  упорядоченный неизменяемый
my_tuple = ('a', 123, True, {'user_id': 154, 'user_name': 'Vasy'})
print(my_tuple[3]['user_name'])
# кортежи можно преобразовывать в списки (изменять) и конвертировать обратно.



# SET  НАБОРЫ - неупорядоченная изменяемая последовательность уникальныж эл-ов
# methods  add, union, remove, differince, intersection, discard, clear, copy, update ...
my_set = {'one', '44', 'two'}
size_smal = { '480', '800'}
size_big  = {'800', '1024', '1920'}
all_size = size_smal.union(size_big) # ( или | ) {'480', '800', '19200'}
commin_size = size_smal.intersection(size_big) # (или & ) {'800'}
res = size_smal.issubset(size_big) # false проверка включен ли small полностью в big
#print(my_set)



# RANGE диапазон - упорядоч. неизм. послед. эл-ов. ~ используются в циклах
# my_range = range(1, 22, 2) # нечетные с 1 по 21
# print(list(my_range))
for n in range(1, 11):
    for c in range(1, 11):
        print(n * c)



let = ['a', 'b', 'c']
integ = [5, 7, 10]
logic = ['y', 'n', 'n']
print(list(zip(let, integ, logic))) # при ковертации zip  объекта в список - список кортежей
print(dict(zip(let, integ))) # при ковертации zip  объекта в словарь

# ИЗМЕНЕНИЕ ОБЪЕКТОВ

Переменная содержит ссылку на объект, с помощью id(var) можно узнать адрес в памяти
как избежать изменений при копировании
info = {
    'name': 'Vasy',
    'age': '30'
}

1)  info_copy = info.copy()
подходит для неизменяемых объектов (строки, целые числа, кортежи)

2) создание полной копии с помощью модуля
from copy import deepcopy
info_copy = deepcopy(info)

"""

"""
FUNCTIONS
def my_sum(a = 0, b = 0):
    return a +b
# объединение всех аргументов в кортеж в ф-ии
def sum_num(*args):
    return sum(args)

print(sum_num(1, 3, 8, 9)) # 21

#Объединение именованных аргументов в словарь

def dict_arr(**el):
    info = (
        f"My name is {el['name']} and, "
        f"me {el['age']} years"
    )
    return info

print(dict_arr(name='Vasy', age=32))

# ОПЕРАТОРЫ
# арифметичесие + - / *
#  сравнения == === != > <
# логические  and or not  is , is not , not in , in
# присвоения =

# распаковка словарей
one_dict = {"one": 1, "two": 2}
next_dict = {
    **one_dict,
    "three":3
}
print(next_dict) # {'one':1, 'two': 2, 'three': 3}


# объединение 2 словарей
new_dict = {
    **one_dict,
    **two_dict,
}
 new_dict = one_dict | two_dict # аналогичное объединение словарей

# инструкция del  удаления элемента
del new_dict['one'] # new_dict.__delitem__.('one')

# соединение строк  STRING
hell = "Hellow"
name = "Jon"
#new_str = hell + " " + name

# форматирование строк
new_str = f"{hell} {name}"
print(new_str)

# лямбда функции (анонимные)
# lambda parametrs: expression
lambda a, b: a * b

def hell(text):
    return lambda name: f'{text} {name}'

new_hell = hell("Добрый день")

print(new_hell("Павел"))

# РАСПАКОВКА СПИСКОВ И КОРТЕЖЕЙ - извлечение значений и присв. их переменным

my_fruits = ['apple', 'banana', 'lime']
my_fruits = ('apple', 'banana', 'lime')
my_apple, my_banana, my_lime = my_fruits
my_apple, *remaining_fruits = my_fruits # my_apple - apple, my_fruits - ('banana', 'lime')
print(my_banana)

if x > 0:
    print(x)
elif x == 0:
    print(x + " - zerro"
else:
    print(x + " - another)

# ТЕРНАРНЫЙ ОПЕРАТОР
funct_1(arr) if arr.get['example'] else funct_2(arr)   # вызов разных ф-й в завис от усл
var = 'small' if var_2 < 5 else 'big' # присваеваем рез-т переменной

# ЦИКЛЫ
for element in ar_list:
    print(element)

for key in my_dict:
    print(key, my_dict[key])

for item in my_dict.items(): # разбивка словаря на кортежи
    k, v = item  # распаковка кортежей на ключ и значение
    print(k, v)

for k, v in my_dict.items(): # сокращенно
    print(k, v)

for num in range(6):
    print(num)  # 0, 1, 2, 3, 4, 5


one_list = [3, 'ab', {'a': 3, 'b':2}, 7, 'mc', (1, 3, 8), ('a', 'c'), {'b':'c', 'd': 'e'}]

def filter_list(arr, v_type):
    # new_list = []
    # for el in arr:
    #     if type(el) == v_type:
    #         new_list.append(el)
    # return new_list
    # аналог с использованием ф-ии filter
    #def check_type(el):
        #return type(el) is v_type
    #return list(filter(check_type, arr))

    # 2 вариант аналога с исп лямбда ф-ии
    return list(filter(lambda el: type(el) is v_type, arr))


print(filter_list(one_list, str))

# ЦИКЛЫ

while True:
    try:
        val_1 = input('Введите первое число: ')
        val_2 = input('Введите второе число: ')
        print(float(val_1) / float(val_2))
        more = input('Хотите еще (y/n) ? :')
    except ValueError as e:
        print(e)
        print("Можно вводить только числа")
        continue

    if more == 'n':
        break

# сокращенный for in использ для создания новых последовательностей  list, tuple, set, dict
nums = [-2, 3, 0, -16, 65]
abs_nums = [abs(num) for num in nums]
print(abs_nums)
positive_nums = [num for num in nums if num > 0]
print(positive_nums)

my_set = {3, 5, 15}
new_set = {val * val for val in my_set}
print(new_set)

my_dict = {'a': 2, 'b': 5, 'c': 16}
new_dict = {k: v * 10 for k, v in my_dict.items() if v % 2 == 0}
print(new_dict)

my_list = ['a', 10, 'ok']
new_dict = {index: elem for index, elem in enumerate(my_list)}
print(new_dict)

"""

"""
class Comment():
    def __init__(self, text):
        self.text = text
        self.votes_qty = 0
        self.step_qty = 0

    def __add__(self, other):
        return [f"{self.text} {other.text}", self.votes_qty + other.votes_qty]

    def up_vote(self):
        self.votes_qty += 1

    def up_step(self, qty):
        self.step_qty += qty

    @staticmethod # Декоратор, те данный м-д не привязан к данному экз класса, вызыв на уровне и класса и экземпляра кл
    def merge_comment(first, second):
        return f"{first} {second}"

first_comment = Comment("Первый комментарий")
second_comment = Comment("Второй комментарий")
print(first_comment.text)
print(first_comment.votes_qty)
first_comment.up_vote()
first_comment.up_step(5)
print(first_comment.votes_qty)
print(first_comment.step_qty)
print(first_comment + second_comment)

print(Comment.merge_comment("Первый комментарий", "Второй комментарий"))
print(first_comment.merge_comment("1 comment", "2 comment"))

# создание подклассов
class ExtendedList(list): # (list) - класс от которого наследуется новых с наслед методов
    def print_list_info(self):
        print(f"List has {len(self)} elements")

castom_list = ExtendedList([3,5,7])
castom_list.print_list_info()
castom_list.append(9)
castom_list.print_list_info()

# Декораторы - ф-ии которые автоматически выполняют наши ф-ции

def decorator_function(original_fn):
    def wrapper_function(*args, **kwargs):
        print("executed before function")
        result = original_fn(*args, **kwargs)
        print("executed after function")
        return result
    return wrapper_function

@decorator_function
def my_function(a, b, c):
    print("This my function!")
    return (a, b, c)

res = my_function(10, 30, 'b')
print(res)


#==========================

def log_funtction(fn):
    def wrapper(*args, **kwargs):
        print(f"function name is {fn.__name__}")
        print(f"function arguments are {args}, {kwargs}")
        result = fn(*args, **kwargs)
        print(f"function result {result}")
        return result

    return wrapper


@log_funtction
def mult(a, b):
    return a * b

@log_funtction
def sum(a, b):
    return a + b

print(mult(5, 3))
print("")
print(sum(a=8.3, b=9.1))
#======================================
def validate_num(fn):
    def wrapper(*args, **kwargs):
        for arg in [*args, *kwargs.values()]:
            if not isinstance(arg, int) and not isinstance(arg, float):
                raise ValueError(f"Type of the {arg} is {type(arg)}",
                                 "All arguments must be int or float!")

        return fn(*args, *kwargs)

    return wrapper

@validate_num
def sum_nums(a, b):
    return a + b
try:
    print(sum_nums(5,4))
    print(sum_nums(4.9, 4.7))
    print(sum_nums("ok", b=4.7))

except ValueError as e:
    print(e)
"""



"""
# MODULES
# Любой файл с расширением .py является модулем
 if (__name__ == __main__):
    если файл выполняется напрямую то true, если импортирован то false

# Встроенные модули csv, random, os, zipfile и тп
получить информацию о модуле help('csv')

 help('modules')
"""

