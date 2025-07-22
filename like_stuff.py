import random, hangman_stages, sys
import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sports Name Hangman")

def select_word(words):
    return random.choice(words)

def print_secret_word(secret_word, guessed_letters):
    for letter in secret_word:
        if letter in guessed_letters:
            print(" {} ".format(letter), end="")
        else:
            print(" _ ", end="")
    print("\n")
    print(" _ " * len(secret_word))

def is_guess_in_secret_word(guess, secret_word):
    if len(guess) > 1 or not guess.isalpha():
        print("Only single letters are allowed. Unable to continue.")
        sys.exit()
    return guess in secret_word

def get_unique_letters(word):
    return "".join(set(word))

words = ("barzal", "lee", "sinner", "varlomov", "mahomes")
remaining_attempts = 6
guessed_letters = ""

print("Welcome to SportsPlayerNameHangman!")
secret_word = select_word(words)

while remaining_attempts > 0 and len(set(guessed_letters) & set(secret_word)) < len(set(secret_word)):
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You have already guessed this letter. Try again: {}".format(guess))
        continue

    if is_guess_in_secret_word(guess, secret_word):
        print("Correct! The letter {} is part of the name.".format(guess))
    else:
        print("Incorrect! The letter {} is not in the word.".format(guess))
        remaining_attempts -= 1

    guessed_letters += guess

    print(hangman_stages.get_hangman_stage(remaining_attempts))
    print("\n{} attempts remaining\n".format(remaining_attempts))
    print_secret_word(secret_word, guessed_letters)
    print("\nLetters guessed so far: {}\n".format(guessed_letters))

if len(guessed_letters) == len(get_unique_letters(secret_word)):
    print("+++ You won! +++\n")
else:
    print("+++ You lost... +++\n")