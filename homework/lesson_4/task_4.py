# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100)* многочлена и записать в файл многочлен степени k.
#     *Пример:*
#     - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
#     -  k=5 => 2*x^5 + 4*x^4 + 2*x^3 + 2*x^2 + 4*x + 5 = 0

from random import randint


def write_file(st):
    with open('file_1txt', 'w') as data:
        data.write(st)


def lst_koef(k):
    lst = [randint(0, 101) for i in range(k + 1)]
    return lst


def polynomial(sp):
    lst = sp[::-1]
    st = ''
    if len(lst) < 1:
        st = 'x = 0'
    else:
        for i in range(len(lst)):
            if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
                st += f'{lst[i]}x^{len(lst) - i - 1}'
                if lst[i + 1] != 0:
                    st += ' + '
            elif i == len(lst) - 2 and lst[i] != 0:
                st += f'{lst[i]}x'
                if lst[i + 1] != 0:
                    st += ' + '
            elif i == len(lst) - 1 and lst[i] != 0:
                st += f'{lst[i]} = 0'
            elif i == len(lst) - 1 and lst[i] == 0:
                st += ' = 0'
    return st


k = int(input("Введите натуральную степень k = "))
koef = lst_koef(k)
write_file(polynomial(koef))
print(polynomial(koef))