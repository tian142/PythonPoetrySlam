sports_txt = open('sports.txt')

lines = sports_txt.readlines()
for line in lines:
    print(line)

sports_txt.close()
