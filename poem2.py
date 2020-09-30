import random

poem = open("poem.txt")
lines_list = poem.readlines()


def get_file_lines(lines_list):
    print(lines_list)


def lines_printed_backwards(lines_list):
    for i, line in reversed(list(enumerate(lines_list, start=1))):
        print(i, line)


def lines_printed_random(lines_list):
    random.shuffle(lines_list)
    for line in lines_list:
        print(line)


get_file_lines(lines_list)
lines_printed_backwards(lines_list)
lines_printed_random(lines_list)
