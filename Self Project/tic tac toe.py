import itertools


def player_role(x):
    row_position = int(input('Which row do you choose? : row '))
    column_position = str(input('Which column do you choose? : column '))
    if board[row_position][column_index.get(column_position)] != ' ':
        print('place occupied')
        print('Player', player)
        return True
    else:
        print('   a b c')
        for count, row in enumerate(board):
            board[row_position][column_index.get(column_position)] = x
            print(count, '[' + ','.join(row) + ']')


def win():
    # horizontal
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != ' ':
            print(f'Congratulations, Player {player} win the game by horizontally')
            return True
    # vertical
    win = []
    for cols in range(len(board[0])):
        for rows in range(len(board)):
            win.append(board[rows][cols])
        if win.count(win[0]) == len(win) and win[0] != ' ':
            print(f'Congratulations, Player {player} win the game by vertically')
            return True
        win.clear()
    # diagonally
    win = []  # \
    for index in range(len(board)):
        win.append(board[index][index])
    if win.count(win[0]) == len(win) and win[0] != ' ':
        print(f'Congratulations, Player {player} win the game by diagonally (\\)')
        win.clear()
        return True
    # /
    win = []
    for cols, rows in enumerate(reversed(range(len(board[0])))):
        win.append(board[rows][cols])
    if win.count(win[0]) == len(win) and win[0] != ' ':
        print(f'Congratulations, Player {player} win the game by diagonally (/)')
        win.clear()
        return True


player_1 = 'X'
player_2 = 'O'
choice = 'yes'
while choice == 'yes':
    print('\nPlayer 1 is X while Player 2 is O')
    board = [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']]
    column_index = {'a': 0,
                    'b': 1,
                    'c': 2}
    print('   a b c')
    for count, row in enumerate(board):
        print(count, '[' + ','.join(row) + ']')
    player_choice = itertools.cycle([1, 2])
    result = bool(win())
    while not result:
        player = next(player_choice)
        print('Player', player)
        restart = True
        while restart:
            try:
                if player == 1:
                    restart = player_role(player_1)
                elif player == 2:
                    restart = player_role(player_2)
            except ValueError:
                print('please enter the correct input')
            except TypeError:
                print('please enter the correct input')
            result = bool(win())
    choice = input('wish to continue ? (yes / no) :')
