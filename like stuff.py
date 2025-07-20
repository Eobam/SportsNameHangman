import random

def select_word(words):
    return random.choice(words)

def print_secret_word(secret_word, guessed_letters):
    display = ""
    for letter in secret_word:
        if letter.lower() in guessed_letters:
            display += f"{letter} "
        else:
            display += "_ "
    print(display.strip())

words = ("barzal", "Lee", "Sinner", "Varlomov", "Mahomes")
remaining_attempts = 6
guessed_letters = ""

print("Welcome to SportsPlayerNameHangman!")

secret_word = select_word(words)
print_secret_word(secret_word, guessed_letters)
