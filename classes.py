import pygame
#   panel class and its children
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

    def __init__(self):
        pass

    def change(self):
        pass

    def fail(self):
        pass

    def draw(self):
        raise NotImplementedError

class Button(Module):
    def __init__(self, segment):
        super().__init__()
        self.segment = segment