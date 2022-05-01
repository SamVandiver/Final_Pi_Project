import pygame
import os
import codeGenLibrary as CODE

#   adds a bunch of stuff so vs code doesnt get pissed at me
screen = pygame.display.set_mode((0, 0))
PIHEIGHT = 480
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
def loadImages(buttonSegment:str, simonSegment:str, morseSegment:str, mazeSegment:str, passwordsSegment:str, needySegment:str):

    #   get the fonts
    global timerFont
    timerFont = pygame.font.SysFont("Arial", 30)

    #   start loading stuff
    os.chdir("assets/screens")
    global startScreen
    global mainScreenBase
    global winScreen
    global loseScreen
    startScreen = pygame.image.load("start screen.png")
    mainScreenBase = pygame.image.load("gui draft1.png")
    winScreen = pygame.image.load("victoryroyale.png")
    loseScreen = pygame.image.load("gameover.png")

    #   gets everything from indicators
    os.chdir("../indicator")
    global timerNoStrikes
    global timerOneStrike
    global timerTwoStrikes
    global strikeList
    timerNoStrikes = pygame.image.load("timer0.png")
    timerOneStrike = pygame.image.load("timer1.png")
    timerTwoStrikes = pygame.image.load("timer2.png")
    strikeList = [timerNoStrikes, timerOneStrike, timerTwoStrikes, timerTwoStrikes]

    #   gets everything from buttoncolors
    os.chdir("../buttoncolors")
    global buttonBase
    if buttonSegment[:1] == CODE.BUTTON_BLUE:
        buttonBase = pygame.image.load("buttonBlue.png")
    elif buttonSegment[:1] == CODE.BUTTON_YELLOW:
        buttonBase = pygame.image.load("buttonYellow.png")
    elif buttonSegment[:1] == CODE.BUTTON_WHITE:
        buttonBase = pygame.image.load("buttonWhite.png")
    elif buttonSegment[:1] == CODE.BUTTON_RED:
        buttonBase = pygame.image.load("buttonRed.png")

    #   gets everything from buttonwords
    os.chdir("../buttonwords")
    global buttonWord
    wordForButton = ""
    #   determines what word goes on the button
    if buttonSegment[1:2] == CODE.BUTTON_ABORT:
        wordForButton += "abort"
    elif buttonSegment[1:2] == CODE.BUTTON_DETONATE:
        wordForButton += "detonate"
    elif buttonSegment[1:2] == CODE.BUTTON_PRESS:
        wordForButton += "press"
    elif buttonSegment[1:2] == CODE.BUTTON_HOLD:
        wordForButton += "hold"
    #   determines color of word
    if ((buttonSegment[:1] == CODE.BUTTON_BLUE) or (buttonSegment[:1] == CODE.BUTTON_RED)):
        wordForButton += "White"
    else:
        wordForButton += "Black"
    #   adds .png to the wordForButton
    wordForButton += ".png"
    buttonWord = pygame.image.load(wordForButton)

    #   gets everything from modules/passwords
    os.chdir("../modules/passwords")
    global passwordsBase
    passwordsBase = pygame.image.load("passwords.png")

    #   gets everything from modules/morse
    os.chdir("../morse")
    global morseBase
    morseBase = pygame.image.load("morse.png")

    #   gets everything from modules/simon
    os.chdir("../simon")
    global simonBase
    simonBase = pygame.image.load("simon.png")

    #gets everything from modules/mazes
    os.chdir("../mazes")
    global mazeBase
    mazeBase = pygame.image.load("mazeBase.png")

    #   gets everything from modules/needy
    os.chdir("../needy")
    global capacitorBase
    capacitorBase = pygame.image.load("capacitor.png")

def createRects(simonTrue, morseTrue, mazeTrue, passwordsTrue, needyTrue):
    if simonTrue:
        simonBlueRect = pygame.Rect(432, 128, 67, 67)
        simonYellowRect = pygame.Rect(501, 128, 67, 67)
        simonGreenRect = pygame.Rect(432, 128, 67, 67)
        simonRedRect = pygame.Rect(501, 197, 67, 67)
    if morseTrue:
        morseUpRect = pygame.Rect(521, 339, 52, 40)
        morseTXRect = pygame.Rect(521, 379, 52, 30)
        morseDownRect = pygame.Rect(521, 409, 52, 40)
    if mazeTrue:
        pass
    if passwordsTrue:
        passButtonSize = (17, 17)
        passOneUpRect = pygame.Rect((230, 330), passButtonSize)
        passOneDownRect = pygame.Rect((230, 409), passButtonSize)
        passTwoUpRect = pygame.Rect((271, 330), passButtonSize)
        passTwoDownRect = pygame.Rect((271, 409), passButtonSize)
        passThreeUpRect = pygame.Rect((302, 330), passButtonSize)
        passThreeDownRect = pygame.Rect((302, 409), passButtonSize)
        passFourUpRect = pygame.Rect((305, 330), passButtonSize)
        passFourDownRect = pygame.Rect((305, 409), passButtonSize)
    if needyTrue:
        needyDischargeRect = pygame.Rect(714, 372, 66, 66)

#   function for checking ifthe game is over
def gameEndCheck(strikes, moduleTable):
    win = True
    if strikes >= 3:
        return "lose"
    else:
        for module in moduleTable:
            if moduleTable[module][0] == True:
                win = False
        if win:
            return "win"

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

def SIMON(strikes):
    code = CODE.simonSegment
    global message
    message = input('Input code { }...')
    guess = encrypt(message)
    # if guess != code: pi.strike()
    # else: print('Good job.')

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
    turn = int(input(f'{CODE.W}\n')) # Just for testing, normally the player would have to use the manual to get the right wire
    turn -= 1 # Because indexing starts at 0
    # if CODE.W[turn] == False: pi.strike()
    # else:
    #     print('Good job.')
    #     CODE.W.pop(turn)
    # print('Congratulations you have succesfully unplugged the correct wires.')
