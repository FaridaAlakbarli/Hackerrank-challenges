import numpy as np


def magic_square(size):
    grid = np.array([[0 for i in range(size)] for j in range(size)])

    if size % 2 == 1:
        mid_index = size // 2
        grid[0][mid_index] = 1

    row = 0
    col = size // 2
    number = 1

    for i in range((size * size) - 1):
        row -= 1
        col += 1
        number += 1

        if row < 0:
            row = size - 1
        if col == size:
            col = 0

        if grid[row][col] == 0:
            grid[row][col] = number
        else:
            row = temp_row
            col = temp_col
            if row + 1 != size:
                row += 1
            else:
                row = 0
            grid[row][col] = number

        temp_row = row
        temp_col = col

    return grid


print(magic_square(int(input())))