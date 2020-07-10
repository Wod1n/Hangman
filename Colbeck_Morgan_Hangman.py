#Hangman Game
import random

def new_word():
    with open("./word_list.txt") as words:
        word_list = words.readlines()

    for i in range(len(word_list)):
        word_list[i] = word_list[i].replace("\n","")

    index = random.randrange(0, len(word_list), 1)

    word_choice = list(word_list[index])
    #Take these out
    print(word_choice)

    return word_choice

def hangman_game():
    word_choice = new_word()
    lives = 7

    partial_solution = []

    for i in range(len(word_choice)):
        partial_solution.append("*")

    while lives > 0:
        correct_letters = len(word_choice)
        print("".join(partial_solution))
        print("-----------------------------")
        guess = input("Please enter your next guess: ")
        while guess == "":
            guess = input("Please make an input: ")

        parsed_guess = guess[0].lower()

        if parsed_guess in set(word_choice):
            print("Correct!")
            for i in range(len(word_choice)):
                if parsed_guess == word_choice[i]:
                    partial_solution[i] = parsed_guess

            for i in range(len(partial_solution)):
                if partial_solution[i] == "*":
                    correct_letters -= 1

            print(correct_letters)
            if correct_letters == len(word_choice):
                print ("")
                print("-----------------------------")
                print("You Win!")
                print("The word was: {}".format("".join(word_choice)))
                return

        else:
            lives -= 1
            print("Incorrect guess")
            if lives == 1:
                print("You have 1 life remaining")
            else:
                print("You have {} lives remaining".format(lives))

        print("")

    print("-----------------------------")
    print("You Lose")
    print("The word was: {}".format("".join(word_choice)))

hangman_game()
