
print("Some basic information about the game:")
print("1. You have to enter only one alphabet when you are asked to guess.")
print("2. If there are multiple lines of 'Yes! The alphabet you guessed was:' then that alphabet occurs that many number of times in the game")

print("\n")
print("*********************")
print("ENJOY THE GAME!!")
print("*********************")
print("\n")

import random

# Set of words where the word will be taken from
words = ['rainbow', 'computer', 'science', 'programming', 
		'python', 'mathematics', 'player', 'condition', 
		'reverse', 'water', 'board', 'geeks']

# Selecting a word from the list of words
guess_word = random.choice(words)
# print(guess_word)

# number of turns should be equal to the length of the word
turns = len(guess_word)
print("The length of the word is:",len(guess_word))

# initialization of empty sets
right_guess = set()
guess_list = set()

# Adding the alphabets in guess_list to match the right list later on
for alpha in guess_word:
    guess_list.add(alpha)
    
# main block of code for taking input from user and adding the correct input alphabets into the set of right_guess
# print the number of turns left so that the user can be aware
for i in range(turns):
    guess = input("Enter an alphabet to guess:")
    for alpha in guess_word:
        if guess in alpha:
            print("Yes! The alphabet you guessed was:", guess)
            right_guess.add(guess)
    print("\n")
    print("You have " + str(turns-1) + " turns left")
    turns = turns - 1

# printing the result
if right_guess == guess_list:
    print("Hooray!...You guessed the word!")
    print("The word you guessed is:", guess_word)
else:
    print("Don't lose hope!... Try playing the game again!")
    print("The word you guessed is:", guess_word)
    
# Note: We used set for removing the duplicates as in list we have to use other functions to remove the duplicates


