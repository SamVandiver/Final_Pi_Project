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
    EVEN_NO_VOWEL]

#       indicator
NO_INDICATOR = "1"
CAR_INDICATOR = "2"
FRK_INDICATOR = "3"
OTHER_INDICATOR = "4"
INDICATORS_LIST = [
    "SND",
    "CLR",
    "IND",
    "FRQ",
    "SIG",
    "NSA",
    "MSA",
    "TRN",
    "BOB"
]

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
    BATTERIES_3]

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
WIRE_RED = "1"
WIRE_BLUE = "2"
WIRE_WHITE = "3"
WIRE_YELLOW = "4"
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
    MORSE_BEATS]

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
    MAZES_9]

#   passwords variables
#       first letter of password
PASSWORDS_APEX = "00"
PASSWORDS_BEAN = "01"
PASSWORDS_BLUR = "02"
PASSWORDS_BONK = "03"
PASSWORDS_CARS = "04"
PASSWORDS_CHAD = "05"
PASSWORDS_COOL = "06"
PASSWORDS_CARE = "07"
PASSWORDS_CORE = "08"
PASSWORDS_CURE = "09"
PASSWORDS_DEAL = "10"
PASSWORDS_FOUR = "11"
PASSWORDS_HYPE = "12"
PASSWORDS_LAMP = "13"
PASSWORDS_MUSH = "14"
PASSWORDS_QUIT = "15"
PASSWORDS_ROAD = "16"
PASSWORDS_SEAL = "17"
PASSWORDS_SIGN = "18"
PASSWORDS_SINE = "19"
PASSWORDS_SLAG = "20"
PASSWORDS_SPUR = "21"
PASSWORDS_TYPO = "22"
PASSWORDS_VILE = "23"
PASSWORDS_WIFI = "24"
PASSWORDS_XRAY = "25"
PASSWORDS_YELP = "26"
PASSWORDS_ZING = "27"
PASSWORDS_SOLUTIONS = [
    "APEX",
    "BEAN",
    "BLUR",
    "BONK",
    "CARS",
    "CHAD",
    "COOL",
    "CARE",
    "CORE",
    "CURE",
    "DEAL",
    "FOUR",
    "HYPE",
    "LAMP",
    "MUSH",
    "QUIT",
    "ROAD",
    "SEAL",
    "SIGN",
    "SINE",
    "SLAG",
    "SPUR",
    "TYPO",
    "VILE",
    "WIFI",
    "XRAY",
    "YELP",
    "ZING"
]


#   needy variables
NEEDY_VENT = "1"
NEEDY_CAPACITOR = "2"

NEEDY_MODULES = [
    NEEDY_VENT,
    NEEDY_CAPACITOR]

def generateCode():
    # equals '{1-4}+{1-4}{0-3}'
    code = generatePrefix()
    create = False
    setup = ["wires", "button", "simon", "morse", "maze", "passwords", "needy"]
    for _ in setup:
        while True:
            x = input(f"Do you want the {_} module? y/n\n")
            if x.lower() == "y" or "yes":
                create = True
                break
            elif x.lower() == "n" or "no":
                create = False
                break
            else:
                print("Please retry.")
        if create is True:
            if _ == "wires":
                run = createWires()
            elif _ == "button":
                run = createButton()
            elif _ == "simon":
                run = createSimon()
            elif _ == "morse":
                run = createMorse()
            elif _ == "maze":
                run = createMaze()
            elif _ == "passwords":
                run = createPasswords()
            elif _ == "needy":
                run = createNeedy()
            code += run
    # returns: '[1-4 + 1-4 + 0-3] + random { [.a + ('1'-'5')*(3-5)] + [.b + 1-4 + 1-4] + [.c + (1-4)*6] + [.e + (0-9+a-f)] + [.f + 1-9] + [.g + (0-9+a-e) + 1-6] }'
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

    # equates to '1'-'4'
    serialNumber = choice(SERIAL_NUMBERS)

    # equates to '1'-'4'
    indicatorProbability = choice(range(11))
    if indicatorProbability == 0: indicator = NO_INDICATOR
    elif indicatorProbability == 1: indicator = CAR_INDICATOR
    elif indicatorProbability == 2: indicator = FRK_INDICATOR
    else: indicator = OTHER_INDICATOR

    # equates to '0'-'3'
    batteries = BATTERIES_LIST[choice(range(3))]

    return serialNumber + indicator + batteries


#wires
def createWires():
    wireSegment = "." + WIRE_START
    numberOfWires = randint(3, 6)
    wireColors = [WIRE_RED, WIRE_BLUE, WIRE_WHITE, WIRE_YELLOW, WIRE_BLACK]
    for wire in range(numberOfWires):
        wireSegment += choice(wireColors)
    # returns ['.a' + ('1'-'5')*(3-5)]
    return wireSegment

def wiresWalkthrough(segment):
    print(segment)

def wiresSolution(segment:str, prefix:str):
    wireLogicVariable = None
    serialIsOdd = False
    if prefix[:1] in [ODD_NO_VOWEL, ODD_VOWEL]:
        serialIsOdd = True
    segmentList = []
    for letter in segment:
        segmentList.append(letter)
    if len(segment) == 3:
        if WIRE_RED not in segmentList:
            wireLogicVariable = 1
        elif segmentList[2] == WIRE_WHITE:
            wireLogicVariable = 2
        elif segmentList.count(WIRE_BLUE) >= 2:
            if segmentList[2] == WIRE_BLUE:
                wireLogicVariable = 2
            else:
                wireLogicVariable = 1
        else:
            wireLogicVariable = 2
    if len(segment) == 4:
        if segmentList.count(WIRE_RED) > 1:
            wireLogicVariable = segment.rfind(WIRE_RED)
        elif ((segmentList[-1] == WIRE_YELLOW) and (WIRE_RED not in segmentList)):
            wireLogicVariable = 0
        elif segmentList.count(WIRE_BLUE) == 1:
            wireLogicVariable = 0
        elif segmentList.count(WIRE_YELLOW) > 1:
            wireLogicVariable = 3
        else:
            wireLogicVariable = 1
    if len(segment) == 5:
        if ((segmentList[4] == WIRE_BLACK) and (serialIsOdd)):
            wireLogicVariable = 3
        elif ((segmentList.count(WIRE_RED) == 1) and (segmentList.count(WIRE_YELLOW) > 1)):
            wireLogicVariable = 0
        elif segmentList.count(WIRE_BLACK) == 0:
            wireLogicVariable = 1
        else:
            wireLogicVariable = 0
    if len(segment) == 6:
        if ((segmentList.count(WIRE_YELLOW) == 0) and (serialIsOdd)):
            wireLogicVariable = 2
        elif ((segmentList.count(WIRE_YELLOW) == 1) and (segmentList.count(WIRE_WHITE) > 1)):
            wireLogicVariable = 3
        elif segmentList.count(WIRE_RED) == 0:
            wireLogicVariable = 5
        else:
            wireLogicVariable = 3
    return wireLogicVariable

#button
def createButton():
    buttonSegment = "." + BUTTON_START
    buttonColor = choice([BUTTON_BLUE, BUTTON_WHITE, BUTTON_YELLOW, BUTTON_RED])
    buttonText = choice([BUTTON_ABORT, BUTTON_DETONATE, BUTTON_HOLD, BUTTON_PRESS])
    # returns ['.b' + '1'-'4' + '1'-'4']
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
    # returns ['.e' + '0'-'9'+'a'-'f']
    return morseSegment + morseCode

def morseSolution(segment):
    pass

#maze
def createMaze():
    mazeSegment = "." + MAZES_START
    mazePick = choice(MAZES_CHOICES)
    # returns ['.f' + '1'-'9']
    return mazeSegment + mazePick

def mazeSolution(segment):
    pass

#password
def createPasswords():
    passwordsSegment = "." + PASSWORDS_START
    password = choice(range(27))
    password = str(password)
    if len(password) == 1:
        password = "0" + password
    return passwordsSegment + password

def passwordsSolution(segment):
    pass

#needy
def createNeedy():
    needySegment = "." + NEEDY_START
    return needySegment

def needySolution(segment):
    pass
