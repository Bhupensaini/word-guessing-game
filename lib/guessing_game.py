#guessing game
from mymodule import word_list
import time as anime
import sys

word_list = word_list
word = ''
guess_count = 0
guess_limit = 5
out_of_guesses = False

print("you will have maximum 5 guesses")
print("if you guess the correct word which is available in my list you will win.")
print("now lets start guessing")
anime.sleep(0.6)

print("")

while word not in word_list:
    if guess_count < guess_limit:
        print("guess a word which is available in my list.")
        word = input('Guess a word: ')
        guess_count += 1
        print('you have usen ' + str(guess_count) + ' guess')
    else:
        out_of_guesses = True

if out_of_guesses:
    print('you are out of guesses, you lose.')
else:
    print('You win :)')
