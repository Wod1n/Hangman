#Hangman Game
import random

def new_word():

    #import word list
    with open("./word_list.txt") as words:
        word_list = words.readlines()

    #remove carriage returns
    for i in range(len(word_list)):
        word_list[i] = word_list[i].replace("\n","")

    #select random word from list
    index = random.randrange(0, len(word_list), 1)
    word_choice = word_list[index]
    print(word_choice)

    return word_choice

def user_guess(guessed_letters):
    print("-----------------------------")
    guess = input("Please enter your next guess: ")
    while True:
        if guess != "" and guess.lower().islower():
            for i in range(len(guess)):
                if guess[i].islower():
                    if guess[i] in set(guessed_letters):
                        print("You have already guessed that letter!")
                        guess = input("Please enter your next guess: ")
                        break
                    print(guess[i])
                    return guess[i]
            continue

        print("Invalid input")
        guess = input("Please enter your next guess: ")



def hangman_game():
    word_choice = new_word()
    lives = 7

    partial_solution = []
    guessed_letters = []

    for i in range(len(word_choice)):
        partial_solution.append("*")

    while lives > 0:
        correct_letters = len(word_choice)
        print("".join(partial_solution))
        parsed_guess = user_guess(guessed_letters)

        guessed_letters.append(parsed_guess)
        if parsed_guess in set(word_choice):
            print("Correct!")
            for i in range(len(word_choice)):
                if parsed_guess == word_choice[i]:
                    partial_solution[i] = parsed_guess

            for i in range(len(partial_solution)):
                if partial_solution[i] == "*":
                    correct_letters -= 1

            if correct_letters == len(word_choice):
                print("")
                print("-----------------------------")
                print("You Win!")
                print("The word was: {}".format(word_choice))
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
    print("The word was: {}".format(word_choice))

hangman_game()
