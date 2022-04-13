import pygame
#   panel class and its children

screen = pygame.display.set_mode((0, 0))
PIHEIGHT = 600
PIWIDTH = 800

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