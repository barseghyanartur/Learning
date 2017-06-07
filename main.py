import random
import time

already = 0

listfile = input("What is the name of the list you want to learn? (without .txt): ")

with open(listfile + '.txt', 'r') as document:
    answer = []
    word = []
    for line in document:
        line = line.split()
        if not line:  # empty line?
            continue
        word += [line[0]]
        answer += [line[1]]

def go():
    global already
    question = random.randint(0, len(word))
    print("Learn words by guessing \n\n")
    if question == already:
        go()
    else:
        already = question
        print("The word is: " + word[question - 1])
        inp = input("Your answer is: ")
        if inp == answer[question - 1]:
            print("\n\nCongratulations")
        else:
            print("\nNo it is wrong. The good answer was " + answer[question - 1])
        time.sleep(2)
        go()

go()
