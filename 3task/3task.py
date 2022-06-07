from math import sqrt
import re


class Line:
    def __init__(self, a, b, c):
        if a == 0 and b == 0 and c == 0:
            print("Error! Not a line! a, b and c equals 0")
        else:
            self.a = a
            self.b = b
            self.c = c

    def __str__(self):
        return "{}x + {}y + {} = 0".format(self.a, self.b, self.c)

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b and self.c == other.c


class Pair:
    def __init__(self, l1, l2):
        self.l1 = l1
        self.l2 = l2


def cal_intersection(a1, b1, a2, b2):
    try:
        x = (b2 - b1) / (a1 - a2)
        y = a1 * (b2 - b1) / (a1 - a2) + b1
        return x, y
    except Exception as e:
        print(str(e))
        return None


def distance_to_zero(x1, y1):
    return sqrt(x1 ** 2 + y1 ** 2)


def find_intersection(lines):
    global min_dist, y, x, pair
    lines_pair = {}
    lines_pair.clear()
    for l1 in lines:
        for l2 in lines:
            if l1 != l2:
                a1 = - l1.a / l1.b
                c1 = - l1.c / l1.b
                a2 = - l2.a / l2.b
                c2 = - l2.c / l2.b
                x, y = cal_intersection(a1, c1, a2, c2)
                if not (x is None and y is None):
                    lines_pair[Pair(l1, l2)] = distance_to_zero(x, y)
    if len(lines_pair) != 0:
        pair = min(lines_pair, key=lines_pair.get)
        min_dist = lines_pair[pair]
        if pair.l1.b != 0:
            a1 = - pair.l1.a / pair.l1.b
            c1 = - pair.l1.c / pair.l1.b
        else:
            a1 = - pair.l1.a
            c1 = - pair.l1.c
        if pair.l2.b != 0:
            a2 = - pair.l2.a / pair.l2.b
            c2 = - pair.l2.c / pair.l2.b
        else:
            a2 = - pair.l2.a
            c2 = - pair.l2.c
        x, y = cal_intersection(a1, c1, a2, c2)

    return [pair, x, y, min_dist] if lines_pair is not None else None


def write_to_file(filename, string):
    file = open(filename, 'w')
    file.write(string)
    file.close()


def read_matrix(filename):
    file = open(filename, "r")
    matrix = []
    for line in file:
        matrix.append([int(x) for x in re.split(", |; | ", line)])
    file.close()
    return matrix


def read_lines(matrix):
    lines = []
    for row in matrix:
        lines.append(Line(row[0], row[1], row[2]))
    return lines


def tests():
    for i in range(1, 6):
        input_dir = f"tests/input{i}.txt"
        output_dir = f"tests/output/output{i}.txt"
        run(input_dir, output_dir)


def run(input_dir, output_dir):
    lines_ = read_lines(read_matrix(input_dir))
    intersection = find_intersection(lines_)
    if intersection is not None:
        pair = find_intersection(lines_)[0]
        x = find_intersection(lines_)[1]
        y = find_intersection(lines_)[2]
        min_dist = find_intersection(lines_)[3]
        data = f"{pair.l1}\n{pair.l2}\nx = {x}, y = {y}\ndistance = {min_dist}"
    else:
        data = "No intersections found"
    write_to_file(output_dir, data)


if __name__ == '__main__':
    run("./input.txt", "./output.txt")
    tests()
