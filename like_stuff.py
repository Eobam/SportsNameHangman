import pygame
import random
import sys
import wikipediaapi

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sports Name Hangman")
FONT = pygame.font.Font("DMSans-Variable.ttf", 36)
SMALL_FONT = pygame.font.Font("DMSans-Variable.ttf", 24)
clock = pygame.time.Clock()


def load_img(path, size=(300, 300)):
    try:
        image = pygame.image.load(path)
        return pygame.transform.scale(image, size)
    except pygame.error:
        print(f"[ERROR] Couldn't load image: {path}")
        return pygame.Surface(size)

background = load_img("background1.jpg", size=(WIDTH, HEIGHT))

def load_img(path, size=(300, 300)):
    try:
        image = pygame.image.load(path)
        return pygame.transform.scale(image, size)
    except pygame.error:
        print(f"[ERROR] Couldn't load image: {path}")
        return pygame.Surface(size)  # blank placeholder if image not found

play_again_button = None
quit_button = None
wikipedia_summary = ""  # cache summary after game ends

def get_wikipedia_summary(secret_word):
    headers = {
        "User-Agent": "SportsNameHangman/1.0 (elliottlieberman123@gmail.com)"
    }
    wiki = wikipediaapi.Wikipedia(
        language="en",
        user_agent=headers["User-Agent"]
    )

    key = secret_word.strip().lower()
    full_name = full_name_lookup.get(key, key.title())

    page = wiki.page(full_name)
    if page.exists() and page.summary.strip():
        return page.summary[:400]

    # Optional fallback: Try last name only
    fallback_page = wiki.page(key.title())
    if fallback_page.exists() and fallback_page.summary.strip():
        return "[Fallback] " + fallback_page.summary[:400]

    return "No summary found on Wikipedia."

hangman_images = [
    load_img("hangmanblank.png"),
    load_img("hangmanhead.png"),
    load_img("hangmanbody.png"),
    load_img("hangmanleg1.png"),
    load_img("hangmanleg2.png"),
    load_img("hangmanarm1.png"),
    load_img("hangmanarm2.png"),
]

words = (
    "barzal", "lee", "sinner", "varlamov", "mahomes", "aho", "andersen", "andersson", "arvidsson", "atkinson",
    "bäckström", "bedard", "bennett", "benn", "bergeron", "binnington", "boeser", "bouchard", "brayden", "brodeur",
    "burns", "byram", "caldwell", "carlson", "carrick", "caufield", "chabot", "chara", "cirelli", "clutterbuck",
    "coleman", "connor", "copp", "couturier", "crosby", "dahlin", "debrincat", "demko", "draisaitl", "duchene",
    "dumba", "eichel", "ekblad", "eriksson ek", "esa", "fabri", "faksa", "fantilli", "fleury", "foligno", "fox",
    "daniels", "gallagher", "gaudreau", "georgiev", "girard", "giroux", "gostisbehere", "gourde", "graves",
    "grzelcyk", "gudas", "hall", "hamilton", "harding", "harley", "hedman", "heiskanen", "henrique", "hintz",
    "holmstrom", "horvat", "hughes", "hyman", "iafallo", "ingram", "jarry", "jarvis", "jeannot", "jenner", "jiricek",
    "johnson", "johnston", "jones", "joseph", "josi", "kadri", "kane", "karlsson", "kempe", "killorn", "Judge",
    "klingberg", "knies", "kopitar", "skenes", "kucherov", "kuznetsov", "lafrenière", "landeskog", "larkin", "lehkonen",
    "letang", "lindell", "lindholm", "lizotte", "lundell", "mackinnon", "makar", "malgin", "malkin", "mantha",
    "marchand", "marchessault", "marino", "markstrom", "marner", "martinook", "matthews", "mcavoy", "mccann",
    "mcdavid", "mcdonagh", "mctavish", "meier", "mercer", "merzlikins", "middleton", "mikheyev", "miller", "monahan",
    "mrazek", "murphy", "necas", "nedeljkovic", "nelson", "newhook", "novak", "nugent-hopkins", "nylander",
    "o'connor", "o'reilly", "oettinger", "orlov", "ovechkin", "palmieri", "panarin", "pastrnak", "pelech",
    "pettersson", "pietrangelo", "point", "provorov", "puljujarvi", "quick", "rakell", "rantanen", "raymond",
    "reichel", "reimer", "reinhart", "robertson", "rodrigues", "romanov", "roslovic", "rust", "saros", "scheifele",
    "schmidt", "seguin", "severson", "shesterkin", "sillinger", "skjei", "slavin", "smith", "soucy", "staal",
    "stamkos", "stankoven", "stolarz", "strome", "svechnikov", "swayman", "suzuki", "terry", "tavares", "tkachuk",
    "toews", "tomasino", "trocheck", "tsygankov", "tuch", "vasilevskiy", "vatrano", "verhaeghe", "vlasic", "voracek",
    "walman", "weber", "weegar", "wilson", "wood", "wotherspoon", "wright", "york", "zacha", "zegras"
)

full_name_lookup = {
    "aho": "Sebastian Aho",
    "andersen": "Frederik Andersen",
    "andersson": "Joel Andersson",
    "arvidsson": "Viktor Arvidsson",
    "atkinson": "Cam Atkinson",
    "bäckström": "Nicklas Bäckström",
    "barzal": "Mathew Barzal",
    "bedard": "Connor Bedard",
    "benn": "Jamie Benn",
    "bennett": "Sam Bennett",
    "bergeron": "Patrice Bergeron",
    "binnington": "Jordan Binnington",
    "boeser": "Brock Boeser",
    "bouchard": "Evan Bouchard",
    "brayden": "Brayden Point",
    "brodeur": "Martin Brodeur",
    "burns": "Brent Burns",
    "byram": "Bowen Byram",
    "caldwell": "Jamaree Caldwell",
    "carlson": "John Carlson",
    "carrick": "Sam Carrick",
    "caufield": "Cole Caufield",
    "chabot": "Thomas Chabot",
    "chara": "Zdeno Chára",
    "cirelli": "Anthony Cirelli",
    "clutterbuck": "Cal Clutterbuck",
    "coleman": "Blake Coleman",
    "connor": "Kyle Connor",
    "copp": "Andrew Copp",
    "couturier": "Sean Couturier",
    "crosby": "Sidney Crosby",
    "dahlin": "Rasmus Dahlin",
    "debrincat": "Alex DeBrincat",
    "demko": "Thatcher Demko",
    "draisaitl": "Leon Draisaitl",
    "duchene": "Matt Duchene",
    "dumba": "Matt Dumba",
    "eichel": "Jack Eichel",
    "ekblad": "Aaron Ekblad",
    "eriksson ek": "Filip Eriksson Ek",
    "esa": "Esa Lindell",
    "fabri": "Tomas Fabri",
    "faksa": "Radek Faksa",
    "fantilli": "Michael Fantilli",
    "fleury": "Marc-André Fleury",
    "foligno": "Marcus Foligno",
    "fox": "Adam Fox",
    "daniels": "Jayden Daniels",
    "gallagher": "Brendan Gallagher",
    "gaudreau": "Johnny Gaudreau",
    "georgiev": "Alexender Georgiev",
    "girard": "Sam Girard",
    "giroux": "Claude Giroux",
    "gostisbehere": "Shayne Gostisbehere",
    "gourde": "Yanni Gourde",
    "graves": "Ryan Graves",
    "grzelcyk": "Matt Grzelcyk",
    "gudas": "Radko Gudas",
    "hall": "Taylor Hall",
    "hamilton": "Dougie Hamilton",
    "harding": "Zachary Harding",
    "harley": "Thomas Harley",
    "hedman": "Victor Hedman",
    "heiskanen": "Miro Heiskanen",
    "henrique": "Adam Henrique",
    "hintz": "Roope Hintz",
    "holmstrom": "Simon Holmstrom",
    "horvat": "Bo Horvat",
    "hughes": "Quinn Hughes",
    "hyman": "Zach Hyman",
    "iafallo": "Alex Iafalllo",
    "ingram": "Brandon Ingram",
    "jarry": "Tristan Jarry",
    "jarvis": "Bryce Jarvis",
    "jeannot": "Tanner Jeannot",
    "jenner": "Boone Jenner",
    "jiricek": "Adam Jiříček",
    "johnson": "Antonio Johnson (defensive back)",
    "johnston": "Alistair Johnston",
    "jones": "Dillon Jones",
    "joseph": "Greg Joseph",
    "josi": "Roman Josi",
    "kadri": "Nazem Kadri",
    "kane": "Patrick Kane",
    "karlsson": "Erik Karlsson",
    "kempe": "Marcus Kempe",
    "killorn": "Alex Killorn",
    "Judge": "Aaron Judge",
    "klingberg": "John Klingberg",
    "knies": "Matthew Knies",
    "kopitar": "Anze Kopitar",
    "skenes": "Paul Skenes",
    "kucherov": "Nikita Kucherov",
    "kuznetsov": "Evgeny Kuznetsov",
    "lafrenière": "Alexis Lafrenière",
    "landeskog": "Gabriel Landeskog",
    "larkin": "Dylan Larkin",
    "lee": "Anders Lee",
    "lehkonen": "Joel Lehkonen",
    "letang": "Kris Letang",
    "lindell": "Joel Lindell",
    "lindholm": "Elias Lindholm",
    "lizotte": "Kevin Lizotte",
    "lundell": "Adam Lundell",
    "mackinnon": "Nathan MacKinnon",
    "makar": "Cale Makar",
    "malgin": "Denis Malgin",
    "malkin": "Evgeni Malkin",
    "mantha": "Anthony Mantha",
    "marchand": "Brad Marchand",
    "marchessault": "Jonathan Marchessault",
    "marino": "Joe Marino",
    "markstrom": "Jacob Markström",
    "marner": "Mitch Marner",
    "martinook": "Jordan Martinook",
    "matthews": "Auston Matthews",
    "mcavoy": "Charlie McAvoy",
    "mccann": "Tyler McCann",
    "mcdavid": "Connor McDavid",
    "mcdonagh": "Ryan McDonagh",
    "mctavish": "Connor McTavish",
    "meier": "Tobias Meier",
    "mercer": "Trevor Mercer",
    "merzlikins": "Elvis Merzlikins",
    "middleton": "Nick Middleton",
    "mikheyev": "Alexander Mikheyev",
    "miller": "Ryan Miller",
    "monahan": "Sean Monahan",
    "mrazek": "Petr Mrazek",
    "murphy": "Greg Murphy",
    "necas": "Martin Necas",
    "nedeljkovic": "Ivan Nedeljkovic",
    "nelson": "Matthew Nelson",
    "newhook": "Jesper Newhook",
    "novak": "David Novak",
    "nugent-hopkins": "Ryan Nugent-Hopkins",
    "nylander": "William Nylander",
    "o'connor": "Ryan O'Connor",
    "o'reilly": "Ryan O'Reilly",
    "oettinger": "Dustin Oettinger",
    "orlov": "Dmitry Orlov",
    "ovechkin": "Alex Ovechkin",
    "palmieri": "Kyle Palmieri",
    "panarin": "Artemi Panarin",
    "pastrnak": "David Pastrnak",
    "pelech": "Ryan Pelech",
    "pettersson": "Elias Pettersson",
    "pietrangelo": "Alex Pietrangelo",
    "point": "Brayden Point",
    "provorov": "Ivan Provorov",
    "puljujarvi": "Jesse Puljujarvi",
    "quick": "Jonathan Quick",
    "rakell": "Rickard Rakell",
    "rantanen": "Mikko Rantanen",
    "raymond": "Brandon Raymond",
    "reichel": "Connor Reichel",
    "reimer": "Joey Reimer",
    "reinhart": "Sam Reinhart",
    "robertson": "Jason Robertson",
    "rodrigues": "Andre Rodrigues",
    "romanov": "Daniil Romanov",
    "roslovic": "Brandon Roslovic",
    "rust": "Bryan Rust",
    "saros": "Juuse Saros",
    "scheifele": "Mark Scheifele",
    "schmidt": "Nate Schmidt",
    "seguin": "Tyler Seguin",
    "severson": "Will Severson",
    "shesterkin": "Igor Shesterkin",
    "sillinger": "Luke Sillinger",
    "skjei": "Brady Skjei",
    "slavin": "Jaccob Slavin",
    "smith": "Craig Smith",
    "soucy": "Philippe Soucy",
    "staal": "Eric Staal",
    "stamkos": "Steven Stamkos",
    "stankoven": "Cole Stankoven",
    "stolarz": "Anthony Stolarz",
    "strome": "Brandon Strome",
    "svechnikov": "Andrei Svechnikov",
    "swayman": "Jared Swayman",
    "suzuki": "Nick Suzuki",
    "terry": "Chris Terry",
    "tavares": "John Tavares",
    "tkachuk": "Brady Tkachuk",
    "toews": "Jonathan Toews",
    "tomasino": "Riley Tomasino",
    "trocheck": "Vincent Trocheck",
    "tsygankov": "Vladislav Tsygankov",
    "tuch": "Alex Tuch",
    "vasilevskiy": "Andrei Vasilevskiy",
    "vatrano": "Frank Vatrano",
    "verhaeghe": "Cal Verhaeghe",
    "vlasic": "Marc-Édouard Vlasic",
    "voracek": "Jakub Voracek",
    "walman": "Adam Walman",
    "weber": "Shea Weber",
    "weegar": "Cal Weegar",
    "wilson": "Nathan Wilson",
    "wood": "Joe Wood",
    "wotherspoon": "Brandon Wotherspoon",
    "wright": "J.T. Wright",
    "york": "Calvin York",
    "zacha": "Pavel Zacha",
    "zegras": "Trevor Zegras"
}

def reset_game():
    global secret_word, guessed_letters, remaining_attempts, game_over, win, wikipedia_summary
    secret_word = random.choice(words).lower()
    guessed_letters = set()
    remaining_attempts = 6
    game_over = False
    win = False
    wikipedia_summary = ""

reset_game()

def draw_button(text, x, y, width, height, color, text_color):
    pygame.draw.rect(screen, color, (x, y, width, height), border_radius=10)
    label = SMALL_FONT.render(text, True, text_color)
    label_rect = label.get_rect(center=(x + width // 2, y + height // 2))
    screen.blit(label, label_rect)
    return pygame.Rect(x, y, width, height)


def draw_game():
    screen.blit(background, (0, 0))

    stage = 6 - remaining_attempts
    screen.blit(hangman_images[stage], (50, 50))

    display_word = ' '.join([l if l in guessed_letters else '_' for l in secret_word])
    word_surface = FONT.render(display_word, True, (255, 255, 255))
    screen.blit(word_surface, (400, 200))

    guessed_text = FONT.render("Guessed: " + ', '.join(sorted(guessed_letters)), True, (180, 180, 180))
    screen.blit(guessed_text, (400, 260))

    input_surface = FONT.render("Type a letter...", True, (255, 255, 100))
    screen.blit(input_surface, (400, 320))

    if game_over:
        global play_again_button, quit_button, wikipedia_summary
        outcome = "You WON!" if win else f"You LOST! Word was: {secret_word}"
        result_text = FONT.render(outcome, True, (0, 255, 0) if win else (255, 0, 0))
        text_rect = result_text.get_rect(center=(WIDTH // 2, 400))
        screen.blit(result_text, text_rect)

        if not wikipedia_summary:
            wikipedia_summary = get_wikipedia_summary(secret_word)

        summary = wikipedia_summary
        summary_lines = []
        max_line_length = 60
        while len(summary) > 0:
            split_at = summary.rfind(' ', 0, max_line_length)
            if split_at == -1:
                split_at = max_line_length
            summary_lines.append(summary[:split_at])
            summary = summary[split_at+1:]

        for i, line in enumerate(summary_lines[:5]):
            summary_text = pygame.font.SysFont(None, 24).render(line, True, (200, 200, 200))
            screen.blit(summary_text, (WIDTH // 2 - 350, 440 + i * 25))

        play_again_button = draw_button("Play Again", WIDTH // 2 - 150, 550, 140, 50, (0, 200, 0), (255, 255, 255))
        quit_button = draw_button("Quit", WIDTH // 2 + 10, 550, 140, 50, (200, 0, 0), (255, 255, 255))

    pygame.display.flip()

# Game loop
while True:
    draw_game()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and game_over:
            mouse_pos = pygame.mouse.get_pos()
            if play_again_button and play_again_button.collidepoint(mouse_pos):
                reset_game()
            elif quit_button and quit_button.collidepoint(mouse_pos):
                pygame.quit()
                sys.exit()

        if not game_over and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            key = event.unicode.lower()
            if key.isalpha() and key not in guessed_letters:
                guessed_letters.add(key)
                if key not in secret_word:
                    remaining_attempts -= 1
                if all(letter in guessed_letters for letter in secret_word):
                    game_over = True
                    win = True
                if remaining_attempts == 0:
                    game_over = True
                    win = False

    clock.tick(30)

