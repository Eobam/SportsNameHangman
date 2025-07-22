import random, hangman_stages, sys, Listofplayers
import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sports Name Hangman")


hangman_stage_images = [
    pygame.image.load("hangmanarm1.png"),
    pygame.image.load("hangmanarm2.png"),
    pygame.image.load("hangmanblank.png"),
    pygame.image.load("hangman3bodypng"),
    pygame.image.load("hangmanhead.png"),
    pygame.image.load("hangmanleg1.png"),
    pygame.image.load("hangmanleg2.png"),]

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

words = ("barzal", "lee", "sinner", "varlomov", "mahomes", "Aho", "Andersen", "Andersson", "Arvidsson", "Atkinson",
    "Bäckström", "Barzal", "Bedard", "Bennett", "Benn", "Bergeron", "Binnington",
    "Boeser", "Bouchard", "Brayden", "Brodeur", "Burns", "Byram", "Caldwell",
    "Carlson", "Carrick", "Caufield", "Chabot", "Chara", "Cirelli", "Clutterbuck",
    "Coleman", "Connor", "Copp", "Couturier", "Crosby", "Dahlin", "DeBrincat",
    "Demko", "Draisaitl", "Duchene", "Dumba", "Eichel", "Ekblad", "Eriksson Ek",
    "Esa", "Fabri", "Faksa", "Fantilli", "Fleury", "Foligno", "Fox", "Frederic",
    "Gallagher", "Gaudreau", "Georgiev", "Girard", "Giroux", "Gostisbehere",
    "Gourde", "Graves", "Grzelcyk", "Gudas", "Hall", "Hamilton",
    "Harding", "Harley", "Hedman", "Heiskanen", "Henrique", "Hintz", "Holmstrom",
    "Horvat", "Hughes", "Hyman", "Iafallo", "Ingram", "Jarry", "Jarvis",
    "Jeannot", "Jenner", "Jiricek", "Johnson", "Johnston", "Jones", "Joseph",
    "Josi", "Kadri", "Kane", "Karlsson", "Kempe", "Killorn", "Kiviranta",
    "Klingberg", "Knies", "Kopitar", "Krejci", "Kucherov", "Kuznetsov", "Lafrenière",
    "Landeskog", "Larkin", "Lee", "Lehkonen", "Letang", "Lindell", "Lindholm",
    "Lizotte", "Lundell", "Mackinnon", "Makar", "Malgin", "Malkin", "Mantha",
    "Marchand", "Marchessault", "Marino", "Markstrom", "Marner", "Martinook",
    "Matthews", "McAvoy", "McCann", "McDavid", "McDonagh", "McTavish", "Meier",
    "Mercer", "Merzlikins", "Middleton", "Mikheyev", "Miller", "Monahan",
    "Mrazek", "Murphy", "Necas", "Nedeljkovic", "Nelson", "Newhook", "Novak",
    "Nugent-Hopkins", "Nylander", "O'Connor", "O'Reilly", "Oettinger", "Orlov",
    "Ovechkin", "Palmieri", "Panarin", "Pastrnak", "Pelech", "Pettersson",
    "Pietrangelo", "Point", "Provorov", "Puljujarvi", "Quick", "Rakell",
    "Rantanen", "Raymond", "Reichel", "Reimer", "Reinhart", "Robertson",
    "Rodrigues", "Romanov", "Roslovic", "Rust", "Saros", "Scheifele", "Schmidt",
    "Seguin", "Severson", "Shesterkin", "Sillinger", "Skjei", "Slavin", "Smith",
    "Soucy", "Staal", "Stamkos", "Stankoven", "Stolarz", "Strome", "Svechnikov",
    "Swayman", "Suzuki", "Terry", "Tavares", "Tkachuk", "Toews", "Tomasino",
    "Trocheck", "Tsygankov", "Tuch", "Vasilevskiy", "Vatrano", "Verhaeghe",
    "Vlasic", "Voracek", "Walman", "Weber", "Weegar", "Wilson", "Wood",
    "Wotherspoon", "Wright", "York", "Zacha", "Zegras")
remaining_attempts = 6
guessed_letters = ""

print("Welcome to SportsPlayerNameHangman!")
secret_word = select_word(words)

def draw_hangman(remaining_attempts):
    screen.blit(hangman_stage_images[6 - remaining_attempts], (100, 100))

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