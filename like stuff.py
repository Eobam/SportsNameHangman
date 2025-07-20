import random

def select_word(words):
    return random.choice(words)

words = ("barzal", "Lee", "Sinner", "Varlomov", "Mahomes")

print(select_word(words))