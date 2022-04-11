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

running = True

#   change current working directory to the folder this file is in
os.chdir("Final Pi Project/Final_Pi_Project/assets/buttoncolors")

#   images
#       button backgrounds
buttonBlue = pygame.image.load("buttonBlue.png")
buttonWhite = pygame.image.load("buttonWhite.png")
buttonYellow = pygame.image.load("buttonYellow.png")
buttonRed = pygame.image.load("buttonRed.png")

os.chdir("../buttonwords")
#       button text
abortWhite = pygame.image.load("abortWhite.png")


#   module functions
def button(buttonBackground, buttonText, x, y):
    screen.blit(buttonBackground, (x, y))
    screen.blit(buttonText, (x, y))


#   create all the objects
sidePanel = classes.Panel(250, PIHEIGHT, 0, 0, (60, 60, 60))
strikePanel = classes.Panel(PIWIDTH, 200, 250, 0, (20,20,20))


while running:

#      events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.fill((100,100,100))
    button(buttonBlue, abortWhite, 450, 200)
    sidePanel.draw()
    strikePanel.draw()
    pygame.display.update()
