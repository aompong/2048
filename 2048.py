# import logic.py
import logic

# Driver code
if __name__ == '__main__':
    # initialize grid
    mat = logic.start_game()


while(True):
    x = input("Press the key: ")  

    if x == '\x1b[D':
        mat, flag = logic.move_left(mat)
        status = logic.get_current_state(mat)
        print(status)
        if status == 'Please continue':
            logic.add_new_number(mat)
        else:
            break

    elif x == '\x1b[B':
        mat, flag = logic.move_down(mat)
        status = logic.get_current_state(mat)
        print(status)
        if status == 'Please continue':
            logic.add_new_number(mat)
        else:
            break

    elif x == '\x1b[A':
        mat, flag = logic.move_up(mat)
        status = logic.get_current_state(mat)
        print(status)
        if status == 'Please continue':
            logic.add_new_number(mat)
        else:
            break

    elif x == '\x1b[C':
        mat, flag = logic.move_right(mat)
        status = logic.get_current_state(mat)
        print(status)
        if status == 'Please continue':
            logic.add_new_number(mat)
        else:
            break
    
    else:
        print('invalid key')

    for i in range(4):
        row_string = ''
        for j in range(4):
            if mat[i][j] == 0:
                row_string = row_string + '.'
            else:
                row_string = row_string + str(mat[i][j])

            while len(row_string) % 4 != 0:
                row_string = row_string + ' '
            row_string = row_string + '|'
        print(row_string)
