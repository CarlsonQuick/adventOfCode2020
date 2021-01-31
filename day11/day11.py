import numpy as np

def build_board():
    with open('input.txt') as f:
        board = []
        for line in f:
            board.append([l for l in line.strip()])
        return np.array(board)

def in_frame(x,y,board):
    shape = board.shape
    if 0 <= x and shape[0]-1 >= x and 0 <=y and shape[1]-1 >= y:
        return True
    return False
def find_next_seat(x,y, x_iter, y_iter, board):
    next_seat = '.'
    pos_x = x
    pos_y = y
    while next_seat == '.' and in_frame(pos_x + x_iter, pos_y + y_iter, board):
            pos_x += x_iter
            pos_y += y_iter
            next_seat = board[pos_x][pos_y]
    return next_seat
def get_visible(x,y, board):
    surroundings = []

    for x_iter in range(-1,2):
        for y_iter in range(-1, 2):
            if not (x_iter == 0 and y_iter == 0):
                surroundings.append(find_next_seat(x,y,x_iter, y_iter, board))
    return surroundings

def get_surroundings(x,y,board):
    surroundings = []
    shape = board.shape
    x_max = shape[0]-1
    y_max = shape[1]-1
    if x > 0 and y > 0:
        surroundings.append(board[x-1][y-1])
    if x > 0 and y < y_max:
        surroundings.append(board[x-1][y+1])
    if x < x_max and y > 0:
        surroundings.append(board[x+1][y-1])
    if x < x_max and y < y_max:
        surroundings.append(board[x+1][y+1])
    if x > 0:
        surroundings.append(board[x-1][y])
    if x < x_max:
        surroundings.append(board[x+1][y])
    if y > 0:
        surroundings.append(board[x][y-1])
    if y < y_max:
        surroundings.append(board[x][y+1])

    return surroundings

def toggle(x,y,board):
    if board[x][y] == 'L':
        board[x][y] = '#'
    elif board[x][y] == '#':
        board[x][y] = 'L'


def should_toggle(x,y,board):
    #adjacent = get_surroundings(x,y,board)
    adjacent = get_visible(x,y, board)
    if board[x][y] == 'L' and '#' not in adjacent:
        return True
    elif board[x][y] == '#' and adjacent.count('#') >= 5:
        return True
    return False


# def count_occupied(board):
#     shape = board.shape
#
#     for x in range(0,shape[0]):
#         for y in range(0,shape[1]):
#             if
def update_board(board):
    shape = board.shape
    toggle_count = 0
    st = np.zeros(shape=shape, dtype=bool)
    for x in range(0,shape[0]):
        for y in range(0,shape[1]):
            if should_toggle(x,y,board):
                st[x][y] = True
            else:
                st[x][y] = False
    for x in range(0,shape[0]):
        for y in range(0,shape[1]):
            if st[x][y]:
                toggle_count += 1
                toggle(x,y,board)
    return toggle_count

board = build_board()

count = update_board(board)
while count > 0:
    count = update_board(board)
    print(np.count_nonzero(board == '#'), count)

#print(board)

