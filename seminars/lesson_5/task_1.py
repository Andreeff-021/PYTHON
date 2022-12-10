num1 = int(input("Введите число: "))
num2 = int(input("Введите число: "))

def fun(num):
    i = 2
    lst = []
    while i <= num:
        if num % i == 0:
            lst.append(i)
            num //= i
        else:
            i += 1
    return lst

nod_find = set(fun(num1)).intersection(set(fun(num2)))
nod = 1
for i in nod_find:
    nod = nod * i

nok = num1 * num2 // nod

print(nok)
print(nod)