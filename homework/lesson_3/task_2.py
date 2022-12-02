# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
#     - [2, 3, 4, 5, 6] => [12, 15, 16];
#     - [2, 3, 5, 6] => [12, 15]

def power_digit(lst):
    result = 0
    if len(lst) % 2 != 0:
        for i in range(len(lst) // 2 + 1):
            result = lst[i] * lst[-1 - i]
            print(result, end=' ')
    else:
        for i in range(len(lst) // 2):
            result = lst[i] * lst[-1 - i]
            print(result, end=' ')

lst_1 = [2, 3, 4, 5, 6]
lst_2 = [2, 3, 5, 6]

power_digit(lst_1)
print()
power_digit(lst_2)