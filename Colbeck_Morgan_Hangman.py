#Hangman Game
import random

lives = 7

with open("./word_list.txt") as words:
    word_list = words.readlines()

for i in range(len(word_list)):
    word_list[i] = word_list[i].replace("\n","")

index = random.randrange(0, len(word_list), 1)

word_choice = list(word_list[index])
#Take these out
print(word_choice)
print(len(word_choice))

partial_solution = []

for i in range(len(word_choice)):
    partial_solution.append("*")

while lives > 0:
    correct_letters = len(word_choice)
    print("".join(partial_solution))
    guess = input("Please enter your next guess: ")

    if guess in set(word_choice):
        print("Correct!")
        for i in range(len(word_choice)):
            if guess == word_choice[i]:
                partial_solution[i] = guess

        for i in range(len(partial_solution)):
            if partial_solution[i] == "*":
                correct_letters -= 1

        print(correct_letters)
        if correct_letters == len(word_choice):
            print("You Win!")
            print("The word was " + "".join(word_choice))
            break

    else:
        lives -= 1
        print("Incorrect guess")
        print("You have {} lives remaining".format(lives))
