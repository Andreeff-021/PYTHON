# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt
# в одной строке одно число.

from random import randint

n = int(input('Введите число N: '))

list_n= []
for i in range(-abs(n), abs(n) + 1):
    list_n.append(i)
print(list_n)

with open('file.txt', 'r') as f:
    res = list_n[int(f.readline())] * list_n[int(f.readline())]
print(res)