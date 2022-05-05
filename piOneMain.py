from re import S
from sqlite3 import SQLITE_UPDATE
import pygame
import random
import socket
import sys
import os
from time import sleep
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

#   code        121.b31.a1111.c.e.f.g.h
#   (example code for now)
code = input("Enter game code:")

#   print cwd for debugging purposes
if DEBUG:
    print(os.getcwd())
    if SAMSPC:
        os.chdir("Final Pi Project\Final_Pi_Project")


#   constants
#       pi stuff
PIHEIGHT = 800
PIWIDTH = 480

#   start pygame
pygame.init()
 
#   makes the screen and clock
screen = pygame.display.set_mode((PIHEIGHT, PIWIDTH))   #   pygame.display.set_mode((PIHEIGHT, PIWIDTH), pygame.FULLSCREEN) for fullscreen
clock = pygame.time.Clock()

#   window title
pygame.display.set_caption("Keep Talking")

#   table for all the stuff about each modules
#       "module" : [isTheModuleActive, codeSegment, solutionList, image, (coordinates)]
moduleTable = {

    "wires"     : [False, None, None, None, None],
    "button"    : [False, None, None, None, (200, 80)],
    "simon"     : [False, None, None, None, (400, 80)],
    "morse"     : [False, None, None, None, (400, 280)],
    "maze"      : [False, None, None, None, (600, 80)],
    "passwords" : [False, None, None, None, (200, 280)],
    "needy"     : [False, None, None, None, (600, 280)]

}

prefix, moduleTable["wires"][1], moduleTable["button"][1], moduleTable["simon"][1], moduleTable["morse"][1], moduleTable["maze"][1], moduleTable["passwords"][1], moduleTable["needy"][1], = CODE.splitCode(code)

print("piOneMain prefix = " + prefix)
#   if splitCode returns a string instead of None, set the module to active
for module in moduleTable:
    if moduleTable[module][1] != None:
        moduleTable[module][0] = True

#   variables
gamestate = "starting"
strikes = 0
timerLocation = (0,0)
timeLimit = 300000    #   5 minutes in miliseconds
startTime = 0         #   updates when the game starts
if moduleTable["button"][0]:
    buttonLogicVariable = "click"  #   is "click" if button must be pressed and immediately released, otherwise is the color of the button indicator strip as a string
    buttonIndicatorColors = ["blue", "white", "yellow"]
    buttonShortPress = 500
if moduleTable["simon"][0]:
    simonInputList = [] #   The list determined by the user that shows their inputs; should end up matching the order list
    simonOrderList = [0, random.randint(1,4)]  #   list that determines the order the Simon module blinks in, must start with 0 to have a blank
    simonSequenceNumber = 0        #   old, new
    simonSetToChange = True        #   variable that prevents lights from flashing during transition

#   load the stuff
classes.loadImages(moduleTable["button"][1], moduleTable["simon"][1], moduleTable["morse"][1], moduleTable["maze"][1], moduleTable["passwords"][1], moduleTable["needy"][1], prefix)

#   get all the rectangles
classes.createRects(moduleTable["simon"][0], moduleTable["morse"][0], moduleTable["maze"][0], moduleTable["passwords"][0], moduleTable["needy"][0], )

#   get all the indicators
serial, indicator, numBatteries = classes.createIndicators(prefix)

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

#   wire logic stuff
if moduleTable["wires"][0]:
    wireLogicVariable = CODE.wiresSolution(moduleTable["wires"][1], prefix)

#   create all the rects
#   (rects go here)
startButtonRect = pygame.Rect(250, 300, 300, 250)


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
                if startButtonRect.collidepoint(mouse):
                    gamestate = "playing"
                    startTime = pygame.time.get_ticks()
                    timeLimit += startTime
                    indicatorText = classes.timerFont.render(indicator, False, (0, 0, 0))
                    serialText = classes.timerFont.render(serial, False, (0, 0, 0))
                    screen.blit(classes.mainScreenBase, (0,0))
                    screen.blit(classes.battery, (600, 0))
                    screen.blit(indicatorText, (80, 410))
                    screen.blit(serialText, (350, 20))
                    if moduleTable["button"][0]:
                        buttonRect = screen.blit(classes.buttonBase, moduleTable["button"][4])
                        screen.blit(classes.buttonWord, moduleTable["button"][4])
                    if moduleTable["passwords"][0]:
                        screen.blit(classes.passwordsBase, moduleTable["passwords"][4])
                    if moduleTable["morse"][0]:
                        screen.blit(classes.morseBase, moduleTable["morse"][4])
                    if moduleTable["simon"][0]:
                        screen.blit(classes.simonBase, moduleTable["simon"][4])
                    if moduleTable["maze"][0]:
                        screen.blit(classes.mazeBase, moduleTable["maze"][4])
                    if moduleTable["needy"][0]:
                        screen.blit(classes.capacitorBase, moduleTable["needy"][4])


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
        screen.blit(timerText, (100,30))
        if currentTime >= timeLimit:
            screen.blit(classes.loseScreen, (0,0))
            gamestate = "over"

        #   blinking stuff
        if int(secondsRemaining) % 2 == 0:
            #   simon blinks
            if moduleTable["simon"][0]:
                if simonSetToChange:
                    if simonSequenceNumber == 0:
                        pass
                    else:
                        classes.simonRectList[simonSequenceNumber] = screen.blit(classes.simonUnlitList[simonOrderList[simonSequenceNumber]], classes.simonCoordsList[simonOrderList[simonSequenceNumber]])
                    simonSequenceNumber += 1
                    simonSequenceNumber %= len(simonOrderList)
                    if simonSequenceNumber == 0:
                        pass
                    else:
                        classes.simonRectList[simonSequenceNumber] = screen.blit(classes.simonLitList[simonOrderList[simonSequenceNumber]], classes.simonCoordsList[simonOrderList[simonSequenceNumber]])
                    simonSetToChange = False
        else:
            if moduleTable["simon"][0]:
                simonSetToChange = True

        #   checks the pygame event stack
        for event in pygame.event.get():
            #   closes the game if the x button is presssed
            if event.type == pygame.QUIT:
                running = False

            #   if the mouse is clicked while over the module
            if event.type == pygame.MOUSEBUTTONDOWN:
                #   button
                if moduleTable["button"][0]:
                    if buttonRect.collidepoint(mouse):
                        buttonModulePressedStart = pygame.time.get_ticks()
                        if buttonLogicVariable == "yellow":
                            pygame.draw.rect(screen, (255, 255, 0), pygame.Rect(365, 245, 28, 28))
                        elif buttonLogicVariable == "blue":
                            pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(365, 245, 28, 28))
                        elif buttonLogicVariable == "white":
                            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(365, 245, 28, 28))
                if moduleTable["morse"][0]:
                    if classes.morseUpRect.collidepoint(mouse):
                        pass
                    if classes.morseTXRect.collidepoint(mouse):
                        pass
                    if classes.morseDownRect.collidepoint(mouse):
                        pass
                if moduleTable["passwords"][0]:
                    if classes.passOneUpRect.collidepoint(mouse):
                        pass
                    if classes.passOneDownRect.collidepoint(mouse):
                        pass
                    if classes.passTwoUpRect.collidepoint(mouse):
                        pass
                    if classes.passTwoDownRect.collidepoint(mouse):
                        pass
                    if classes.passThreeUpRect.collidepoint(mouse):
                        pass
                    if classes.passThreeDownRect.collidepoint(mouse):
                        pass
                    if classes.passFourUpRect.collidepoint(mouse):
                        pass
                    if classes.passFourDownRect.collidepoint(mouse):
                        pass
                if moduleTable["simon"][0]:
                    if ((432 < mouse[0] < 499) and (128 < mouse[1] < 195)):
                        if DEBUG:
                            print(f"clicked blue")
                        simonTranslated = classes.translateSimon(4, strikes, prefix)
                        if DEBUG:
                            print(f"input translated: {simonTranslated}")
                        simonInputList.append(simonTranslated)
                        if DEBUG:
                            print(f"input appended. simonInputList: {simonInputList} simonOrderList: {simonOrderList[1:(len(simonInputList)+1)]}")
                        if simonInputList == simonOrderList[1:(len(simonInputList)+1)]:
                            if len(simonInputList) == 3:
                                moduleTable["simon"][0] = False
                                result = classes.gameEndCheck(strikes, moduleTable)
                                if DEBUG:
                                    print(result)
                                if result == "win":
                                    gamestate = "over"
                                    screen.blit(classes.winScreen, (0,0))
                                elif result == "lose":
                                    gamestate = "over"
                                    screen.blit(classes.loseScreen, (0,0))
                            elif len(simonOrderList) - 1 == len(simonInputList):
                                simonInputList = []
                                simonOrderList.append(random.randint(1,4))
                                if simonOrderList[-1] == simonOrderList[-2]:
                                    simonOrderList[-1] += 1
                                    simonOrderList[-1] %= 5
                            else: 
                                pass
                        else:
                            strikes += 1
                            result = classes.gameEndCheck(strikes, moduleTable)
                            if DEBUG:
                                print(result)
                            if result == "win":
                                gamestate = "over"
                                screen.blit(classes.winScreen, (0,0))
                            elif result == "lose":
                                gamestate = "over"
                                screen.blit(classes.loseScreen, (0,0))
                            simonInputList = []
                    if ((432 < mouse[0] < 499) and (197 < mouse[1] < 264)):
                        if DEBUG:
                            print(f"clicked green")
                        simonTranslated = classes.translateSimon(1, strikes, prefix)
                        if DEBUG:
                            print(f"input translated: {simonTranslated}")
                        simonInputList.append(simonTranslated)
                        if DEBUG:
                            print(f"input appended. simonInputList: {simonInputList} simonOrderList: {simonOrderList[1:(len(simonInputList)+1)]}")
                        if simonInputList == simonOrderList[1:(len(simonInputList)+1)]:
                            if len(simonInputList) == 3:
                                moduleTable["simon"][0] = False
                                result = classes.gameEndCheck(strikes, moduleTable)
                                if DEBUG:
                                    print(result)
                                if result == "win":
                                    gamestate = "over"
                                    screen.blit(classes.winScreen, (0,0))
                                elif result == "lose":
                                    gamestate = "over"
                                    screen.blit(classes.loseScreen, (0,0))
                            elif len(simonOrderList) - 1 == len(simonInputList):
                                simonInputList = []
                                simonOrderList.append(random.randint(1,4))
                                if simonOrderList[-1] == simonOrderList[-2]:
                                    simonOrderList[-1] += 1
                                    simonOrderList[-1] %= 5
                            else: 
                                pass
                        else:
                            strikes += 1
                            result = classes.gameEndCheck(strikes, moduleTable)
                            if DEBUG:
                                print(result)
                            if result == "win":
                                gamestate = "over"
                                screen.blit(classes.winScreen, (0,0))
                            elif result == "lose":
                                gamestate = "over"
                                screen.blit(classes.loseScreen, (0,0))
                            simonInputList = []
                    if ((501 < mouse[0] < 568) and (197 < mouse[1] < 264)):
                        if DEBUG:
                            print(f"clicked red")
                        simonTranslated = classes.translateSimon(2, strikes, prefix)
                        if DEBUG:
                            print(f"input translated: {simonTranslated}")
                        simonInputList.append(simonTranslated)
                        if DEBUG:
                            print(f"input appended. simonInputList: {simonInputList} simonOrderList: {simonOrderList[1:(len(simonInputList)+1)]}")
                        if simonInputList == simonOrderList[1:(len(simonInputList)+1)]:
                            if len(simonInputList) == 3:
                                moduleTable["simon"][0] = False
                                result = classes.gameEndCheck(strikes, moduleTable)
                                if DEBUG:
                                    print(result)
                                if result == "win":
                                    gamestate = "over"
                                    screen.blit(classes.winScreen, (0,0))
                                elif result == "lose":
                                    gamestate = "over"
                                    screen.blit(classes.loseScreen, (0,0))
                            elif len(simonOrderList) - 1 == len(simonInputList):
                                simonInputList = []
                                simonOrderList.append(random.randint(1,4))
                                if simonOrderList[-1] == simonOrderList[-2]:
                                    simonOrderList[-1] += 1
                                    simonOrderList[-1] %= 5
                            else: 
                                pass
                        else:
                            strikes += 1
                            result = classes.gameEndCheck(strikes, moduleTable)
                            if DEBUG:
                                print(result)
                            if result == "win":
                                gamestate = "over"
                                screen.blit(classes.winScreen, (0,0))
                            elif result == "lose":
                                gamestate = "over"
                                screen.blit(classes.loseScreen, (0,0))
                            simonInputList = []
                    if ((501 < mouse[0] < 568) and (128 < mouse[1] < 195)):
                        if DEBUG:
                            print(f"clicked yellow")
                        simonTranslated = classes.translateSimon(3, strikes, prefix)
                        if DEBUG:
                            print(f"input translated: {simonTranslated}")
                        simonInputList.append(simonTranslated)
                        if DEBUG:
                            print(f"input appended. simonInputList: {simonInputList} simonOrderList: {simonOrderList[1:(len(simonInputList)+1)]}")
                        if simonInputList == simonOrderList[1:(len(simonInputList)+1)]:
                            if len(simonInputList) == 3:
                                moduleTable["simon"][0] = False
                                result = classes.gameEndCheck(strikes, moduleTable)
                                if DEBUG:
                                    print(result)
                                if result == "win":
                                    gamestate = "over"
                                    screen.blit(classes.winScreen, (0,0))
                                elif result == "lose":
                                    gamestate = "over"
                                    screen.blit(classes.loseScreen, (0,0))
                            elif len(simonOrderList) - 1 == len(simonInputList):
                                simonInputList = []
                                simonOrderList.append(random.randint(1,4))
                                if simonOrderList[-1] == simonOrderList[-2]:
                                    simonOrderList[-1] += 1
                                    simonOrderList[-1] %= 5
                            else: 
                                pass
                        else:
                            strikes += 1
                            result = classes.gameEndCheck(strikes, moduleTable)
                            if DEBUG:
                                print(result)
                            if result == "win":
                                gamestate = "over"
                                screen.blit(classes.winScreen, (0,0))
                            elif result == "lose":
                                gamestate = "over"
                                screen.blit(classes.loseScreen, (0,0))
                            simonInputList = []
                if moduleTable["maze"][0]:
                    if classes.mazeUpRect.collidepoint(mouse):
                        pass
                    if classes.mazeDownRect.collidepoint(mouse):
                        pass
                    if classes.mazeLeftRect.collidepoint(mouse):
                        pass
                    if classes.mazeRightRect.collidepoint(mouse):
                        pass
                if moduleTable["needy"][0]:
                    if classes.needyDischargeRect.collidepoint(mouse):
                        pass

            if event.type == pygame.MOUSEBUTTONUP:
                if moduleTable["button"][0]:
                    if (buttonRect.collidepoint(mouse) and buttonModulePressedStart > 0):
                        #   finds how long the button was pressed
                        buttonReleasedTime = pygame.time.get_ticks()
                        buttonHeldElapsed = buttonReleasedTime - buttonModulePressedStart
                        if DEBUG:
                            active = moduleTable["button"][0]
                            print(f"buttonElapsedTime = {buttonHeldElapsed}, buttonActive = {active}")
                        #   if the button is completed successfully, its isTheModuleActive value is set to false
                        if ((buttonLogicVariable == "click") and (buttonHeldElapsed <= buttonShortPress)):
                            if DEBUG:
                                print('"click" detected')
                            moduleTable["button"][0] = False
                        elif (((buttonLogicVariable == "yellow") and (("5" in minutesRemaining) or ("5" in secondsRemaining))) and (buttonHeldElapsed >= buttonShortPress)):
                            moduleTable["button"][0] = False
                        elif (((buttonLogicVariable == "blue") and (("4" in minutesRemaining) or ("4" in secondsRemaining))) and (buttonHeldElapsed >= buttonShortPress)):
                            moduleTable["button"][0] = False
                        elif (((buttonLogicVariable == "white") and (("1" in minutesRemaining) or ("1" in secondsRemaining))) and (buttonHeldElapsed >= buttonShortPress)):
                            moduleTable["button"][0] = False
                        if DEBUG:
                            active = moduleTable["button"][0]
                            print(f"button module complete, active={active}")
                        #   if the module is still active after all the completion checks, the module is deactivated and a strike is recieved.
                        if moduleTable["button"][0]:
                            # moduleTable["button"][0] = False
                            strikes += 1

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
