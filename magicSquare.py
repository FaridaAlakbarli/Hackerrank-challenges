import numpy as np

def magic_square(s):
    matrix = np.array([[8, 1, 6], [3, 5, 7], [4, 9, 2]])

    diff_array = []

    for i in range(4):
        matrix = matrix.swapaxes(0, 1)
        diff = np.abs(matrix-s)
        diff_array.append(sum(sum(diff)))

        matrix = np.flip(matrix, axis=0)
        diff = np.abs(matrix - s)
        diff_array.append(sum(sum(diff)))

    return min(diff_array)


s = []

for _ in range(3):
    s.append(list(map(int, input('Enter 3 numbers: ').rstrip().split())))

print(magic_square(s))