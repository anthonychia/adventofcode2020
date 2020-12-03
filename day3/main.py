import numpy as np
from scipy.sparse import csr_matrix


def gen_whole_matrix(smatrix, slope):
    repeat = (smatrix.shape[0] * slope[1] // smatrix.shape[1]) + 1
    matrix = np.hstack([smatrix for i in range(repeat)])
    return matrix


def check_encountered_trees(matrix, slope):
    matrix = csr_matrix(matrix)
    key_list = np.array(list(matrix.todok().keys()))

    return sum([slope[0] * col == slope[1] * row for row, col in key_list])


f = open('input.txt')
matrix = []

for line in f:
    string = line.replace('.', '0').replace('#', '1').replace('\n', '')
    matrix.append(np.array([int(i) for i in string]))

matrix = np.asmatrix(matrix)
f.close()

# Part 1
print(check_encountered_trees(gen_whole_matrix(matrix, (1, 3)), (1, 3)))

# Part 2
slopes =[(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
trees = []

for slope in slopes:
    trees.append(check_encountered_trees(gen_whole_matrix(matrix, slope), slope))

# to prevent numerical overflow
trees = np.asarray(trees, dtype='int64')

print(np.prod(trees))

