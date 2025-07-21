import random, hangman_stages, sys

def select_word(words):
    return random.choice(words)

def print_secret_word(secret_word, guessed_letters):
    for letter in secret_word:
        if letter in guessed_letters:
            print(" {} ".format(letter), ends="")
        else:
            print(" _ ", ends="")
    print("/n")
    print(" _ " * len(secret_word))

def is_guess_in_secret_word(guess, secret_word):
    if len(guess) > 1 or not guess.isalpha():
        print("Only single letters are allowed. Unable to continue")
        sys.exit()
    else:
        if guess in secret_word:
            return True
        else:
            return False


words = ("barzal", "lee", "sinner", "varlomov", "mahomes")
remaining_attempts = 6
guessed_letters = ""

print("Welcome to SportsPlayerNameHangman!")
secret_word = select_word(words)
guess = input("Guess a letter: ")
guess_in_secret_word = is_guess_in_secret_word(guess, secret_word)

if guess_in_secret_word:
    if guess in guessed_letters:
        print("You have already guessed this letter. Try again: {}".format(guess))
    else:
        print("Correct! The letter {} is part of the name.".format(guess))
        guessed_letters += guess
else:
    print("Incorrect! The letter {} is not in the word.".format(guess))
    remaining_attempts -= 1
        
print(hangman_stages.get_hangman_stage(remaining_attempts))
print_secret_word(secret_word, guessed_letters)