from random import randint, choice
'''
    game code needs to:
        determine other characteristics of the bomb such as
            number and type of ports
            serial number
            indicator lights
            external batteries number and type



    then for each module:

        for wires:
            determine solution of the puzzle
            determine color sequence of wires but dont actually put them in the code, just send it to the setup
        for button:
            determine button color
            determine button text (the color the strip/multicolor LED turns can be determined by the first pi)
        for simon:
            determine color sequence
        for memory:
            determine if we're doing memory (it basically generates itself)
        for morse:
            determine which codeword it is
        for mazes:
            determine which maze (the game can randomly determine the positions of the player and the goal)
        for needy module:
            determine which needy module to add

the game code can be separated into a first section and then successive sections separated by periods
the first section can determine the non-module stuff
every successive group can determine which module and its characteristics

FIRST GROUP:
    First Digit: serial number
        1: last digit is odd, serial contains a vowel
        2: last digit is odd, serial lacks vowel
        3: last digit isnt odd, serial contains a vowel
        4: last digit isnt odd, serial lacks vowel
    Second Digit: indicator light
        1: no indicator
        2: indicator CAR
        3: indicator FRK
        4: some other random indicator
    Third Digit: Batteries by Type and Number 
        1: no batteries
        2: one battery
        3: two batteries
        4: three batteries

SUCCESSIVE GROUPS BY MODULE
Wires: A
    Each Digit: wire color
        (Possible wire colors: blue, black, white, red, yellow)
        1: red
        2: blue
        3: white
        4: yellow
        5: black

Button: B
    First Digit: color
        1: blue
        2: white
        3: yellow
        4: red
    Second Digit: Text
        1: Abort
        2: Detonate
        3: Hold
        4: Press

Simon: C

Memory: D

Morse: E
    First Digit: phrase
        1: shell
        2: halls
        3: slick
        4: trick
        5: boxes
        6: leaks
        7: strobe
        8: bistro
        9: flick
        0: bombs
        a: break
        b: brick
        c: steak
        d: sting
        e: vector
        f: beats

Mazes: F
    First Digit: maze number
        1: maze 1
        2: maze 2
        3: maze 3
        4: maze 4
        5: maze 5
        6: maze 6
        7: maze 7
        8: maze 8
        9: maze 9

Passwords: G
    First Digit: first letter
        1: a
        2: b
        3: c
        4: e
        5: f
        6: g
        7: h
        8: l
        9: n
        a: o
        b: p
        c: r
        d: s
        e: t
        f: w
    Second Digit: which number password the solution is from the words that have that first letter (the 5 s words, small, sound, spell, still, study would be 1,2,3,4,5 respectively)
        1: word 1
        2: word 2
        3: word 3
        4: word 4
        5: word 5
        6: word 6

Needy: H
    First Digit: which module it is
        1: Vent Gas
        2: Capacitor
'''

#   initials variables
#       serial number
ODD_VOWEL = "1"
ODD_NO_VOWEL = "2"
EVEN_VOWEL = "3"
EVEN_NO_VOWEL = "4"
#       list of serial numbers
SERIAL_NUMBERS = [
ODD_VOWEL,
ODD_NO_VOWEL,
EVEN_VOWEL,
EVEN_NO_VOWEL
]

#       indicator
NO_INDICATOR = "1"
CAR_INDICATOR = "2"
FRK_INDICATOR = "3"
OTHER_INDICATOR = "4"

#       batteries
BATTERIES_0 = "0"
BATTERIES_1 = "1"
BATTERIES_2 = "2"
BATTERIES_3 = "3"
#       list of numbers of batteries
BATTERIES_LIST = [
BATTERIES_0,
BATTERIES_1,
BATTERIES_2,
BATTERIES_3
]

#   segment start variables
WIRE_START = "a"
BUTTON_START = "b"
SIMON_START = "c"
MEMORY_START = "d"
MORSE_START = "e"
MAZES_START = "f"
PASSWORDS_START = "g"
NEEDY_START = "h"

#   wires variables
#       wire color
WIRE_RED  = "1"
WIRE_BLUE  = "2"
WIRE_WHITE  = "3"
WIRE_YELLOW  = "4"
WIRE_BLACK = "5"

#   buttons variables
#       button color
BUTTON_BLUE = "1"
BUTTON_WHITE = "2"
BUTTON_YELLOW = "3"
BUTTON_RED = "4"

#       button text
BUTTON_ABORT = "1"
BUTTON_DETONATE = "2"
BUTTON_HOLD = "3"
BUTTON_PRESS = "4"

#   morse variables
#       what the morse phrase is
MORSE_SHELL = "1"
MORSE_HALLS = "2"
MORSE_SLICK = "3"
MORSE_TRICK = "4"
MORSE_BOXES = "5"
MORSE_LEAKS = "6"
MORSE_STROBE = "7"
MORSE_BISTRO = "8"
MORSE_FLICK = "9"
MORSE_BOMBS = "0"
MORSE_BREAK = "a"
MORSE_BRICK = "b"
MORSE_STEAK = "c"
MORSE_STING = "d"
MORSE_VECTOR = "e"
MORSE_BEATS = "f"

#       list of all morse phrases
MORSE_CODES = [
MORSE_SHELL,
MORSE_HALLS,
MORSE_SLICK,
MORSE_TRICK,
MORSE_BOXES,
MORSE_LEAKS,
MORSE_STROBE,
MORSE_BISTRO,
MORSE_FLICK,
MORSE_BOMBS,
MORSE_BREAK,
MORSE_BRICK,
MORSE_STEAK,
MORSE_STING,
MORSE_VECTOR,
MORSE_BEATS
]

#   maze variables
#       which maze it is
MAZES_1 = "1"
MAZES_2 = "2"
MAZES_3 = "3"
MAZES_4 = "4"
MAZES_5 = "5"
MAZES_6 = "6"
MAZES_7 = "7"
MAZES_8 = "8"
MAZES_9 = "9"

#       list of maze choices
MAZES_CHOICES = [
MAZES_1,
MAZES_2,
MAZES_3,
MAZES_4,
MAZES_5,
MAZES_6,
MAZES_7,
MAZES_8,
MAZES_9
]

#   passwords variables
#       first letter of password
PASSWORDS_A = "1"
PASSWORDS_B = "2"
PASSWORDS_C = "3"
PASSWORDS_E = "4"
PASSWORDS_F = "5"
PASSWORDS_G = "6"
PASSWORDS_H = "7"
PASSWORDS_L = "8"
PASSWORDS_N = "9"
PASSWORDS_O = "0"
PASSWORDS_P = "a"
PASSWORDS_R = "b"
PASSWORDS_S = "c"
PASSWORDS_T = "d"
PASSWORDS_W = "e"

#       which number password it is
PASSWORDS_1 = "1"
PASSWORDS_2 = "2"
PASSWORDS_3 = "3"
PASSWORDS_5 = "5"
PASSWORDS_6 = "6"

#       list of password numbers
PASSWORDS_IDS = [
PASSWORDS_1,
PASSWORDS_2,
PASSWORDS_3,
PASSWORDS_5,
PASSWORDS_6
]

#       lists of first letters by number of passwords that have that first letter
PASSWORDS_LEN1 = [
PASSWORDS_B,
PASSWORDS_C,
PASSWORDS_E,
PASSWORDS_G,
PASSWORDS_H,
PASSWORDS_N,
PASSWORDS_O,
PASSWORDS_R
]

PASSWORDS_LEN2 = [
PASSWORDS_F,
PASSWORDS_L
]

PASSWORDS_LEN3 = [
PASSWORDS_A,
PASSWORDS_P
]

PASSWORDS_LEN5 = [
PASSWORDS_S
]

PASSWORDS_LEN6 = [
PASSWORDS_T,
PASSWORDS_W
]

#   needy variables
NEEDY_VENT = "1"
NEEDY_CAPACITOR = "2"

NEEDY_MODULES = [
NEEDY_VENT,
NEEDY_CAPACITOR
]


def generateCode(difficulty = 0):
    code = generatePrefix()

    if difficulty <= 3:
        for _ in range(difficulty):
            run = choice(easyModules)
            code += run
    if difficulty >= 4:
        for _ in range(difficulty-3):
            run = choice(hardModules)
            print(run)
    
    return code

def splitCode(code:str):
    segments = code.split(".")
    wireSegment = None
    buttonSegment = None
    simonSegment = None
    morseSegment = None
    mazeSegment = None
    passwordSegment = None
    needySegment = None
    for segment in segments:
        if segment.startswith(WIRE_START): wireSegment = segment[1:]
        elif segment.startswith(BUTTON_START): buttonSegment = segment[1:]
        elif segment.startswith(SIMON_START): simonSegment = segment[1:]
        elif segment.startswith(MORSE_START): morseSegment = segment[1:]
        elif segment.startswith(MAZES_START): mazeSegment = segment[1:]
        elif segment.startswith(PASSWORDS_START): passwordSegment = segment[1:]
        elif segment.startswith(NEEDY_START): needySegment = segment[1:]
        else: prefix = segment
    return prefix, wireSegment, buttonSegment, simonSegment, morseSegment, mazeSegment, passwordSegment, needySegment

#prefix
def generatePrefix():
    serialNumber = ""
    indicator = ""
    batteries = ""

    serialNumber = choice(SERIAL_NUMBERS)

    indicatorProbability = choice(range(11))
    if indicatorProbability == 0:
        indicator = NO_INDICATOR
    elif indicatorProbability == 1:
        indicator = CAR_INDICATOR
    elif indicatorProbability == 2:
        indicator = FRK_INDICATOR
    else:
        indicator = OTHER_INDICATOR
    
    batteries = BATTERIES_LIST[choice(range(3))]

    return serialNumber + indicator + batteries


#wires
def createWires():
    wireSegment = "." + WIRE_START
    numberOfWires = randint(3, 6)
    wireColors = [WIRE_RED, WIRE_BLUE, WIRE_WHITE, WIRE_YELLOW, WIRE_BLACK]
    for wire in range(numberOfWires):
        wireSegment = wireSegment + choice(wireColors)
    return wireSegment

def wiresWalkthrough(segment):
    print(segment)

def wiresSolution(segment):
    pass

#button
def createButton():
    buttonSegment = "." + BUTTON_START
    buttonColor = choice([BUTTON_BLUE, BUTTON_WHITE, BUTTON_YELLOW, BUTTON_RED])
    buttonText = choice([BUTTON_ABORT, BUTTON_DETONATE, BUTTON_HOLD, BUTTON_PRESS])
    return buttonSegment + buttonColor + buttonText

def buttonSolution(segment):
    pass

#simon
def createSimon():
    return "." + SIMON_START

#memory
def createMemory():
    return "." + MEMORY_START

def memorySolution(segment):
    pass

#morse
def createMorse():
    morseSegment = "." + MORSE_START
    morseCode = choice(MORSE_CODES)
    return morseSegment + morseCode

def morseSolution(segment):
    pass

#maze
def createMaze():
    mazeSegment = "." + MAZES_START
    mazePick = choice(MAZES_CHOICES)
    return mazeSegment + mazePick

def mazeSolution(segment):
    pass

#password
def createPasswords():
    passwordsSegment = "." + PASSWORDS_START
    password = choice(range(34))
    passwordFirstLetter = ""
    passwordNumber = ""
    if password < 2:
        passwordFirstLetter = PASSWORDS_A
    elif password < 3:
        passwordFirstLetter = PASSWORDS_B
    elif password < 4:
        passwordFirstLetter = PASSWORDS_C
    elif password < 5:
        passwordFirstLetter = PASSWORDS_E
    elif password < 7:
        passwordFirstLetter = PASSWORDS_F
    elif password < 8:
        passwordFirstLetter = PASSWORDS_G
    elif password < 9:
        passwordFirstLetter = PASSWORDS_H
    elif password < 11:
        passwordFirstLetter = PASSWORDS_L
    elif password < 12:
        passwordFirstLetter = PASSWORDS_N
    elif password < 13:
        passwordFirstLetter = PASSWORDS_O
    elif password < 16:
        passwordFirstLetter = PASSWORDS_P
    elif password < 17:
        passwordFirstLetter = PASSWORDS_R
    elif password < 22:
        passwordFirstLetter = PASSWORDS_S
    elif password < 28:
        passwordFirstLetter = PASSWORDS_T
    elif password < 34:
        passwordFirstLetter = PASSWORDS_W
    
    if passwordFirstLetter in PASSWORDS_LEN1:
        passwordNumber = choice(PASSWORDS_IDS[:1])
    if passwordFirstLetter in PASSWORDS_LEN2:
        passwordNumber = choice(PASSWORDS_IDS[:2])
    if passwordFirstLetter in PASSWORDS_LEN3:
        passwordNumber = choice(PASSWORDS_IDS[:3])
    if passwordFirstLetter in PASSWORDS_LEN5:
        passwordNumber = choice(PASSWORDS_IDS[:4])
    if passwordFirstLetter in PASSWORDS_LEN6:
        passwordNumber = choice(PASSWORDS_IDS)
    
    return passwordsSegment + passwordFirstLetter + passwordNumber

        


def passwordsSolution(segment):
    pass

#needy
def createNeedy():
    needySegment = "." + NEEDY_START
    needyModule = choice(NEEDY_MODULES)
    return needySegment + needyModule

def needySolution(segment):
    pass

easyModules=[createWires(), createButton(), createSimon()]
hardModules=[createMemory(), createMaze(), createPasswords()]
