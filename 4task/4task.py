def read_strings_from_file(filename):
    file = open(filename, "r", encoding="utf-8")
    strings = [str(s) for s in file.read().strip().split("\n")]
    file.close()
    return strings


def read_text_from_file(filename):
    file = open(filename, "r", encoding="utf-8")
    text = ""
    for line in file:
        text += str(line)
    file.close()
    return text


def write_to_file(filename, data):
    file = open(filename, 'w')
    file.write(str(data))
    file.close()


def select_numbers(s):
    l = len(s)
    nums = ""
    i = 0
    while i < l:
        s_num = ''
        a = s[i]
        while '0' <= a <= '9' or a == '.' or a == ',' or a == '-':
            s_num += a
            i += 1
            if i < l:
                a = s[i]
            else:
                break
        i += 1
        if s_num != '':
            nums = nums + s_num + " "
    return nums


def tests():
    for i in range(1, 6):
        input_dir = "tests/input{}.txt".format(i)
        output_dir = "tests/output/output{}.txt".format(i)
        s = read_text_from_file(input_dir)
        nums = select_numbers(s)
        write_to_file(output_dir, nums)


if __name__ == '__main__':
    s = read_text_from_file("./input.txt")
    nums = select_numbers(s)
    write_to_file("./output.txt", nums)
    tests()
