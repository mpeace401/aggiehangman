#By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do"
# "I have not given or received any unauthorized aid on this assignment"
#
# Name:  Marissa Peace
# UIN: 930004136
# Section: 510
# Assignment: PythonProject
# Date: 11 17 2020
from random import *
#Hangman, a game where you try to guess the word before the drawing is done
#This hangman is A&M themed, all words relate to Texas A&M
wordlist = ['aggies','gig em', 'howdy', 'war hymn', 'kyle field', 'whoop', 'wildcat', 'aggie ring', 'fish camp',
            'midnight yell', 'senior boots', 'college station', 'reveille', 'maroon', 'bonfire', 'silver taps',
            'horns down', 'aggieland', 'corps', 'farmers', 'horse laugh', 'hullabaloo', 'jimbo', 'muster',
            'old army', 'ring dance', 'reed arena', 'twelfth man', 'aggie spirit', 'yell leader', 'aggie band',
            'college station','century tree', 'elephant walk', 'hump it', 'pass backs', 'zachry', 'sbisa', 'sully',
            'rudder tower'] #List of aggie words

def change(turns):
    '''This function is responsible for changing the image each turn. The turn variable goes up everytime
    the user fails to guess a word or letter. For each incorrect guess, a new detail is added to the picture.
    After 8 guess, the man is hung and the game is lost.'''
    if turns[0] == 1:
        pic[1][2] = '¿'
    elif turns[0] == 2:
        pic[2][2] = 'O'
    elif turns[0] == 3:
        pic[3][2] = '|'
    elif turns[0] == 4:
        pic[4][2] = '|'
    elif turns[0] == 5:
        pic[3][1] = '\\'
    elif turns[0] == 6:
        pic[3][3] = '/'
    elif turns[0] == 7:
        pic[5][1] = '/'
    elif turns[0] == 8:
        pic[5][3] = '\\'
def evaluate():
    '''This function checks to see if the user has guessed the word correctly. This checks if a) all the letters have
    been guessed correctly or b) if the word was guessed correctly. Depending on the result of this test, it returns
    a win statement, a lose statement, or ask the user if they want to continue.'''
    if complete[0] == length:
        print("You guessed it! The word was {}".format(word))
        if times[0] > 1:
            print("It took you", times[0], 'guesses!')
        else:
            print("It took you", times[0], 'guess!')
        return 'N'
    elif turns[0] == 8:
        graphic()
        print('You lost! The word was {}'.format(word))
        return 'N'
    else:
        return str(input("Would you like to continue playing? (Y/N): "))
def present():
    '''This function displays the blank lines that correspond to each letter in the word. If the user guessed the
    correct letter, it print that letter instead of a blank. The spaces between blanks were added to help with
    readability.'''
    for i in word:
        if i in letters:
            print('_', end =' ')
        elif i == ' ':
            print(' ', end = ' ')
        else:
            print(i, end = ' ')
    print()
def letter(guess):
    '''This function evaluates the letter that the user guesses. It deletes guessed letters from the letter list to
    ensure they can't be called again. If the letter is in the word, It increases a variable that can be compared against
    the length of the word. It then outputs how many of each letter were found, or that the letter is not in the word.
    This functions also checks for invalid inputs such as ?!@* and for letters already guessed.'''
    counter = 0
    if guess in exclude:
        print("The input was invalid. Only lowercase letters are accepted.")
    elif guess not in letters:
        print("You have already guessed this letter!")
    elif guess not in word:
        letters[letters.index(guess)] = 0
        print("This letter is not in the word!")
        turns[0] = turns[0] + 1
        times[0] = times[0] + 1
        change(turns)
    elif guess in word:
        letters[letters.index(guess)] = 0
        times[0] = times[0] + 1
        for i in word:
            if i == guess:
                counter += 1
                complete[0] = complete[0] + 1
        if counter == 1:
            print("There is {} {} in the word".format(counter, guess))
        else:
            print("There are {} {}'s in the word".format(counter, guess))
def wordguess(guess):
    '''This function checks if a guessed word is the actual word. If not, it outputs that it is not the word. If it is
    the word, it changes the variable to be the length of the word, letting the system know that the word has been
    guessed.'''
    if guess == word:
        complete[0] = len(word)
        times[0] = times[0] + 1
    else:
        turns[0] = turns[0] + 1
        times[0] = times[0] + 1
        change(turns)
        print("That was not the word!")
def graphic():
    '''This function draws the graphic. It prints each part of the list, forming a picture.'''
    for i in range(len(pic)):
        for j in range(8):
            print(pic[i][j], end='')

#Main code. This code runs the game and calls the functions.
play = 'y'
while play == 'y' or play == 'Y' or play == 'r' or play == 'R': #This allows the game to restart, or be fully quit.
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    exclude = ['!', '?', ',', '.', '-', '_', '/', '@', '*', '&', '$', "'", '1', '2', '3', '4', '5', '6', '7', '8', '9',
               '0']
    word = wordlist[randint(0, len(wordlist) - 1)]
    pic = [[' ', ' ', 'Ⲅ', '=', '=', '\\', ' ', '\n'],
           [' ', ' ', ' ', ' ', ' ', '|', ' ', '\n'],
           [' ', ' ', ' ', ' ', ' ', '|', ' ', '\n'],
           [' ', ' ', ' ', ' ', ' ', '|', ' ', '\n'],
           [' ', ' ', ' ', ' ', ' ', '|', ' ', '\n'],
           [' ', ' ', ' ', ' ', ' ', '|', ' ', '\n'],
           [' ', ' ', ' ', '_', '_', 'L', '_', '\n']]
    length = len(word)
    complete = [0]
    turns = [0]
    times = [0]
    #Instructions
    print("Howdy! Welcome to Aggie Hangman! This is hangman featuring aggie-themed words.")
    print("You will be given a random word represented as blank lines. You can choose to guess a letter, or guess the word.")
    print("The game ends if you take too many turns to guess the word, or if you guess the word correctly")
    print("All words in this game will be in lowercase letters, and there will be no special symbols, only lowercase letters.")
    print("There are both regular words, and phrases. They range in difficulty, with some being easy and others being hard.\n")
    play = str(input("Would you like to play Aggie Hangman? (y/n): "))
    choice = play
    print()
    option = ''
    while choice == 'Y' or choice == 'y': #This runs the game so long as the play chooses to  continue.
        graphic()
        present()
        print()
        option = str(input("Would you like to guess a letter, or guess a word? (letter/word): "))
        if option == 'Letter' or option == 'letter': #checks what the user wants to enter
            guess = str(input("Enter a letter (lowercase): "))
            letter(guess)
        elif option == 'word' or option == 'Word': #checks what the user wants to enter
            guess = str(input("Enter a word/phrase (all lowercase): "))
            wordguess(guess)
        else: #checks what the user wants to enter is not an option
            print("The input was invalid, please try again.")
        print()
        choice = evaluate()
    #once the player decides to stop playing or wins the game, this question asks if they want to reset, or quit the game.
    play = str(input("Would you like to reset, or quit Aggie Hangman? (r/q): "))
    print()