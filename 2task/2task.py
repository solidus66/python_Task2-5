import re


def read_matrix(filename):
    file = open(filename, "r")
    matrix = []
    for line in file:
        matrix.append([int(x) for x in re.split(", |; | ", line)])
    file.close()
    return matrix


def matrix_to_str(matrix):
    str_matrix = ''
    for row in matrix:
        for element in row:
            str_matrix += element.__str__() + " "
        str_matrix += "\n"
    return str_matrix


def write_matrix(matrix, filename):
    file = open(filename, 'w')
    file.write(matrix_to_str(matrix))
    file.close()


def change_min_max(matrix):
    min = matrix[0][0]
    c_min = -1
    max = matrix[0][0]
    c_max = -1
    for j in range(len(matrix[0])):
        for i in range(len(matrix)):
            if matrix[i][j] <= min:
                min = matrix[i][j]
                c_min = j
            if matrix[i][j] > max:
                max = matrix[i][j]
                c_max = j

    if c_min != c_max:
        for i in range(len(matrix)):
            temp = matrix[i][c_min]
            matrix[i][c_min] = matrix[i][c_max]
            matrix[i][c_max] = temp
    else:
        print("Минимальный и максимальный элемент в одном столбце")
    if c_max == -1:
        print("Нет максимального элемента")
    if c_min == -1:
        print("Нет минимального элемента")


if __name__ == '__main__':
    matrix0 = read_matrix("./input.txt")
    change_min_max(matrix0)
    write_matrix(matrix0, "./output.txt")
