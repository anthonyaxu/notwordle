#!/usr/bin/python3

# Five letter words collected from Charles Reid
# https://github.com/charlesreid1/five-letter-words/blob/master/sgb-words.txt

import string
import random

# Initialise usable five letter words
# Don't actually need to put words into a dictionary
# Can just put them into a list
def get_word_list(words_file):
    words_dict = {}
    # Get words list
    f = open(words_file, "r")
    for w in f:
        # Remove new line character
        w = w.strip()
        # Sort words into dictionary based on their first letter
        if w[0] in words_dict:
            # If first letter is already a key in dictionary
            # Add it to the list
            words_dict[w[0]].append(w)
            # Sort by alphabetical order
            words_dict[w[0]].sort()
        else:
            # If first letter isn't in dictionary
            # Create new list
            words_dict[w[0]] = [w]
    f.close()
    return words_dict

def print_start_message():
    print("Welcome to Very Basic Not Wordle! You should know how this works.\
 Letters with + indicate they are an exact match, whereas letters with * mean\
 they are found within the target word. Letters with nothing indicate they are\
 not found in the target word. Enjoy and good luck!")

# Randomly select a word that the user will be trying to guess
def select_target_word(dict):
    first_letter = random.choice(string.ascii_lowercase)
    select = random.randint(0, len(dict[first_letter]) - 1)
    target_word = dict[first_letter][select]
    return target_word

# Check if the letters in guess word are also in the target word
def check_matches(word, target):
    display = []
    # Split target word into individual characters
    t = list(target)
    for c in range(0,len(word)):
        letter = word[c]
        # If letter location is an exact match with target word letter
        if letter == target[c]:
            # print("{} is an exact match!".format(letter))
            display.append("{}+".format(letter))
        
        # If letter exists in target word
        elif letter in t:
            # print("{} exists in target word".format(letter))
            display.append("{}*".format(letter))
        else:
            display.append("{} ".format(letter))
    return display

# Print out all words guessed by user, including which letters are matches
def print_guesses(list):
    print()
    for g in list:
        for i in range(0, len(g)):
            print("|{}".format(g[i]), end = "")
        print("|")
    print()
    return True

def start_game(target_word, words_dict):
    print_start_message()
    success = False
    tracker = []
    g = 0
    while g < 6:
        # Get user guess
        guess = input("Guess {}: ".format(g + 1)).lower()
        # Check if user guess is a valid word or is five letters long or starts with something not a letter
        if len(guess) != 5 or not guess[0].isalpha() or guess not in words_dict[guess[0]]:
            print("Invalid word!")

            # Print out current guesses
            if not print_guesses(tracker):
                print("Error! There was something wrong with the display")
                break
            # Let user re-try guess (doesn't use up a guess)
            continue
        # If user word is correct
        if guess == target_word:
            success = True

        # Check which letters match up
        matches = check_matches(guess, target_word)
        tracker.append(matches)
        # Print out current guesses
        if not print_guesses(tracker):
            print("Error! There was something wrong with the display")
            break
        
        # End game if word has been guessed
        if success:
            break

        # Go to next guess
        g += 1
    return success

def main():
    words_file = "words.txt"
    words_dict = get_word_list(words_file)
    target_word = select_target_word(words_dict)
    # print(target_word)
    if start_game(target_word, words_dict):
        print("Congratulations! The word was {}.".format(target_word))
    else:
        print("Uh oh you failed. Try again!")

if __name__ == "__main__":
    main()