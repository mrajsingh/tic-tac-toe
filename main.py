def is_win(board, mark):
    print(f'{mark}')
    return ((board[0] == mark and board[1] == mark and board[2] == mark) or
            (board[0] == mark and board[3] == mark and board[6] == mark) or
            (board[0] == mark and board[4] == mark and board[8] == mark) or
            (board[2] == mark and board[5] == mark and board[8] == mark) or
            (board[2] == mark and board[4] == mark and board[6] == mark) or
            (board[3] == mark and board[4] == mark and board[5] == mark) or
            (board[6] == mark and board[7] == mark and board[8] == mark) or
            (board[1] == mark and board[4] == mark and board[7] == mark))


def draw(board):
    print(f'{board[0]}         | {board[1]}     | {board[2]}')
    print(f'          |       |')
    print(f'__________+_______+_________')
    print(f'{board[3]}         | {board[4]}     | {board[5]}')
    print(f'          |       |')
    print(f'__________+_______+_________')
    print(f'{board[6]}         | {board[7]}     | {board[8]}')
    print(f'          |       |')


def start_game(symbol, board):
    move = 0
    last_player = 1
    win = False
    list_index = []
    while not win and move < 9:
        print(f'Player {last_player}')
        index = int(input("Enter place "))
        if index in list_index:
            print(f'{index} is invalid')
            continue
        else:
            list_index.append(index)
        board[index] = symbol[last_player - 1]
        draw(board)
        win = is_win(board, symbol[last_player - 1])
        if not win:
            move += 1
            if last_player == 1:
                last_player = 2
            else:
                last_player = 1
        else:
            break
    if win:
        print(f'Player {last_player} WINS!!!')
    else:
        print("It's a DRAW!!!")


def start():
    board = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
    symbol = []
    draw(board)
    player_one_symbol = input("Enter player one symbol O/X")
    if player_one_symbol == 'X':
        symbol = ['X', 'O']
    else:
        symbol = ['O', 'X']
    start_game(symbol, board)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
