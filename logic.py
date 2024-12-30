import random

# initialize game
def start_game():
    mat = []
    for i in range(4):
        mat.append([0] * 4)
    # mat = [[0, 0, 0, 0], [...], ...]

    # print instructions for users
    print("press '1' to move left")
    print("press '2' to move down")
    print("press '3' to move up")
    print("press '4' to move right")

    # add a new number in grid
    add_new_number(mat)
    return mat

# add a new number in grad at random empty cell
def add_new_number(mat):
    r = random.randint(0, 3)
    c = random.randint(0, 3)

    # if cell not empty, choose a new cell
    while(mat[r][c] != 0):
        r = random.randint(0, 3)
        c = random.randint(0, 3)

    # new number is either 2 or 4
    if random.randint(0, 2):
        mat[r][c] = 2
    else:
        mat[r][c] = 4


def get_current_state(mat):
    # check if user has won
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 2048:
                return 'YOU WON'

    for i in range(4):
        for j in range(4):
            if mat[i][j] == 0:
                return 'Please continue'

            if i <= 2:
                if mat[i][j] == mat[i+1][j]:
                    return 'Please continue'
            if j <= 2:
                if mat[i][j] == mat[i][j+1]:
                    return 'Please continue'

    return 'YOU LOST'

def compress(mat):
    changed = False
    new_mat = []
    for i in range(4):
        new_mat.append([0] * 4)

    for i in range(4):
        pos = 0
        for j in range(4):
            # if cell not empty, move number to previous empty in that row
            if mat[i][j] != 0:
                new_mat[i][pos] = mat[i][j]
                # if nonempty cell is moved to different cell, mark 'changed'
                if j != pos:
                    changed = True
                # count non-empty cells
                pos += 1
    return new_mat, changed

def merge(mat):
    changed = False
    for i in range(4):
        for j in range(3):
            if mat[i][j] == mat[i][j+1] and mat[i][j] != 0:
                mat[i][j] = mat[i][j] * 2
                mat[i][j+1] = 0
                changed = True
    return mat, changed

# reverse the content of each row
def reverse(mat):
    new_mat = []
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[i][3-j])
    return new_mat

# ginterchange rows and columns
def transpose(mat):
    new_mat = []
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[j][i])
    return new_mat    

def move_left(grid):
    new_grid, changed1 = compress(grid)
    new_grid, changed2 = merge(new_grid)
    changed = changed1 or changed2
    new_grid, temp = compress(new_grid)
    return new_grid, changed

def move_right(grid):
    new_grid = reverse(grid)
    new_grid, changed = move_left(new_grid)
    new_grid = reverse(new_grid)
    return new_grid, changed
        
def move_up(grid):
    new_grid = transpose(grid)
    new_grid, changed = move_left(new_grid)
    new_grid = transpose(new_grid)
    return new_grid, changed

def move_down(grid):
    new_grid = transpose(grid)
    new_grid, changed = move_right(new_grid)
    new_grid = transpose(new_grid)
    return new_grid, changed
