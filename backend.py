import random
from colorama import init,Back, Style


data = []
chance = [1, 2, 3, 4, 5, 6]
init()

print("Welcome to the game, Here are the rules")
print("You have to guess a 5 letter word in 6 tries.")
print("We will give you hint on each try, if that alphabet is present in word but at wrong place then that Alphabet will be shown yellow")
print("if Alphabet is present in word at right place then alphabet will be highlighted with green")
print("and if alphabet is not present in word then it will be highlighted with red, All the best!!", "\n")

File_object = open(r"dataset", "r")
for line in File_object:
    data.append(line.strip('\n'))
today_word = random.choice(data)

for i in chance:
    word = input()
    if len(word) == 5:
        if word != today_word and word in data:
            list_of_word = word.strip("")
            list_of_today = today_word.strip("")
            for j in range(5):
                if list_of_today[j] == list_of_word[j]:
                    print(Back.GREEN + list_of_word[j], end=" ")
                elif list_of_word[j] in list_of_today:
                    print(Back.YELLOW + list_of_word[j], end=" ")
                else:
                    print(Back.RED + list_of_word[j], end=" ")
            print(Style.RESET_ALL)
        elif word not in data:
            print("word not in data set!")
            chance.append(max(chance) + 1)
        elif word == today_word:
            print("found")
            print(Back.GREEN + word, end=" ")
            exit()
    else:
        if len(word) < 5:
            print("word too short, try again!!")
        else:
            print("word too big, try again!!")
        chance.append(max(chance) + 1)
    print(max(chance) - i, " chances left")
print("zesty")