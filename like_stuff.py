import random, sys, pygame

pygame.init()

screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sports Name Hangman")
font = pygame.font.SysFont('arial', 38)

hangman_images = [
    pygame.image.load("hangmanblank.png"),   
    pygame.image.load("hangmanhead.png"),   
    pygame.image.load("hangmanbody.png"),    
    pygame.image.load("hangmanarm1.png"),    
    pygame.image.load("hangmanarm2.png"),    
    pygame.image.load("hangmanleg1.png"),    
    pygame.image.load("hangmanleg2.png"),    

stage = 6 - remaining_attempts
screen.blit(hangman_images[stage], (100, 100))


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
guessed_letters = ""
remaining_attempts = 6
iput_letter = ''
game_over = False

def draw_game():
    screen.fill((0, 0, 0))

    
    stage = 6 - remaining_attempts
    screen.blit(hangman_images[stage], (100, 100))

    
    display_word = ' '.join([letter if letter in guessed_letters else "_" for letter in secret_word])
    text_surface = font.render(display_word, True, (255, 255, 255))
    screen.blit(text_surface, (100, 400))

    
    guessed_text = font.render("Guessed: " + ', '.join(guessed_letters), True, (200, 200, 200))
    screen.blit(guessed_text, (100, 450))

    
    input_text = font.render("Type a letter: " + input_letter, True, (255, 255, 100))
    screen.blit(input_text, (100, 500))

    pygame.display.flip()

    while not game_over:
        draw_game()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        
        elif event.type == pygame.KEYDOWN:
            if event.unicode.isalpha():
                input_letter = event.unicode.lower()
                if input_letter not in guessed_letters:
                    guessed_letters.append(input_letter)
                    if input_letter not in secret_word:
                        remaining_attempts -= 1
                input_letter = ''  
                
def print_secret_word(secret_word, guessed_letters):
    for letter in secret_word:
        if letter in guessed_letters:
            print(" {} ".format(letter), end="")
        else:
            print(" _ ", end="")
    print("\n")

def is_guess_in_secret_word(guess, secret_word):
    if len(guess) > 1 or not guess.isalpha():
        print("Only single letters are allowed.")
        return False
    return guess in secret_word

def draw_hangman(stage):
    screen.fill((0, 0, 0))
    index = 6 - stage
    if 0 <= index < len(hangman_images):
        screen.blit(hangman_images[index], (100, 100))
    pygame.display.update()

print("Welcome to SportsPlayerNameHangman!")
draw_hangman(remaining_attempts)
print_secret_word(secret_word, guessed_letters)

running = True
while running and remaining_attempts > 0:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("Already guessed:", guess)
        continue

    guessed_letters += guess

    if is_guess_in_secret_word(guess, secret_word):
        print("Correct!")
    else:
        print("Incorrect!")
        remaining_attempts -= 1

    draw_hangman(remaining_attempts)
    print_secret_word(secret_word, guessed_letters)

    
    if all(letter in guessed_letters for letter in secret_word):
        print("+++ You won! +++")
        running = False

if remaining_attempts == 0:
    print("+++ You lost... +++")
    print("The word was:", secret_word)

pygame.quit()
