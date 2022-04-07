import pygame
import random
import socket
import sys
import codeGenLibrary as CODE
import os

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
os.chdir("Final Pi Project/Final_Pi_Project")

#   images
buttonBlue = pygame.image.load("buttonBlue.png")
# buttonWhite = pygame.image.load("buttonWhite.png")
# buttonYellow = pygame.image.load("buttonYellow.png")
# buttonRed = pygame.image.load("buttonRed.png")


#   module functions
def button(buttonBackground, buttonText):
    screen.blit(buttonBackground, (300, 400))

while running:

#      events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.fill((100,100,100))
    button(buttonBlue, 0)
    pygame.display.update()
