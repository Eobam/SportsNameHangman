import pygame
import random
import sys

# --- Setup ---
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sports Name Hangman")
FONT = pygame.font.SysFont("arial", 36)
clock = pygame.time.Clock()

def load_img(path, size=(300, 300)):
    image = pygame.image.load(path)
    return pygame.transform.scale(image, size)


hangman_images = [
    load_img("hangmanblank.png"),
    load_img("hangmanhead.png"),
    load_img("hangmanbody.png"),
    load_img("hangmanarm1.png"),
    load_img("hangmanarm2.png"),
    load_img("hangmanleg1.png"),
    load_img("hangmanleg2.png"),
]


# --- Game Setup ---
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
secret_word = random.choice(words).lower()
guessed_letters = []
remaining_attempts = 6
current_guess = ''
game_over = False
win = False

# --- Draw Function ---
def draw_game():
    screen.fill((0, 0, 0))

    # Draw hangman image
    stage = 6 - remaining_attempts
    screen.blit(hangman_images[stage], (50, 50))

    # Word with underscores
    display_word = ' '.join([l if l in guessed_letters else '_' for l in secret_word])
    word_surface = FONT.render(display_word, True, (255, 255, 255))
    screen.blit(word_surface, (400, 200))

    # Guessed letters
    guessed_text = FONT.render("Guessed: " + ', '.join(sorted(guessed_letters)), True, (180, 180, 180))
    screen.blit(guessed_text, (400, 260))

    # Current key input
    input_surface = FONT.render("Type a letter...", True, (255, 255, 100))
    screen.blit(input_surface, (400, 320))

    # Outcome
    if game_over:
        outcome = "You WON!" if win else f"You LOST! Word was: {secret_word}"
        result_text = FONT.render(outcome, True, (0, 255, 0) if win else (255, 0, 0))
        screen.blit(result_text, (400, 400))

    pygame.display.flip()

# --- Game Loop ---
while True:
    draw_game()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if not game_over and event.type == pygame.KEYDOWN:
            key = event.unicode.lower()
            if key.isalpha() and key not in guessed_letters:
                guessed_letters.append(key)
                if key not in secret_word:
                    remaining_attempts -= 1

                if all(letter in guessed_letters for letter in secret_word):
                    game_over = True
                    win = True

                if remaining_attempts <= 0:
                    game_over = True

    clock.tick(30)