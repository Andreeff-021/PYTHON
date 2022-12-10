# Создайте программу для игры в ""Крестики-нолики"".

board = list(range(1, 10))

def print_board(lst):
    print('\n|', board[0], '|', board[1], '|', board[2], '|')
    print('\n|', board[3], '|', board[4], '|', board[5], '|')
    print('\n|', board[6], '|', board[7], '|', board[8], '|\n')

print_board(board)

step = 0
game_over = False
count = 0
player = 0

while game_over == False:
    if count % 2 == 0:
        player = 'Крестики'
    else:
        player = 'Нолики'

    step = input(f'{player} ваш ход, введите номер поля: ')
    if step not in str(board):
        print('\nНеверный ввод!')

    else:
        if player == 'Крестики':
            board[int(step) - 1] = 'X'
        else:
            board[int(step) - 1] = '0'
        count += 1

    print_board(board)

    if (board[0] == board[1] == board[2]) \
        or (board[3] == board[4] == board[5]) \
        or (board[6] == board[7] == board[8]) \
        or (board[0] == board[3] == board[6]) \
        or (board[1] == board[4] == board[7]) \
        or (board[2] == board[5] == board[8]) \
        or (board[2] == board[4] == board[6]) \
        or (board[0] == board[4] == board[8]):
        print(f'{player} победили!')
        game_over = True


    if count == 9 and game_over == False:
        game_over = True
        print('Ничья!')