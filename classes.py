import pygame
import os
import codeGenLibrary as CODE
import piOneMain as pi

#   adds a bunch of stuff so vs code doesnt get pissed at me
screen = pygame.display.set_mode((0, 0))
PIHEIGHT = 600
PIWIDTH = 800


#   panel class and its children (obsolete)

class Panel(pygame.sprite.Sprite):
    def __init__(self, width, height, x, y, fillColor):
        super().__init__()

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.fillColor = fillColor

        self.surface = pygame.Surface((self.width, self.height))
        self.surface.fill(self.fillColor)

        self.rect = self.surface.get_rect()
    
    def draw(self):
        screen.blit(self.surface, ((self.x, self.y)))

#   a class (which probably would be better as a bunch of functions) which sets up all the parts of the window which don't need to change every frame
class DisplaySetup:
    def __init__(self) -> None:
        pass


    def startScreen(self):
        screen.fill((100, 100, 100))

    def playingScreen():
        screen.fill((100, 100, 100))
        sidePanel = Panel(250, PIHEIGHT, 0, 0, (60, 60, 60))
        strikePanel = Panel(PIWIDTH, 150, 250, 0, (20,20,20))
        return sidePanel, strikePanel

class Strikes(Panel):
    def __init__(self, strikes):
        super().__init__()
        self.strikes = strikes

    def loadStrikes(self):
        pass

    def addStrike(self):
        pass

#   module class and its children
class Module:

    def __init__(self, id, segment):
        self.id = id
        self.segment = segment

    def change(self):
        pass

    def fail(self):
        raise NotImplementedError

    def draw(self):
        raise NotImplementedError

class Button(Module):
    def __init__(self, id, segment):
        super().__init__(id, segment)


#   functions that dont belong in codeGenLibrary
def loadImages():

    #   get the font
    global font1
    font1 = pygame.font.SysFont

    #   start loading stuff
    os.chdir("assets/screens")
    global startScreen
    global mainScreenBase
    startScreen = pygame.image.load("start screen.png")
    mainScreenBase = pygame.image.load("gui draft1.png")

    #   gets everything from indicators
    os.chdir("../indicator")
    global timerNoStrikes
    global timerOneStrike
    global timerTwoStrikes
    timerNoStrikes = pygame.image.load("timer0.png")
    timerOneStrike = pygame.image.load("timer1.png")
    timerTwoStrikes = pygame.image.load("timer2.png")

    #   gets everything from buttoncolors
    os.chdir("../buttoncolors")
    global buttonBlue
    global buttonWhite
    global buttonYellow
    global buttonRed
    buttonBlue = pygame.image.load("buttonBlue.png")
    buttonWhite = pygame.image.load("buttonWhite.png")
    buttonYellow = pygame.image.load("buttonYellow.png")
    buttonRed = pygame.image.load("buttonRed.png")

    #   gets everything from buttonwords
    os.chdir("../buttonwords")

    #   gets everything from modules/passwords
    os.chdir("../modules/passwords")
    global passwordsBase
    passwordsBase = pygame.image.load("passwords.png")


# morse code dictionary
MC={'A':'.-',      'B':'-...',
    'C':'-.-.',    'D':'-..',
    'E':'.',       'F':'..-.',
    'G':'--.',     'H':'....',
    'I':'..',      'J':'.---',
    'K':'-.-',     'L':'.-..',
    'M':'--',      'N':'-.',
    'O':'---',     'P':'.--.',
    'Q':'--.-',    'R':'.-.',
    'S':'...',     'T':'-',
    'U':'..-',     'V':'...-',
    'W':'.--',     'X':'-..-',
    'Y':'-.--',    'Z':'--..',
    '1':'.----',   '2':'..---',
    '3':'...--',   '4':'....-',
    '5':'.....',   '6':'-....',
    '7':'--...',   '8':'---..',
    '9':'----.',   '0':'-----',
    ', ':'--..--', '.':'.-.-.-',
    '?':'..--..',  '/':'-..-.',
    '-':'-....-',  '(':'-.--.',
    ')':'-.--.-'}

def SIMON():
    code = CODE.simonSegment
    global message
    message = input('Input code { }...')
    guess = encrypt(message)
    if guess != code: pi.strike()
    else: print('Good job.')

# Function to encrypt the string according to the morse code chart
def encrypt(message):
    C = ''
    for character in message:
        # Looks up the dictionary and adds the correspponding morse code along with a space to separate morse codes for different characters
        if character != ' ': C += MC[character] + ' '
        # 1 space indicates different characters and 2 indicates different words
        else: C += ' '
    return C

def WIRES():
    turn=int(input(f'{CODE.W}\n')) # Just for testing, normally the player would have to use the manual to get the right wire
    turn-=1 # Because indexing starts at 0
    if CODE.W[turn] == False: pi.strike()
    else:
        print('Good job.')
        CODE.W.pop(turn)
    print('Congratulations you have succesfully unplugged the correct wires.')
