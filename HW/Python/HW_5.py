import random
import names
import randomtimestamp as rt
import string

#1.Написать скрипт который в создаст список целых чисел.
print('Задание 1 -- список целых чисел')
int_list = list(range(1,71))
print(int_list)
print('=' * 70)

#2.Написать скрипт который в создаст список целых чётных чисел.
print('Задание 2 -- список четных числе')
even_list = []

while len(even_list) < 70:
    num = random.randint(1, 500)
    if num % 2 == 0:
        even_list.append(num)

print(even_list)
print('=' * 70)

#3.Написать скрипт который в создаст список целых нечётных чисел.
print('Задание 3 -- список нечетных чисел')
odd_list = []

while len(odd_list) < 70:
    num = random.randint(1, 500)
    if num % 2 != 0:
        odd_list.append(num)

print(odd_list)
print('=' * 70)

#4.Написать скрипт который из списка целых чисел выведет чётные числа.
print('Задание 4 -- четные числа из списка целых чисел')
for i in int_list:
    if i % 2 == 0:
        print(i)

print('=' * 70)

#5.Написать скрипт который из списка целых чисел выведет нечётные числа.
print('Задание 5 -- нечетные числа из списка целых чисел')
for i in int_list:
    if i % 2 != 0:
        print(i)

print('=' * 70)

#6.Написать скрипт который из списка целых чисел выведет чётные числа которые делятся на 5 без остатка.
print('Задание 6 -- четные числа, которые делятся на 5 без остатка')
for i in int_list:
    if i % 2 == 0 and i % 5 == 0:
        print(i)

print('=' * 70)

#7.Написать скрипт который из списка целых чисел выведет количество  чётных чисел которые делятся на 5 без остатка.
print('Задание 7 -- четные числа, которые делятся на 5 без остатка')
count = 0

for i in int_list:
    if i % 2 == 0 and i % 5 == 0:
        count += 1

print('Количество четных чисел, которые делятся на 5 без остатка:', count)
print('=' * 70)

#8.Написать скрипт который  создаст список целых рандомных чисел.
print('Задание 8 -- список рандомных целых чисел')
rand_list = []

for i in range(1,71):
    rand_list.append(random.randint(1, 500))

print(rand_list)
print('=' * 70)

#9.Написать функцию которая, получив на вход любой из выше созданных списков, разобьёт его списки по 5 элементов.
print('Задание 9 -- разбитие списка на списки по 5 элементов')

def sep_list(num_lst, n):
    for i in range(0, len(num_lst), n):
        each_chunk = num_lst[i: n+i]

        if len(each_chunk) < n:
            each_chunk = each_chunk + [None for y in range(n-len(each_chunk))]
        yield each_chunk

print(list(sep_list(int_list, 5)))
print('=' * 70)

#10.Написать функцию которая, получив на вход список целых чисел, вернёт 2 списка, список чётных и список нечётных чисел.
print('Задание 10 -- создание списков с четными и нечетными числами из списка целых чисел')
def odd_even_list(lst):
    odd_lst = []
    even_lst = []

    for i in lst:
        if i % 2 == 0:
            even_lst.append(i)
        else:
            odd_lst.append(i)

    return even_lst, odd_lst

even_lst, odd_lst = odd_even_list(int_list)
print('Список четных чисел:', even_lst)
print('Список нечетных числе:', odd_lst)
print('=' * 70)

#11.Написать скрипт который сгенерирует список под названием 5_stars из списков по 5 элементов целых чисел.
print('Задание 11 -- список со списками по 5 элементов')
stars_5 = []

for i in range(5):
    arr = []
    for ii in range(5):
        arr.append(random.randint(1,30))
    stars_5.append(arr)

print(stars_5)
print('=' * 70)

#12.Написать скрипт который выведет список из сумм каждого внутреннего списка из  5_stars
print('Задание 12 -- список сумм каждого внутреннего списка')
sum_stars_5 = []

for i in range(len(stars_5)):
    sum = 0

    for ii in range(len(stars_5[i])):
        sum += stars_5[i][ii]

    sum_stars_5.append(sum)

for i in range(len(sum_stars_5)):
    print('Сумма списка ',stars_5[i], ' =', sum_stars_5[i])

print('=' * 70)

#13.Написать функцию которая на вход получает список 5_stars, а вернёт 2 списка. В одном списке внутренние списки из 5_stars сумма чисел которых >= 100, а другой сумма чисел которых < 100. Если какого-то списка не получится, то вместо него вернуть текст “No lists”
print('Задание 13 -- список с суммами больше 100 + список с суммами меньше 100')
def sum_stars_more_100(lst):
    more_100 = []
    less_100 = []

    for i in range(len(lst)):
        sum = 0

        for ii in range(len(lst[i])):
            sum += lst[i][ii]

        if sum >= 100:
            more_100.append(lst[i])
        elif sum < 100:
            less_100.append(lst[i])

    if more_100 == []:
        more_100 = 'No lists'
    elif less_100 == []:
        less_100 = 'No lists'

    return more_100, less_100

more_100, less_100 = sum_stars_more_100(stars_5)
print('Списки, с суммой значений >= 100:', more_100)
print('Списки, с суммой значений < 100:', less_100)
print('=' * 70)

#14.Написать функцию которая получив на вход ваш возраст, выведет вам через какой срок вы сумеете отложить 10 000$, 20 000$, 30 000$, 50 000$, 100 000$ в кубышку.
# def kubyshechka(age):
print('Задание 14 -- кубышка')
def kubyshka(age=24):
    koef = random.randint(1,5)
    if age < 18:
        koef = random.randint(10, 15)
    elif 18 <= age <= 23:
        koef = random.randint(7, 10)
    elif 24 <= age <= 27:
        koef = random.randint(5, 7)
    elif 28 <= age <= 32:
        koef = random.randint(4, 6)
    elif 33 <= age <= 40:
        koef = random.randint(3, 6)
    elif 41 <= age <= 60:
        koef = random.randint(2, 4)
    elif 61 <= age <= 90:
        koef = random.randint(1, 3)
    elif 90 < age:
        return print("Вам больше не нужны деньги, отдыхайте!")
    res_10 = koef + 1
    res_20 = koef + 2
    res_30 = koef + 3
    res_50 = koef + 5
    res_100 = koef + 7
    result = ("Вы положите 10 000 в кубышку через: " + str(res_10) + ' лет' +
    "\nВы положите 20 000 в кубышку через " + str(res_20) + ' лет' +
    "\nВы положите 30 000 в кубышку через " + str(res_30) + ' лет' +
    "\nВы положите 50 000 в кубышку через " + str(res_50) + ' лет' +
    "\nВы положите 100 000 в кубышку через " + str(res_100) + ' лет')
    print(result)

age = int(input('Введите ваш возраст: '))
kubyshka(age)
print('=' * 70)

#15.Написать функцию которая получив на вход стартовую ЗП Junior QA и количество лет стажа выведет в консоль прогресс роста ЗП по каждому году из введенного количества лет стажа. Внутри функция учитывает дорожную карту развития скилов QA и список, полезных для компании, активностей которые может делать QA. Free implementation of function body logic

#16.Написать скрипт который сгенерирует список имён пользователей. Список имён вывести в консоль.
print('Задание 16 -- список рандомных имен')
rand_names = []

for i in range(1,71):
    rand_names.append(names.get_full_name())

print(rand_names)
print('=' * 70)

#17.Написать скрипт который сгенерирует список имён файлов. К каждому имени  файла надо прикрепить номер итерации цикла как порядковый номер.
print('Задание 17 -- список имен файлов')
src_names = ['file'] * 70
file_names = []

for i in range(len(src_names)):
    file_names.append(src_names[i] + '_' + str(i+1))

print(file_names)
print('=' * 70)

#18.Написать скрипт который сгенерирует список списков. Каждый элемент списка это список в котором:
# 0-й элемент - это имя пользователя
# 1-й - элемент это дата регистрации.
print('Задание 18 -- рандомные имя пользователя + дата регистрации')
users_list = []

for i in range(70):
    users_list.append(['', ''])
    users_list[i][0] = names.get_full_name()
    users_list[i][1] = rt.randomtimestamp(start_year=2017, end_year=2021, text=True)

print(users_list)
print('=' * 70)

#19.Написать скрипт который сгенерирует список Employees списков . Каждый элемент списка - это список в котором:
# 0-й - элемент - это имя пользователя,
# 1-й - элемент - это логин,
# 2-й - элемент - это пароль,
# 3-й - элемент - это email (email тоже генерировать),
# 4-й - элемент - это дата регистрации
print('Задание 19 -- список employee с рандомным именем пользователя, логином, паролем, почтой и датой регистрации')
employees = []
mail = '@gmail.com'
genders = []

def get_random_string(length, case):
    if case == 0:
        return ''.join(random.choice(string.ascii_lowercase) for i in range(length))
    if case == 1:
        return ''.join(random.choice(string.ascii_letters) for i in range(length))

for i in range(70):
    employees.append(['', '', '', '', ''])
    login_length = random.randint(2, 6)
    pass_length = random.randint(8, 20)
    gender_k = random.randint(0, 1)
    if gender_k == 0:
        name = names.get_full_name(gender='female')
        genders.append(0)
    if gender_k == 1:
        name = names.get_full_name(gender='male')
        genders.append(1)
    employees[i][0] = name
    name_temp = employees[i][0].split(' ')
    employees[i][1] = name_temp[0] + '_' + get_random_string(login_length, 0)
    employees[i][2] = get_random_string(pass_length, 1)
    employees[i][3] = name_temp[0] + '_' + name_temp[1] + mail
    employees[i][4] = rt.randomtimestamp(start_year=2017, end_year=2021, text=True)

print(employees)
print('=' * 70)

#20.Написать скрипт который сгенерирует список family списков. Каждый элемент списка - это список в котором:
# 0-й - элемент - это логин,
# 1-й - элемент - это имя,
# 2-й - элемент - семейный статус (True, False - генерировать рандомно)
print('Задание 20 -- список family с семейным статусом (True - женат/замужем, False - холост')
family = []

for i in range(70):
    family.append(['', '', ''])
    family[i][0] = employees[i][1]
    family[i][1] = employees[i][0]
    married = random.randint(0,1)
    if married == 0:
        family[i][2] = False
    if married == 1:
        family[i][2] = True

print(family)
print('=' * 70)

#21.Написать скрипт который сгенерирует список gender списков. Каждый элемент списка - это список в котором:
# 0-й - элемент - это логин,
# 1-й - элемент - это имя,
# 2-й - элемент - гендер (1-м, 0-ж)
print('Задание 21 -- список gender с полом (0 - жен, 1 - муж)')
gender = []

for i in range(70):
    gender.append(['', '', ''])
    if genders[i] == 0:
        gender[i][2] = 0
    if genders[i] == 1:
        gender[i][2] = 1
    gender[i][0] = employees[i][1]
    gender[i][1] = employees[i][0]

print(gender)
print('=' * 70)

#22.Написать скрипт который сгенерирует список salary списков. Каждый элемент списка - это список в котором:
# 0-й - элемент - это логин,
# 1-й - элемент - это имя,
# 2-й - элемент - зарплата (генерироовать от 300$ до 5000$)
print('Задание 22 -- список salary с зарплатами')
salary = []

for i in range(70):
    salary.append(['', '', ''])
    salary[i][0] = employees[i][1]
    salary[i][1] = employees[i][0]
    salary[i][2] = random.randint(300, 5000)

print(salary)
print('=' * 70)

#23.Написать скрипт который создаст список имён работников из salary у которых ЗП от 1500$ до 3000$
print('Задание 23 -- имена сотрудников с запрлатой от 1500$ до 3000$')
salary_1500_300 = []

for i in range(len(salary)):
    if 1500 < salary[i][2] < 3000:
        salary_1500_300.append(salary[i][1])

print(salary_1500_300)
print('=' * 70)

#24.Написать скрипт который создаст список имён мужчин из gender.
print('Задание 24 -- имена мужчин')
male_gender = []

for i in range(len(gender)):
    if gender[i][2] == 1:
        male_gender.append(gender[i][1])

print(male_gender)
print('=' * 70)

#25.Написать скрипт который создаст список имён женщин из gender.
print('Задание 25 -- имена женщин')
female_gender = []

for i in range(len(gender)):
    if gender[i][2] == 0:
        female_gender.append(gender[i][1])

print(female_gender)
print('=' * 70)


#26.Написать скрипт который создаст список имён неженатых мужчин из family.
print('Задание 26 -- имена неженатых мужчин')
not_married_male = []

for i in range(len(gender)):
    if gender[i][2] == 1 and family[i][2] == False:
        not_married_male.append(employees[i][0])

print(not_married_male)
print('=' * 70)

#27.Написать скрипт который создаст список имён незамужних женщин из family.
print('Задание 27 -- имена незамужних женщин')
not_married_female = []

for i in range(len(gender)):
    if gender[i][2] == 0 and family[i][2] == False:
        not_married_female.append(employees[i][0])

print(not_married_female)
print('=' * 70)


#28.Написать скрипт который создаст список имён неженатых мужчин с ЗП больше или равной 1500$. Используйте Employees, family, gender, salary. Реализуйте как скрипт, без функций
print('Задание 28 -- неженатые мужчины с зарплатой больше или равно 1500$')
not_married_male_1500 = []

for i in range(len(gender)):
    if gender[i][2] == 1 and family[i][2] == False and salary[i][2] >= 1500:
        not_married_male_1500.append(employees[i][0])

print(not_married_male_1500)
print('=' * 70)

#29.Реализуйте пункт 28 через через функции.
print('Задание 29 -- неженатые мужчины с зарплатой больше или равно 1500$ через фукнцию')

def rich_lonely_man():
    not_married_male_1500_def = []
    for i in range(len(gender)):
        if gender[i][2] == 1 and family[i][2] == False and salary[i][2] >= 1500:
            not_married_male_1500_def.append(employees[i][0])
    print(not_married_male_1500_def)

rich_lonely_man()
print('=' * 70)

#30.Поешьте и выспитесь)
print('Сон для слабаков')
