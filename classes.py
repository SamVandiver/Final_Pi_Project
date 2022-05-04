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
def loadImages(buttonSegment:str, simonSegment:str, morseSegment:str, mazeSegment:str, passwordsSegment:str, needySegment:str, prefix):

    #   get the fonts
    global timerFont
    global indicatorFont
    timerFont = pygame.font.SysFont("Arial", 30)
    indicatorFont = pygame.font.SysFont("Calibri", 20)

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
    if buttonSegment != None:
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
    if buttonSegment != None:
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
        
    #   gets everything from batteries
    os.chdir("../batteries")
    global battery
    if prefix[2:3] == CODE.BATTERIES_3:
        battery = pygame.image.load("batteries3.png")
    elif prefix[2:3] == CODE.BATTERIES_2:
        battery = pygame.image.load("batteries2.png")
    elif prefix[2:3] == CODE.BATTERIES_1:
        battery = pygame.image.load("batteries1.png")
    elif prefix[2:3] == CODE.BATTERIES_0:
        battery = pygame.image.load("batteries0.png")

    #   gets everything from modules/passwords
    os.chdir("../modules/passwords")
    if passwordsSegment != None:
        global passwordsBase
        passwordsBase = pygame.image.load("passwords.png")

    #   gets everything from modules/morse
    os.chdir("../morse")
    if morseSegment != None:
        global morseBase
        morseBase = pygame.image.load("morse.png")

    #   gets everything from modules/simon
    os.chdir("../simon")
    if simonSegment != None:
        global simonBase
        global simonGreenLit
        global simonGreenUnlit
        global simonRedLit
        global simonRedUnlit
        global simonYellowLit
        global simonYellowUnlit
        global simonBlueLit
        global simonBlueUnlit
        global simonLitList
        global simonUnlitList
        global simonCoordsList
        simonBase = pygame.image.load("simon.png")
        simonGreenLit = pygame.image.load("greenLit.png")
        simonGreenUnlit = pygame.image.load("greenUnlit.png")
        simonRedLit = pygame.image.load("redLit.png")
        simonRedUnlit = pygame.image.load("redUnlit.png")
        simonYellowLit = pygame.image.load("yellowLit.png")
        simonYellowUnlit = pygame.image.load("yellowUnlit.png")
        simonBlueLit = pygame.image.load("blueLit.png")
        simonBlueUnlit = pygame.image.load("blueUnlit.png")
        simonLitList = [
            None,
            simonGreenLit,
            simonRedLit,
            simonYellowLit,
            simonBlueLit
        ]
        simonUnlitList = [
            None,
            simonGreenUnlit,
            simonRedUnlit,
            simonYellowUnlit,
            simonBlueUnlit
        ]

        simonBlueCoords = (432, 128)
        simonYellowCoords = (501, 128)
        simonGreenCoords = (432, 197)
        simonRedCoords = (501, 197)
        
        simonCoordsList = [
            None,
            simonGreenCoords,
            simonRedCoords,
            simonYellowCoords,
            simonBlueCoords
        ]
        

    #gets everything from modules/mazes
    os.chdir("../mazes")
    if mazeSegment != None:
        global mazeBase
        mazeBase = pygame.image.load("mazeBase.png")

    #   gets everything from modules/needy
    os.chdir("../needy")
    if needySegment != None:
        global capacitorBase
        capacitorBase = pygame.image.load("capacitor.png")

def createRects(simonTrue, morseTrue, mazeTrue, passwordsTrue, needyTrue):
    if simonTrue:
        global simonBlueRect
        global simonYellowRect
        global simonGreenRect
        global simonRedRect
        global simonRectList
        simonBlueRect = pygame.Rect(432, 128, 67, 67)
        simonYellowRect = pygame.Rect(501, 128, 67, 67)
        simonGreenRect = pygame.Rect(432, 128, 67, 67)
        simonRedRect = pygame.Rect(501, 197, 67, 67)
        simonRectList = [
            None,
            simonGreenRect,
            simonRedRect,
            simonYellowRect,
            simonBlueRect
        ]
    if morseTrue:
        global morseUpRect
        global morseTXRect
        global morseDownRect
        morseUpRect = pygame.Rect(521, 339, 52, 40)
        morseTXRect = pygame.Rect(521, 379, 52, 30)
        morseDownRect = pygame.Rect(521, 409, 52, 40)
    if mazeTrue:
        global mazeUpRect
        global mazeRightRect
        global mazeLeftRect
        global mazeDownRect
        mazeUpRect = pygame.Rect(687, 91, 26, 26)
        mazeRightRect = pygame.Rect(763, 167, 26, 26)
        mazeLeftRect = pygame.Rect(611, 167, 26, 26)
        mazeDownRect = pygame.Rect(687, 243, 26, 26)
    if passwordsTrue:
        passButtonSize = (17, 17)
        global passOneUpRect
        global passOneDownRect
        global passTwoUpRect
        global passTwoDownRect
        global passThreeUpRect
        global passThreeDownRect
        global passFourUpRect
        global passFourDownRect
        passOneUpRect = pygame.Rect((230, 330), passButtonSize)
        passOneDownRect = pygame.Rect((230, 409), passButtonSize)
        passTwoUpRect = pygame.Rect((271, 330), passButtonSize)
        passTwoDownRect = pygame.Rect((271, 409), passButtonSize)
        passThreeUpRect = pygame.Rect((302, 330), passButtonSize)
        passThreeDownRect = pygame.Rect((302, 409), passButtonSize)
        passFourUpRect = pygame.Rect((305, 330), passButtonSize)
        passFourDownRect = pygame.Rect((305, 409), passButtonSize)
    if needyTrue:
        global needyDischargeRect
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
        
def createIndicators(prefix):
    pass
    #   return a 6-letter serial number and one of the 3-letter indicators from the manual
    #   given the input prefix
    #   reminder: first character is the parameters for the serial number, second is for the indicator.
    #   use the constants like CODE.ODD_NO_VOWEL and CODE.CAR_INDICATOR
    #   for bonus points return the number of batteries as well

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
