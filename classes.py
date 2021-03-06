import pygame
import os
import codeGenLibrary as CODE
import random

#   adds a bunch of stuff so vs code doesnt get pissed at me
screen = pygame.display.set_mode((0, 0))
PIHEIGHT = 480
PIWIDTH = 800
DEBUG = True


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

#   function for checking if the game is over
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
    #   return a 6-letter serial number and one of the 3-letter indicators from the manual
    #   given the input prefix
    #   reminder: first character is the parameters for the serial number, second is for the indicator.
    #   use the constants like CODE.ODD_NO_VOWEL and CODE.CAR_INDICATOR
    #   for bonus points return the number of batteries as well
    serial = ""
    firstconsonants = random.randint(0,4)
    VOWELS = ["a","e","i","o","u"]
    CONSONANTS = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]
    ODDS = ["1", "3", "5", "7", "9"]
    EVENS = ["2", "4", "6", "8"]
    for padding in range(firstconsonants):
        serial += random.choice(CONSONANTS)
    if ((prefix[0:1] == CODE.ODD_VOWEL) or (prefix[0:1] == CODE.EVEN_VOWEL)):
        serial += random.choice(VOWELS)
    else:
        serial += random.choice(CONSONANTS)
    for padding in range(4-firstconsonants):
        serial += random.choice(CONSONANTS)
    serial = serial.upper()
    if ((prefix[0:1] == CODE.ODD_VOWEL) or (CODE.ODD_NO_VOWEL)):
        serial += random.choice(ODDS)
    else:
        serial += random.choice(EVENS)

    if prefix[1:2] == CODE.NO_INDICATOR:
        indicator = None
    elif prefix[1:2] == CODE.CAR_INDICATOR:
        indicator = "CAR"
    elif prefix[1:2] == CODE.FRK_INDICATOR:
        indicator = "FRK"
    elif prefix[1:2] == CODE.OTHER_INDICATOR:
        indicator = random.choice(CODE.INDICATORS_LIST)

    if prefix[2:3] == CODE.BATTERIES_0:
        numBatteries = 0
    elif prefix[2:3] == CODE.BATTERIES_1:
        numBatteries = 1
    elif prefix[2:3] == CODE.BATTERIES_2:
        numBatteries = 2
    elif prefix[2:3] == CODE.BATTERIES_3:
        numBatteries = 3
    # returns [('a-z')*6 + random { 'None, CAR, FRK, etc' } + '0-3']
    return serial, indicator, numBatteries

# Function to encrypt the string according to the morse code chart
def encrypt(message):
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
    C = ''
    for character in message:
        # Looks up the dictionary and adds the correspponding morse code along with a space to separate morse codes for different characters
        if character != ' ': C += MC[character] + ' '
        # 1 space indicates different characters and 2 indicates different words
        else: C += ' '
    return C


#   green, red, yellow, blue = 1, 2, 3, 4
def translateSimon(simonInput, strikes, prefix):
    if DEBUG:
        print(f"input, strikes, prefix: {simonInput}, {strikes}, {prefix}")
    if ((prefix[0:1] == CODE.ODD_VOWEL) or (prefix[0:1] == CODE.EVEN_VOWEL)):
        if strikes == 0:
            if simonInput == 4:
                return 2
            elif simonInput == 2:
                return 4
            elif simonInput == 3:
                return 1
            elif simonInput == 1:
                return 3
        elif strikes == 1:
            if simonInput == 3:
                return 2
            elif simonInput == 1:
                return 4
            elif simonInput == 4:
                return 1
            elif simonInput == 2:
                return 3
        elif strikes == 2:
            if simonInput == 1:
                return 2
            elif simonInput == 2:
                return 4
            elif simonInput == 3:
                return 1
            elif simonInput == 4:
                return 3
    else:
        if strikes == 0:
            if simonInput == 4:
                return 2
            elif simonInput == 3:
                return 4
            elif simonInput == 1:
                return 1
            elif simonInput == 2:
                return 3
        elif strikes == 1:
            if simonInput == 2:
                return 2
            elif simonInput == 4:
                return 4
            elif simonInput == 3:
                return 1
            elif simonInput == 1:
                return 3
        elif strikes == 2:
            if simonInput == 3:
                return 2
            elif simonInput == 1:
                return 4
            elif simonInput == 4:
                return 1
            elif simonInput == 2:
                return 3

def passwordsSetBarrels(barrelOne, barrelTwo, barrelThree, barrelFour, barrelSegment)
    solution = CODE.PASSWORDS_SOLUTIONS[int(barrelSegment)]
    barrelList = [barrelOne, barrelTwo, barrelThree, barrelFour]
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lettersAsList = []
    possibleSolutions = []
    for letter in letters:
        lettersAsList.append(letter)
    barrelOne.append(solution[0:1])
    barrelTwo.append(solution[1:2])
    barrelThree.append(solution[2:3])
    barrelFour.append(solution[3:])
    for barrel in barrelList:
        barrel.append(random.choice(lettersAsList))
        random.shuffle(barrel)
    for firstLetter in barrelOne:
        for secondLetter in barrelTwo:
            for thirdLetter in barrelThree:
                for fourthLetter in barrelFour:
                    permutation = firstLetter + secondLetter + thirdLetter + fourthLetter
                    if permutation in CODE.PASSWORDS_SOLUTIONS:
                        possibleSolutions.append(permutation)
    if len(possibleSolutions) == 1:
        return barrelOne, barrelTwo, barrelThree, barrelFour
        