user_grid = []
check_list = ['1','2','3','4','5','6','7','8','9']
results = {}
blocks_of_three_rows = ()


def check_input(row, i=0):
    # This function is now working as expected do not alter!
    global user_grid

    if len(row) != 9:
        row = input(f"Please enter row {i + 1} again: ")
        check_input(row, i)
    else:
        user_grid.append(row)
        return


def grid_maker():
    # This function is now working as expected do not alter!
    global blocks_of_three_rows

    for i in range(9):
        row = input(f"Enter row {i+1}: ")
        check_input(row, i)

    blocks_of_three_rows = ((user_grid[0],
                            user_grid[1],
                            user_grid[2]),

                            (user_grid[3],
                            user_grid[4],
                            user_grid[5]),

                            (user_grid[6],
                            user_grid[7],
                            user_grid[8]))
    check_rows(user_grid)


def check_rows(user_grid):
    # This function is now working as expected do not alter!
    global results
    global check_list
    rows_result = 0

    for i in range(9):
        if sorted(user_grid[i]) == check_list:
            rows_result += 1
            check_squares(user_grid)

        if rows_result == 9:
            results['rows'] = True
        else:
            results['rows'] = False

    check_squares(user_grid)


def check_squares(user_grid):
    # This function is now working as expected do not alter!
    global check_list
    global results
    sq_1 = []
    sq_2 = []
    sq_3 = []

    for i in range(3):
        sq_1 = []
        sq_2 = []
        sq_3 = []
        for j in range(0, 3):
            sq_1.append(blocks_of_three_rows[i][0][j])
            sq_1.append(blocks_of_three_rows[i][1][j])
            sq_1.append(blocks_of_three_rows[i][2][j])

        for j in range(3, 6):
            sq_2.append(blocks_of_three_rows[i][0][j])
            sq_2.append(blocks_of_three_rows[i][1][j])
            sq_2.append(blocks_of_three_rows[i][2][j])

        for j in range(6, 9):
            sq_3.append(blocks_of_three_rows[i][0][j])
            sq_3.append(blocks_of_three_rows[i][1][j])
            sq_3.append(blocks_of_three_rows[i][2][j])

        if check_list == sorted(sq_1) and sorted(sq_2) and sorted(sq_3):
            results[f'block_{i}'] = True
        else:
            results[f'block_{i}'] = False

    check_diagonals(user_grid)


def check_diagonals(user_grid):
    # This function is now working as expected do not alter!
    global check_list
    global results
    l_to_r_diag = []
    r_to_l_diag = []

    for i in range(9):
        l_to_r_diag.append(user_grid[i][i])

    for j in range(8,0,-1):
        r_to_l_diag.append(user_grid[j][j])

    print(f'l_to_r_diag{l_to_r_diag}')
    print(f'r_to_l_diag{r_to_l_diag}')

    if check_list == sorted(l_to_r_diag) and sorted(r_to_l_diag):
        results['diagonals'] = True
    else:
        results['diagonals'] = False


def check_columns():
    # I have got to write this function.
    pass

def check_results():
    # I have got to write this function.
    pass


grid_maker()
print(results)




