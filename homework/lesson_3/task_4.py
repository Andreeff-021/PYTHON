# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
#     - 45 -> 101101
#     - 3 -> 11
#     - 2 -> 10

def conversion_to_binary(n):
    if n <= 0:
        return
    conversion_to_binary(n // 2)
    print(n % 2, end='')
n = 45
conversion_to_binary(n)
