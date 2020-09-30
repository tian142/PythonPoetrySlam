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


def lines_printed_custom(lines_list):
    print('------------------------Line of the day-------------------------')
    print(f'Your line of the day is: {random.choice(lines_list)}')
    ask = input(
        'Do you like your line? you get one chance to change it. (y/n) ')
    if ask == "n":
        print(f'Your line of the day is: {random.choice(lines_list)}')
    else:
        return


get_file_lines(lines_list)
lines_printed_backwards(lines_list)
lines_printed_random(lines_list)
lines_printed_custom(lines_list)

poem.close()
