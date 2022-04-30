from re import S
from sqlite3 import SQLITE_UPDATE
import pygame
import random
import socket
import sys
import os
# import RPi.GPIO as GPIO
import codeGenLibrary as CODE
import classes

#debug
DEBUG = True
SAMSPC = True

'''
# Create a connection to the server application on port 81
TCP_SOCKET = socket.create_connection(('localhost', 81))
 
try:
    data = 'Hi. I am a TCP client sending data to the server'
    TCP_SOCKET.sendall(data)
 
finally:
    print("Closing socket")
    TCP_SOCKET.close()
'''

#   code
#   (example code for now)
code = "123.b12.a1111.c.d.e.f.g.h"

#   print cwd for debugging purposes
if DEBUG:
    print(os.getcwd())
    if SAMSPC:
        os.chdir("Final Pi Project\Final_Pi_Project")


#   constants
#       pi stuff
PIHEIGHT = 800
PIWIDTH = 600

#   start pygame
pygame.init()
 
#   makes the screen and clock
screen = pygame.display.set_mode((PIHEIGHT, PIWIDTH))
clock = pygame.time.Clock()

#   window title
pygame.display.set_caption("Keep Talking")

#   variables
gamestate = "starting"
strikes = 0
timerLocation = (250,50)
timeLimit = 300000  #   5 minutes in miliseconds
startTime = 0   #   updates when the game starts
buttonLogicVariable = "click"  #   is "click" if button must be pressed and immediately released, otherwise is the color of the button indicator strip as a string
buttonIndicatorColors = ["blue", "white", "yellow"]
buttonShortPress = 500

#   table for all the stuff about each modules
#       "module" : [isTheModuleActive, codeSegment, solutionList, image, (coord,inates)]
moduleTable = {

    "wires"     : [False, None, None, None, None],
    "button"    : [False, None, None, None, (200, 200)],
    "simon"     : [False, None, None, None, (400, 200)],
    "morse"     : [False, None, None, None, (400, 400)],
    "maze"      : [False, None, None, None, (600, 200)],
    "passwords" : [False, None, None, None, (200, 400)],
    "needy"     : [False, None, None, None, (600, 400)]

}

prefix, moduleTable["wires"][1], moduleTable["button"][1], moduleTable["simon"][1], moduleTable["morse"][1], moduleTable["maze"][1], moduleTable["passwords"][1], moduleTable["needy"][1], = CODE.splitCode(code)

#   if splitCode returns a string instead of None, set the module to active
for module in moduleTable:
    if moduleTable[module][1] != None:
        moduleTable[module][0] = True

#   load the stuff
classes.loadImages(moduleTable["button"][1], moduleTable["simon"][1], moduleTable["morse"][1], moduleTable["maze"][1], moduleTable["passwords"][1], moduleTable["needy"][1])

#   wire logic stuff 
if moduleTable["wires"][0]:
    pass

#   the button logic stuff
if moduleTable["button"][0]:
    if moduleTable["button"][1] == f"{CODE.BUTTON_BLUE}{CODE.BUTTON_ABORT}":
        buttonLogicVariable = random.choice(buttonIndicatorColors)
    elif (prefix[2:] in CODE.BATTERIES_LIST[2:4] and moduleTable["button"][1][1:] == CODE.BUTTON_DETONATE):
        pass
    elif moduleTable["button"][1][0:] == CODE.BUTTON_WHITE and prefix[1:2] == CODE.CAR_INDICATOR:
        buttonLogicVariable = random.choice(buttonIndicatorColors)
    elif prefix[2:] == CODE.BATTERIES_3 and prefix[1:2] == CODE.FRK_INDICATOR:
        pass
    elif moduleTable["button"][1][0] == CODE.BUTTON_YELLOW:
        buttonLogicVariable = random.choice(buttonIndicatorColors)
    elif moduleTable["button"][1] == f"{CODE.BUTTON_RED}{CODE.BUTTON_HOLD}":
        pass
    else:
        buttonLogicVariable = random.choice(buttonIndicatorColors)        
    if DEBUG:
        print(buttonLogicVariable)

#   create all the objects
#   (objects go here)


#   starting game loop, handles the main menu
#   when the start button is pressed, switches to the main game loop
screen.blit(classes.startScreen, (0,0))
running = True
while running:
    #   get mouse position
    mouse = pygame.mouse.get_pos()

    #   updates how long the game has been running
    currentTime = pygame.time.get_ticks()

    #   start screen
    if gamestate == "starting":
        #   checks the pygame event stack
        for event in pygame.event.get():
            #   closes the game if the x button is presssed
            if event.type == pygame.QUIT:
                running = False
            #   checks when the mouse is pressed
            if event.type == pygame.MOUSEBUTTONDOWN:
                #   if the mouse is clicked while over the begin button then change gamestate to playing and setup the main window
                if 250 < mouse[0] < 550 and 375 < mouse[1] < 525:
                    gamestate = "playing"
                    startTime = pygame.time.get_ticks()
                    timeLimit += startTime
                    screen.blit(classes.mainScreenBase, (0,0))
                    if moduleTable["button"][0]:
                        buttonRect = screen.blit(classes.buttonBase, moduleTable["button"][4])
                        screen.blit(classes.buttonWord, moduleTable["button"][4])
                    if moduleTable["passwords"][0]:
                        screen.blit(classes.passwordsBase, moduleTable["passwords"][4])
                    if moduleTable["morse"][0]:
                        screen.blit(classes.morseBase, moduleTable["morse"][4])
                    if moduleTable["simon"][0]:
                        screen.blit(classes.simonBase, moduleTable["simon"][4])


    #   main game
    elif gamestate == "playing":

        #   sets time remaining
        timeRemaining = timeLimit - currentTime
        minutesRemaining = str(timeRemaining // 60000)
        secondsRemaining = str((timeRemaining % 60000)//1000)
        if len(secondsRemaining) == 1:
            secondsRemaining = "0" + secondsRemaining
        timerText = classes.timerFont.render(f"{minutesRemaining}:{secondsRemaining}", False, (255, 0, 0))
        screen.blit(classes.strikeList[strikes], timerLocation)
        screen.blit(timerText, (350,80))
        if currentTime >= timeLimit:
            screen.blit(classes.loseScreen, (0,0))
            gamestate = "over"

        #   checks the pygame event stack
        for event in pygame.event.get():
            #   closes the game if the x button is presssed
            if event.type == pygame.QUIT:
                running = False

            #   if the mouse is clicked while over the module
            if event.type == pygame.MOUSEBUTTONDOWN:
                #   button
                if (((200 < mouse[0] < 400) and (200 < mouse[0] < 400)) and (moduleTable["button"][0] == True)):
                    buttonModulePressedStart = pygame.time.get_ticks()

            if event.type == pygame.MOUSEBUTTONUP:
                if (buttonRect.collidepoint(mouse) and buttonModulePressedStart > 0):
                    if DEBUG:
                        active = moduleTable["button"][0]
                        print(f"button module pressed, active={active}")
                    #   finds how long the button was pressed
                    buttonReleasedTime = pygame.time.get_ticks()
                    buttonHeldElapsed = buttonReleasedTime - buttonModulePressedStart
                    #   if the button is completed successfully, its isTheModuleActive value is set to false
                    if buttonLogicVariable == "click" and buttonHeldElapsed <= buttonShortPress:
                        moduleTable["button"][0] = False
                    elif buttonLogicVariable == "yellow" and ("5" in minutesRemaining or "5" in secondsRemaining):
                        moduleTable["button"][0] = False
                    elif buttonLogicVariable == "blue" and ("4" in minutesRemaining or "4" in secondsRemaining):
                        moduleTable["button"][0] = False
                    elif buttonLogicVariable == "white" and ("1" in minutesRemaining or "1" in secondsRemaining):
                        moduleTable["button"][0] = False
                    if DEBUG:
                        active = moduleTable["button"][0]
                        print(f"button module complete, active={active}")
                    #   if the module is still active after all the completion checks, the module is deactivated and a strike is recieved.
                    if moduleTable["button"][0]:
                        moduleTable["button"][0] = False
                        strikes +=1
                    
                    #   checks if the game is over, put this block after every win/loss check
                    result = classes.gameEndCheck(strikes, moduleTable)
                    if DEBUG:
                        print(result)
                    if result == "win":
                        gamestate = "over"
                        screen.blit(classes.winScreen, (0,0))
                    elif result == "lose":
                        gamestate = "over"
                        screen.blit(classes.loseScreen, (0,0))

        

    elif gamestate == "over":
        pass

    clock.tick(60)



    pygame.display.update()
