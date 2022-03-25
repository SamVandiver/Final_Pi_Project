import random
import socket
import sys
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
Wires:
    First digit: solution
        (3 wires)
        1: no red wires
        2: otherwise, last wire white
        3: otherwise, multiple blue wires
        4: else
        (4 wires)
        5: multiple red wires and odd serial number
        6: otherwise, no red wires and last wire is yellow
        7: otherwise, exactly one blue
        8: otherwise, multiple yellow wires
        9: else
        (5 wires)
        a: last wire is black and odd serial number
        b: otherwise, one red multiple yellow
        c: otherwise, no black wires
        d: else
        (6 wires)
        e: no yellow wires and odd serial number
        f: otherwise, one yellow multiple white
        g: otherwise, no red wires
        h: else
'''