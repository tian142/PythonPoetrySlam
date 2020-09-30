

poem = open("poem.txt")


def get_file_lines(filename):
    lines_list = filename.readlines()
    print(lines_list)


def lines_printed_backwards(filename):
    lines_list = filename.readlines()
    for line in reversed(lines_list):
        print(line)


get_file_lines(poem)
lines_printed_backwards(poem)
