# Реализуйте алгоритм нахождения(генерации) рандомного(случайного) числа.
# (Не используя библиотеки связанные с рандомом)

import datetime

low = int(input('Введите нижнее значение: '))
up = int(input('Введите верхнее знаенеи: '))

rand = int(datetime.datetime.now().microsecond % 10) * (up - low) + low
print(rand)