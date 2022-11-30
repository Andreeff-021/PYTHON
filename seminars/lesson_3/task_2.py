# Задайте список. Напишите прогорамму, которая определит,
# присутствует ли в заданном списке строк некое число.

lst = ['blue', 'green', 'white', 'grv2', 'red']
num = 4
answer = False

for i in lst:
    if i.count(str(num)):
    # if str(num) in i:
        answer = True
    # for j in i:
    #     if j == str(num):
    #         answer = True
    #         break
print(answer)