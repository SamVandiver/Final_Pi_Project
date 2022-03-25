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

#   segment start variables
WIRE_START = ".a"
BUTTON_START = ".b"
SIMON_START = ".c"
MEMORY_START = ".d"
MORSE_START = ".e"
MAZES_START = ".f"
PASSWORDS_START = ".g"
NEEDY_START = ".h"

#   wires variables
WIRE_RED  = "1"
WIRE_BLUE  = "2"
WIRE_WHITE  = "3"
WIRE_YELLOW  = "4"
WIRE_BLACK = "5"

#   buttons variables
BUTTON_BLUE = "1"
BUTTON_WHITE = "2"
BUTTON_YELLOW = "3"
BUTTON_RED = "4"
BUTTON_ABORT = "1"
BUTTON_DETONATE = "2"
BUTTON_HOLD = "3"
BUTTON_PRESS = "4"

#   morse variables
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



def generateCode():
    pass

#wires
def createWires():
    wireSegment = WIRE_START
    numberOfWires = randint(3, 6)
    wireColors = [WIRE_RED, WIRE_BLUE, WIRE_WHITE, WIRE_YELLOW, WIRE_BLACK]
    for wire in range(numberOfWires):
        wireSegment = wireSegment + choice(wireColors)
    return wireSegment

def wiresSolution(segment):
    pass

#button
def createButton():
    buttonSegment = BUTTON_START
    buttonColor = choice([BUTTON_BLUE, BUTTON_WHITE, BUTTON_YELLOW, BUTTON_RED])
    buttonText = choice([BUTTON_ABORT, BUTTON_DETONATE, BUTTON_HOLD, BUTTON_PRESS])
    return buttonSegment + buttonColor + buttonText

def buttonSolution(segment):
    pass

#simon
def createSimon():
    return SIMON_START

#memory
def createMemory():
    return MEMORY_START

def memorySolution(segment):
    pass

#morse
def createMorse():
    morseSegment = MORSE_START
    morseCode = choice([MORSE_CODES])
    return morseSegment + morseCode

def morseSolution(segment):
    pass

#maze
def createMaze():
    pass

def mazeSolution(segment):
    pass

#password
def createPasswords():
    pass

def passwordsSolution(segment):
    pass

#needy
def createNeedy():
    pass

def needySolution(segment):
    pass