#Hangman Game
import random

#Function to select a random word from the word list
def new_word():

    #Import word list
    with open("./word_list.txt") as words:
        word_list = words.readlines()

    #Remove carriage returns
    for i in range(len(word_list)):
        word_list[i] = word_list[i].replace("\n","")

    #Select random word from list
    index = random.randrange(0, len(word_list), 1)
    word_choice = word_list[index]

    #Toggle this line to enable/disable showing word for debugging
    #print(word_choice)

    return word_choice

#Function to receive user input
def user_guess(guessed_letters):
    print("-----------------------------")
    guess = input("Please enter your next guess: ")

    #Tests whether the guess is valid or if it has been used before
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

#Function running the actual hangman game
def hangman_game():
    #Loads new word
    word_choice = new_word()

    #Sets the number of incorrect guesses allowed
    lives = 7

    partial_solution = []
    guessed_letters = []

    #Loads the a star for each letter to be guessed
    for i in range(len(word_choice)):
        partial_solution.append("*")

    #Loops until player runs out of lives
    while lives > 0:
        correct_letters = len(word_choice)
        print("".join(partial_solution))

        #Retrieve the user's guess
        parsed_guess = user_guess(guessed_letters)

        #Add the new guess to the list of guesses
        guessed_letters.append(parsed_guess)

        #Test if the letter is in the word or not
        if parsed_guess in set(word_choice):
            print("Correct!")
            #Find guessed letter in the word
            for i in range(len(word_choice)):
                if parsed_guess == word_choice[i]:
                    #Unstar correct letters
                    partial_solution[i] = parsed_guess

            #Count the number of correct letters found
            for i in range(len(partial_solution)):
                if partial_solution[i] == "*":
                    correct_letters -= 1

            #Test whether the whole word has been guessed correctly
            if correct_letters == len(word_choice):
                print("")
                print("-----------------------------")
                print("You Win!")
                print("The word was: {}".format(word_choice))
                return

        #Deduct lives if guess is incorrect
        else:
            lives -= 1
            print("Incorrect guess")
            if lives == 1:
                print("You have 1 life remaining")
            else:
                print("You have {} lives remaining".format(lives))

        print("")

    #Final message if user runs out of lives
    print("-----------------------------")
    print("You Lose")
    print("The word was: {}".format(word_choice))
    return

hangman_game()
