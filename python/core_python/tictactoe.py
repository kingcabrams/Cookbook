the_board = {'1': ' ', '2': ' ', '3': ' ', '4': ' ', '5': ' ', '6': ' ',
        '7': ' ', '8': ' ', '9': ' '}

def print_board(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])

turn = 'X'
for i in range(9):
    print_board(the_board)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    the_board[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'


print_board(the_board)
