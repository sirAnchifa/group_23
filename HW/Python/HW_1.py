# 1) Создать переменную типа String
var_str = 'Я строка!'
# 2) Создать переменную типа Integer
var_int = 24
# 3) Создать переменную типа Float
var_float = 3.14
# 4) Создать переменную типа Bytes
var_bytes = bytes(10)
# 5) Создать переменную типа List
var_list = ['Day', 'Night', 22, True]
# 6) Создать переменную типа Tuple
var_tuple = (1, 2, 4)
# 7) Создать переменную типа Set
var_set = set(var_list)
# 8. Создать переменную типа Frozen set
var_frozenSet = frozenset(var_list)
# 9) Создать переменную типа Dict
var_dict = {'name': 'Olivka', 'age': 23}
# 10) Вывести в консоль все выше перечисленные переменные с добавлением типа данных.
print('Переменная: ', var_str, '\nТип данных: ', type(var_str))
print('Переменная: ', var_int, '\nТип данных: ', type(var_int))
print('Переменная: ', var_float, '\nТип данных: ', type(var_float))
print('Переменная: ', var_bytes, '\nТип данных: ', type(var_bytes))
print('Переменная: ', var_list, '\nТип данных: ', type(var_list))
print('Переменная: ', var_tuple, '\nТип данных: ', type(var_tuple))
print('Переменная: ', var_set, '\nТип данных: ', type(var_set))
print('Переменная: ', var_frozenSet, '\nТип данных: ', type(var_frozenSet))
print('Переменная: ', var_dict, '\nТип данных: ', type(var_dict))
# 11) Создать 2 переменные String, создать переменную в которой сканкатенируете эти переменные. Вывести в консоль.
str1 = 'А я, иду, шагаю '
str2 = 'по Москве...'
full_str = str1 + str2
print(full_str)
# 12) Вывести в одну строку переменные типа String и Integer используя “,” (Запятую)
print(var_str, var_int)
# 13) Вывести в одну строку переменные типа String и Integer используя “+” (Плюс)
print(var_str + str(var_int))
