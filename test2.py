sports = ["basketball", "softball", "football", "baseball", "track"]

with open('sports.txt', 'w') as sports_txt:
    sports_txt.write('\n'.join(sports))

sports_txt.close()

# ---------------to print each line in terminal---------------
