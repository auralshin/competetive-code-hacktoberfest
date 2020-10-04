# This is a sudoku solver, created using the backtracking algorithm

def find_empty(b):
    for i in range(len(b)):
        for j in range(len(b[0])): # 9
            if b[i][j] == 0:
                return (i, j)  # row, col
    return False # no empty pieces

def is_valid(b, movement, position):
    for i in range(len(b[0])):
        if b[position[0]][i] == movement and position[1] != i:
            return False
    for i in range(len(b)):
        if b[i][position[1]] == movement and position[0] != i:
            return False
    x = position[1] // 3
    y = position[0] // 3
    for i in range(y*3, y*3 + 3):
        for j in range(x * 3, x*3 + 3):
            if b[i][j] == movement and (i,j) != position:
                return False
    return True    

def main(b):
    piece = find_empty(b)
    if piece:
        r, c = piece # row, column
    else:
        return True # no empty pieces
    for movement in range(1, 10): # iter the board
        valid = is_valid(b, movement, (r, c))
        if valid:
            b[r][c] = movement
            if main(b):
                return True
            b[r][c] = 0
    return False

if __name__ == '__main__':
    # 0's represent empty squares
    board = [
        [7,8,0,4,0,0,1,2,0],
        [6,0,0,0,7,5,0,0,9],
        [0,0,0,6,0,1,0,7,8],
        [0,0,7,0,4,0,2,6,0],
        [0,0,1,0,5,0,9,3,0],
        [9,0,4,0,6,0,0,0,5],
        [0,7,0,3,0,0,0,1,2],
        [1,2,0,0,0,7,4,0,0],
        [0,4,9,2,0,6,0,0,7]
    ]
    print(board)
    print('---------------------SOLVED-----------------')
    main(board)
    print(board)