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

starting = True
playing = False
gameover = False

#   change current working directory to the folder this file is in
os.chdir("assets/buttoncolors")

#   images
#       button backgrounds
buttonBlue = pygame.image.load("buttonBlue.png")
buttonWhite = pygame.image.load("buttonWhite.png")
buttonYellow = pygame.image.load("buttonYellow.png")
buttonRed = pygame.image.load("buttonRed.png")

os.chdir("../buttonwords")
#       button text
abortWhite = pygame.image.load("abortWhite.png")

os.chdir("../indicator")

indicator = pygame.image.load("indicatorbase.png")
def drawindicator(image, x, y):
    screen.blit(image, (x, y))


#   module functions
def button(buttonBackground, buttonText, x, y):
    screen.blit(buttonBackground, (x, y))
    screen.blit(buttonText, (x, y))


#   create all the objects

#   (objects go here)


#   starting game loop, handles the main menu
#   when the start button is pressed, switches to the main game loop
while starting:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            starting = False
            playing = True
    
    screen.fill((100,100,100))
    button(buttonBlue, abortWhite, 450, 200)
    pygame.display.update()

#   Classes.DisplaySetup.playingScreen() as of now returns two objects (which at this point are obsolete)
#   proly need to make this function set the background to the base image
sidePanel, strikePanel = classes.DisplaySetup.playingScreen()


#   main game loop, handles the main game and terinates when the player wins or loses by having 3 strikes
while playing:

#      events
    for event in pygame.event.get():
        #   terminates the gameloop if the x button is pressed
        if event.type == pygame.QUIT:
            playing = False

    #   makes the background gray
    screen.fill((100,100,100))
    #   adds a blue abort button
    button(buttonBlue, abortWhite, 450, 200)
    #   draws the two obsolete things from classes.DisplaySetup.playingScreen()
    sidePanel.draw()
    strikePanel.draw()
    pygame.display.update()
