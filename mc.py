from colorama import init, Fore, Style
import time, os, random, threading, getpass, random, string, sys
from playsound import playsound
from subprocess import call

init()

def typewriter(string, end='\n', rate=5):
    for char in string:
        print(char, end='', flush=True)
        time.sleep(random.random() / rate)
    print(end, end='', flush=True)

def typewriterC(string, end='\n', rate=6):
    for char in string:
        print(char, end='', flush=True)
        time.sleep(random.random() / rate)
    print(end, end='', flush=True)

def blue(text: str):
    typewriter(Fore.BLUE + text + Style.RESET_ALL + "\n")
    time.sleep(0.25)
def green(text: str):
    typewriter(Fore.GREEN + text + Style.RESET_ALL + "\n")
    time.sleep(0.25)

def white(text: str):
    typewriterC(Fore.WHITE + text + Style.RESET_ALL)
def grey(text: str):
    typewriterC(Fore.LIGHTBLACK_EX + text + Style.RESET_ALL)
def yellow(text: str):
    typewriterC(Fore.LIGHTYELLOW_EX + text + Style.RESET_ALL)

def check():
    call("clear" if os.name == "posix" else "cls")

def scramblerBLUE():
    amt = random.randint(5, 12)
    ran = "".join(random.choices(string.ascii_uppercase + string.digits, k=amt))
    release = Fore.LIGHTYELLOW_EX + ran + Fore.BLUE
    return str(release)

def scramblerGREEN():
    amt = random.randint(5, 12)
    ran = "".join(random.choices(string.ascii_uppercase + string.digits, k=amt))
    release = Fore.LIGHTYELLOW_EX + ran + Fore.GREEN
    return str(release)  

def audio():
    playsound("audio.mp3")

def text():
    playername = getpass.getuser()

    blue("I see the player you mean.")
    green(playername + "?")
    blue("Yes. Take care. It has reached a higher level now. It can read our thoughts.")
    green("That doesn't matter. It thinks we are part of the game.")
    blue("I like this player. It played well. It did not give up.")
    green("It is reading our thoughts as though they were words on a screen.")
    blue("That is how it chooses to imagine many things, when it is deep in the dream of a game.")
    green("Words make a wonderful interface. Very flexible. And less terrifying than staring at the reality behind the screen.")
    blue("They used to hear voices. Before players could read. Back in the days when those who did not play called the players witches, and warlocks. And players dreamed they flew through the air, on sticks powered by demons.")
    green("What did this player dream?")
    blue("This player dreamed of sunlight and trees. Of fire and water. It dreamed it created. And it dreamed it destroyed. It dreamed it hunted, and was hunted. It dreamed of shelter.")
    green("Hah, the original interface. A million years old, and it still works. But what true structure did this player create, in the reality behind the screen?")
    blue("It worked, with a million others, to sculpt a true world in a fold of the " + scramblerBLUE() + ", and created a " + scramblerBLUE() + " for " + scramblerBLUE() + ", in the " + scramblerBLUE() + ".")
    green("It cannot read that thought.")
    blue("No. It has not yet achieved the highest level. That, it must achieve in the long dream of life, not the short dream of a game.")
    green("Does it know that we love it? That the universe is kind?")
    blue("Sometimes, through the noise of its thoughts, it hears the universe, yes.")
    green("But there are times it is sad, in the long dream. It creates worlds that have no summer, and it shivers under a black sun, and it takes its sad creation for reality.")
    blue("To cure it of sorrow would destroy it. The sorrow is part of its own private task. We cannot interfere.")
    green("Sometimes when they are deep in dreams, I want to tell them, they are building true worlds in reality. Sometimes I want to tell them of their importance to the universe. Sometimes, when they have not made a true connection in a while, I want to help them to speak the word they fear.")
    blue("It reads our thoughts.")
    green("Sometimes I do not care. Sometimes I wish to tell them, this world you take for truth is merely " + scramblerGREEN() + " and " + scramblerGREEN() + ", I wish to tell them that they are " + scramblerGREEN() + " in the " + scramblerGREEN() + ". They see so little of reality, in their long dream.")
    blue("And yet they play the game.")
    green("But it would be so easy to tell them...")
    blue("Too strong for this dream. To tell them how to live is to prevent them living.")
    green("I will not tell the player how to live.")
    blue("The player is growing restless.")
    green("I will tell the player a story.")
    blue("But not the truth.")
    green("No. A story that contains the truth safely, in a cage of words. Not the naked truth that can burn over any distance.")
    blue("Give it a body, again.")
    green("Yes. Player...")
    blue("Use its name.")
    green(playername + ". Player of games.")
    blue("Good.")
    green("Take a breath, now. Take another. Feel air in your lungs. Let your limbs return. Yes, move your fingers. Have a body again, under gravity, in air. Respawn in the long dream. There you are. Your body touching the universe again at every point, as though you were separate things. As though we were separate things.")
    blue("Who are we? Once we were called the spirit of the mountain. Father sun, mother moon. Ancestral spirits, animal spirits. Jinn. Ghosts. The green man. Then gods, demons. Angels. Poltergeists. Aliens, extraterrestrials. Leptons, quarks. The words change. We do not change.")
    green("We are the universe. We are everything you think isn't you. You are looking at us now, through your skin and your eyes. And why does the universe touch your skin, and throw light on you? To see you, player. To know you. And to be known. I shall tell you a story.\n\nOnce upon a time, there was a player.")
    blue("The player was you, " + playername + ".")
    green("Sometimes it thought itself human, on the thin crust of a spinning globe of molten rock. The ball of molten rock circled a ball of blazing gas that was three hundred and thirty thousand times more massive than it. They were so far apart that light took eight minutes to cross the gap. The light was information from a star, and it could burn your skin from a hundred and fifty million kilometres away.\n\nSometimes the player dreamed it was a miner, on the surface of a world that was flat, and infinite. The sun was a square of white. The days were short; there was much to do; and death was a temporary inconvenience.")
    blue("Sometimes the player dreamed it was lost in a story.")
    green("Sometimes the player dreamed it was other things, in other places. Sometimes these dreams were disturbing. Sometimes very beautiful indeed. Sometimes the player woke from one dream into another, then woke from that into a third.")
    blue("Sometimes the player dreamed it watched words on a screen.")
    green("Let's go back.\n\nThe atoms of the player were scattered in the grass, in the rivers, in the air, in the ground. A woman gathered the atoms; she drank and ate and inhaled; and the woman assembled the player, in her body.\n\nAnd the player awoke, from the warm, dark world of its mother's body, into the long dream.\n\nAnd the player was a new story, never told before, written in letters of DNA. And the player was a new program, never run before, generated by a sourcecode a billion years old. And the player was a new human, never alive before, made from nothing but milk and love.")
    blue("You are the player. The story. The program. The human. Made from nothing but milk and love.")
    green("Let's go further back.\n\nThe seven billion billion billion atoms of the player's body were created, long before this game, in the heart of a star. So the player, too, is information from a star. And the player moves through a story, which is a forest of information planted by a man called Julian, on a flat, infinite world created by a man called Markus, that exists inside a small, private world created by the player, who inhabits a universe created by...")
    blue('Shush. Sometimes the player created a small, private world that was soft and warm and simple. Sometimes hard, and cold, and complicated. Sometimes it built a model of the universe in its head; flecks of energy, moving through vast empty spaces. Sometimes it called those flecks "electrons" and "protons".')
    green('Sometimes it called them "planets" and "stars".\n\nSometimes it believed it was in a universe that was made of energy that was made of offs and ons; zeros and ones; lines of code. Sometimes it believed it was playing a game. Sometimes it believed it was reading words on a screen.')
    blue("You are the player, reading words...")
    green("Shush... Sometimes the player read lines of code on a screen. Decoded them into words; decoded words into meaning; decoded meaning into feelings, emotions, theories, ideas, and the player started to breathe faster and deeper and realised it was alive, it was alive, those thousand deaths had not been real, the player was alive")
    blue("You. You. You are alive.")
    green("and sometimes the player believed the universe had spoken to it through the sunlight that came through the shuffling leaves of the summer trees")
    blue("and sometimes the player believed the universe had spoken to it through the light that fell from the crisp night sky of winter, where a fleck of light in the corner of the player's eye might be a star a million times as massive as the sun, boiling its planets to plasma in order to be visible for a moment to the player, walking home at the far side of the universe, suddenly smelling food, almost at the familiar door, about to dream again")
    green("and sometimes the player believed the universe had spoken to it through the zeros and ones, through the electricity of the world, through the scrolling words on a screen at the end of a dream")
    blue("and the universe said I love you")
    green("and the universe said you have played the game well")
    blue("and the universe said everything you need is within you")
    green("and the universe said you are stronger than you know")
    blue("and the universe said you are the daylight")
    green("and the universe said you are the night")
    blue("and the universe said the darkness you fight is within you")
    green("and the universe said the light you seek is within you")
    blue("and the universe said you are not alone")
    green("and the universe said you are not separate from every other thing")
    blue("and the universe said you are the universe tasting itself, talking to itself, reading its own code")
    green("and the universe said I love you because you are love.")
    blue("And the game was over and the player woke up from the dream. And the player began a new dream. And the player dreamed again, dreamed better. And the player was the universe. And the player was love.\n\nYou are the player.")
    green("Wake up.")

    print("\n")
    time.sleep(5)
    print("\n")
    time.sleep(2)
    
    credits()

def credits():
    white("===============")
    yellow("Minecraft Credits (1.6)")
    white("===============\n")
    grey("Created by:")
    white("         Markus Persson\n")
    grey("Game design, programming and graphics:")
    white("         Markus Persson\n         Jens Bergensten\n         Nathan Adams\n")
    grey("Programming:")
    white("         Erik Broes\n")
    grey("Music and sound:")
    white("         Daniel Rosenfeld\n")
    grey("Ingame artwork and paintings:")
    white("         Kristoffer Zetterstrand\n")
    grey("End game narrative:")
    white("         Julian Gough\n")
    grey("Website development:")
    white("         Tobias Möllstam\n         Daniel Frisk\n         Leonard Axelsson\n         Jens Bergensten\n         Markus Persson\n")
    grey("Logo and promotional artwork:")
    white("         Markus Toivonen\n")
    grey("Business and administration:")
    white("         Carl Manneh\n         Daniel Kaplan\n")
    grey("Director of fun:")
    white("         Lydia Winters\n")
    grey("Number crunching and statistics:")
    white("         Patrick Geuder\n")
    grey("Additional programming:")
    white("         Paul Spooner\n         Ryan 'Scaevolus' Hitchman\n         Elliot 'Hippoplatimus' Segal\n")
    grey("Developers of Mo' Creatures (horses etc):")
    white("         John Olarte (DrZhark)\n         Kent Christian Jensen\n         Dan Roque\n")
    grey("Technologies used:")
    white('         Java by Oracle\n         LWJGL by many talented people\n         "3d Sound System" by Paul Lamb\n         JOrbis by JCraft\n\n')
    white("===============")
    yellow("Script Credits")
    white("===============\n")
    grey("Script writer:")
    white("         Oscar Hudson\n")
    grey("Libraries used:")
    white("         Created with Python\n         Colorama by Johnathan Hartley\n         Playsound by Taylor Marks\n")
    grey("Assistance:")
    white("         Noah Pistilli")
    time.sleep(3)
    white('\n\n"Twenty years from now you will be more disappointed by the things that you didnt do than by the ones you did do. So throw off the bowlines. Sail away from the safe harbor. Catch the trade winds in your sails. Explore. Dream. Discover."' + Fore.LIGHTBLACK_EX + " - Unknown\n")

    time.sleep(5)
    check()
    yellow("And that was the end... of the end.")
    time.sleep(2)
    yellow("Or... the end of a dream.")
    time.sleep(8)
    check()

    time.sleep(5)
    
    
check()
threading.Thread(target=audio).start()
threading.Thread(target=text).start()