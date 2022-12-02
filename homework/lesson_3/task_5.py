# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
#     - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

n = int(input('Введите число: '))

def fib(n):
    if n in [0, 1]:
        return n
    return fib(n - 1) + fib(n - 2)

def negfib(n):
    return (-1) ** (n + 1) * fib(n)

lst_fib = []

for i in range(n + 1):
    lst_fib.insert(0, negfib(i))

lst_fib.pop(-1)

for i in range(n + 1):
    lst_fib.append(fib(i))

print(lst_fib)



