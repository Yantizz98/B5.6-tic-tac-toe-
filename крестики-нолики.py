board = list(range(1, 10))


def draw_board(board):
    print('-' * 13)
    for i in range(3):
        print('|', board[0 + i*3], '|', board[1 + i*3], '|', board[2 + i*3], '|')
        print('-' * 13)


def take_input(player_pin):
    vld = False
    while not vld:
        player_answer = input(f'Where to put the {player_pin} ?')
        try:
            player_answer = int(player_answer)
        except ValueError:
            print('Incorrect input')
            continue
        if 1 <= player_answer <= 9:
            if str(board[player_answer -1]) not in'XO':
                board[player_answer -1] = player_pin
                vld = True
            else:
                print('This cell is already occupied')
        else:
            print('Incorrect input. Enter a number from 1 to 9')


def check_win(board):
    win_comb = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for i in win_comb:
        if board[i[0]] == board[i[1]] == board[i[2]]:
            return board[i[0]]
    return False


def game(board):
    cnt = 0
    win = False
    while not win:
        draw_board(board)
        if cnt % 2 == 0:
            take_input('X')
        else:
            take_input('O')
        cnt += 1

        res = check_win(board)
        if res:
            print(f'{res} win!')
            win = True
            break
        if cnt == 9:
            print('drawn game')
            break
    draw_board(board)


game(board)

input('Press Enter for escape')





