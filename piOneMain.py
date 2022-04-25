from sqlite3 import SQLITE_UPDATE
import pygame
import random
import socket
import sys
import codeGenLibrary as CODE
import os
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

            if event.type == pygame.MOUSEBUTTONDOWN:
                #   if the mouse is clicked while over the
                if x1 < mouse[0] < x2 and y1 < mouse[1] < y2:
                    gamestate = "playing"
                    screen.blit(classes.mainScreenBase, (0,0))
                    screen.blit(classes.'something', (x, y))
                    screen.blit(classes.'something', (x, y))
                if True:
                    pass
                if True:
                    pass
                if True:
                    pass
                if True:
                    pass
                if True:
                    pass
        if strikes == 0:
            screen.blit(classes.timerNoStrikes, timerLocation)


        
                
    pygame.display.update()
