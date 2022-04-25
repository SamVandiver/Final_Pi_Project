import pygame
import os

#   adds a bunch of stuff so vs code doesnt get pissed at me
screen = pygame.display.set_mode((0, 0))
PIHEIGHT = 600
PIWIDTH = 800


#   panel class and its children (obsolete)

class Panel(pygame.sprite.Sprite):
    def __init__(self, width, height, x, y, fillColor):
        super().__init__()

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.fillColor = fillColor

        self.surface = pygame.Surface((self.width, self.height))
        self.surface.fill(self.fillColor)

        self.rect = self.surface.get_rect()
    
    def draw(self):
        screen.blit(self.surface, ((self.x, self.y)))

#   a class (which probably would be better as a bunch of functions) which sets up all the parts of the window which don't need to change every frame
class DisplaySetup:
    def __init__(self) -> None:
        pass


    def startScreen(self):
        screen.fill((100, 100, 100))

    def playingScreen():
        screen.fill((100, 100, 100))
        sidePanel = Panel(250, PIHEIGHT, 0, 0, (60, 60, 60))
        strikePanel = Panel(PIWIDTH, 150, 250, 0, (20,20,20))
        return sidePanel, strikePanel

class Strikes(Panel):
    def __init__(self, strikes):
        super().__init__()
        self.strikes = strikes

    def loadStrikes(self):
        pass

    def addStrike(self):
        pass

#   module class and its children
class Module:

    def __init__(self, id, segment):
        self.id = id
        self.segment = segment

    def change(self):
        pass

    def fail(self):
        raise NotImplementedError

    def draw(self):
        raise NotImplementedError

class Button(Module):
    def __init__(self, id, segment):
        super().__init__(id, segment)


#   functions that dont belong in codeGenLibrary
def loadImages():

    #   get the font
    global font1
    font1 = pygame.font.SysFont

    #   start loading stuff
    os.chdir("assets/screens")
    global startScreen
    global mainScreenBase
    startScreen = pygame.image.load("start screen.png")
    mainScreenBase = pygame.image.load("gui draft1.png")

    #   gets everything from indicators
    os.chdir("../indicator")
    global timerNoStrikes
    global timerOneStrike
    global timerTwoStrikes
    timerNoStrikes = pygame.image.load("timer0.png")
    timerOneStrike = pygame.image.load("timer1.png")
    timerTwoStrikes = pygame.image.load("timer2.png")

    #   gets everything from buttoncolors
    os.chdir("../buttoncolors")
    global buttonBlue
    global buttonWhite
    global buttonYellow
    global buttonRed
    buttonBlue = pygame.image.load("buttonBlue.png")
    buttonWhite = pygame.image.load("buttonWhite.png")
    buttonYellow = pygame.image.load("buttonYellow.png")
    buttonRed = pygame.image.load("buttonRed.png")

    #   gets everything from buttonwords
    os.chdir("../buttonwords")

    #   gets everything from modules/passwords
    os.chdir("../modules/passwords")
    global passwordsBase
    passwordsBase = pygame.image.load("passwords.png")
    
