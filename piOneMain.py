from sqlite3 import SQLITE_UPDATE
import pygame
import random
import socket
import sys
import codeGenLibrary as CODE
import os
import RPi.GPIO as GPIO
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
                #   if the mouse is clicked while over the module
                if x1 < mouse[0] < x2 and y1 < mouse[1] < y2:
                    # This is an infinite sequence length but obviously we can fix it to a predetermined length.
                    '''
                    s=[]
                    for i in simonLen:
                        r=randint(0,3)
                        s.append(r)
                        print(s)
                        g=input('Choose "1-4" and remember the sequence.\n')
                        if g!=s[i]:
                            break
                    '''
                        # Some sort of clearing mechanic so the player can't see the previous outcome
                        # Additionally they will actually be playing with buttons and lights so this will be obsolete
                if x1 < mouse[0] < x2 and y1 < mouse[1] < y2:
                    '''
                    st=0
                    code='whatever is randomly assigned'
                    MC={'A':'.-',      'B':'-...',
                        'C':'-.-.',    'D':'-..',
                        'E':'.',       'F':'..-.',
                        'G':'--.',     'H':'....',
                        'I':'..',      'J':'.---',
                        'K':'-.-',     'L':'.-..',
                        'M':'--',      'N':'-.',
                        'O':'---',     'P':'.--.',
                        'Q':'--.-',    'R':'.-.',
                        'S':'...',     'T':'-',
                        'U':'..-',     'V':'...-',
                        'W':'.--',     'X':'-..-',
                        'Y':'-.--',    'Z':'--..',
                        '1':'.----',   '2':'..---',
                        '3':'...--',   '4':'....-',
                        '5':'.....',   '6':'-....',
                        '7':'--...',   '8':'---..',
                        '9':'----.',   '0':'-----',
                        ', ':'--..--', '.':'.-.-.-',
                        '?':'..--..',  '/':'-..-.',
                        '-':'-....-',  '(':'-.--.',
                        ')':'-.--.-'}
                    # Function to encrypt the string according to the morse code chart
                    def encrypt(message):
                        C=''
                        for character in message:
                            # Looks up the dictionary and adds the correspponding morse code along with a space to separate morse codes for different characters
                            if character!=' ': C+=MC[character]+' '
                            # 1 space indicates different characters and 2 indicates different words
                            else: C+=' '
                        return C
                    guess=encrypt(message)
                    while True:
                        pin=input('What is the code?')
                        if guess!=code:
                            st+1
                            if st==2:
                                print('You lose!')
                                quit()
                            else: print('Be careful... 1 attempt left')
                        else:
                            print('Great work you did it!')
                            break
                    '''
                if x1 < mouse[0] < x2 and y1 < mouse[1] < y2:
                    '''
                    st=0
                    W=[]
                    TF=[True,False]
                    WC=['1','2','3','4']
                    for _ in 'wire': # Needs to happen 4 times 'wire' was just a coincidence
                        w=choice(TF) # Sometimes all 4 wires are randomly False and causes you to win instantly, of course in the game this wouldn't be random
                        W.append(w)
                    while True in W: # Keeps looping while a "True" value wire is present
                        print(f'Pick a wire to pull...\n{WC}')
                        turn=int(input(f'{W}\n')) # Just for testing, normally the player would have to use the manual to get the right wire
                        turn-=1 # Because indexing starts at 0
                        if W[turn]==False:
                            st+=1
                            if st==2:
                                print('You lose!')
                                quit()
                            else: print('First strike... be careful.')
                        else: print('Good job.')
                        W.pop(turn)
                        WC.pop(turn)
                    print('Congratulations you have succesfully unplugged the correct wires.')
                    return W
                    '''
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
