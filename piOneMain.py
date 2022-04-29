from sqlite3 import SQLITE_UPDATE
import pygame
import random
import socket
import sys
import os
import RPi.GPIO as GPIO
import codeGenLibrary as CODE
import classes

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

#   constants
#       pi stuff
PIHEIGHT = 800
PIWIDTH = 600

#   start pygame
pygame.init()
 
#   makes the screen 
screen = pygame.display.set_mode((PIHEIGHT, PIWIDTH))

#   window title
pygame.display.set_caption("Keep Talking")

#   variables
gamestate = "starting"
strikes = 0
timerLocation = (250,50)

def strike():
    pass

#   change current working directory to the folder this file is in

#   load the stuff
classes.loadImages()

#   create all the objects
#   (objects go here)


#   starting game loop, handles the main menu
#   when the start button is pressed, switches to the main game loop
screen.blit(classes.startScreen, (0,0))
running = True
while running:
    #   get mouse position
    mouse = pygame.mouse.get_pos()

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
                    screen.blit(classes.mainScreenBase, (0,0))
                    screen.blit(classes.buttonBlue, (200, 200))
                    screen.blit(classes.passwordsBase, (200, 400))


    #   main game
    elif gamestate == "playing":
        #   checks the pygame event stack
        for event in pygame.event.get():
            #   closes the game if the x button is presssed
            if event.type == pygame.QUIT:
                running = False

            #   if the mouse is clicked while over the module
            if event.type == pygame.MOUSEBUTTONDOWN:
                # these variables are not to be used, this is until we have the exact coordiantes
                if 1x1 < mouse[0] < 1x2 and 1y1 < mouse[1] < 1y2:
                    g=0
                if 2x1 < mouse[0] < 2x2 and 2y1 < mouse[1] < 2y2:
                    g=1
                if 3x1 < mouse[0] < 3x2 and 3y1 < mouse[1] < 3y2:
                    g=2
                if 4x1 < mouse[0] < 4x2 and 4y1 < mouse[1] < 4y2:
                    g=3
                if x1 < mouse[0] < x2 and y1 < mouse[1] < y2:
                    pass
                if x1 < mouse[0] < x2 and y1 < mouse[1] < y2:
                    pass
                if True:
                    pass
                if True:
                    pass
                if True:
                    pass
        if strikes == 0:
            screen.blit(classes.timerNoStrikes, timerLocation)
        elif strikes == 1:
            screen.blit(classes.timerOneStrike, timerLocation)
        elif strikes == 2:
            screen.blit(classes.timerTwoStrikes, timerLocation)



    pygame.display.update()
