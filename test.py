new_fruits = []

fruits = ['Banana', 'Apple', 'eear', 'Peach',
          'oherry', 'Avocados', 'Elderberry']

number = int(input("Input a number of fruits: "))


def fruit_count(fruits, number):
    vowls = ['A', 'E', 'I', 'O', 'U']
    for fruit in fruits:
        if fruit[0].upper() not in vowls:
            new_fruits.append(fruit)
    print(new_fruits[:number])


fruit_count(fruits, number)
# 1. ask for input of list of fruit and number
# 2. return the number of fruits that start without vowl
# Jackie was here
