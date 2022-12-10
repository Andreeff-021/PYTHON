# Создайте программу для игры с конфетами человек против человека.
#
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?


from random import randint

total = 100      # Взял 100 конфет, т.к. с 2021 проверять долго

print(f'На кону конфет: {total}\n'
      f'\nКаждый игрок берет конфеты по очереди, не более 28'
      f'\nКто заберёт все конфеты, тот победитель!\n')

player1 = input('Ввелите имя первого игрока: ').title()
player2 = input('Ввелите имя второго игрока: ').title()
win = 0
loser = 0
rand = randint(0, 2)

if rand == 0:
    win = player1
    loser = player2
    print(f'\n{win} делает первый ход')
else:
    win = player2
    loser = player1
    print(f'\n{win} делает первый ход')

take = 0
player = 0
count = 0

while total > 0:
    if count % 2 == 0:
        player = win
    else:
        player = loser

    take = int(input(f'\n{player} ваш ход! Введите число: '))
    if take <= 0 or take > 28 or take > total:
        print('\nНекорректный ввод!')
    else:
        total -= take
        if total == 0:
            print(f'\n{player} вы победитель!')
        else:
            print(f'\nКонфет осталось {total}')
            count += 1