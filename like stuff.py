import random, hangman_stages

def select_word(words):
    return random.choice(words)

def print_secret_word(secret_word):
    print(" _ " * len(secret_word))

words = ("barzal", "Lee", "Sinner", "Varlomov", "Mahomes")
remaining_attempts = 6
guessed_letters = ""

print("Welcome to SportsPlayerNameHangman!")

secret_word = select_word(words)
print(hangman_stages.get_hangman_stage(remaining_attempts))
print_secret_word(secret_word)