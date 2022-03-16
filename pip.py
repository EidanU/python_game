import pygame 
from pygame.locals import * 

# bird class
class Pip(pygame.sprite.Sprite):
    def __init__(self, x, y, width, heigth):
        pygame.sprite.Sprite.__init__(self)
        self.positionX = x
        self.positionY = y
        self.allimages = []
        self.index = 0
        self.counter = 0
        self.couldown = 15
        self.velocity = 0
        self.angle = 0
        self.jumping = False
        for i in range(1,4):
            img = pygame.image.load(f"assets/bird{i}.png")
            self.allimages.append(img)
        self.image = self.allimages[self.index]
        self.rect = self.image.get_rect() 
        self.rect.center = [x,y]

        # il faut que la valeur du rotate aille de 0 à 45 degré lorsque l'on saute et qu'à chaque instant elle perde 5 degré jusqu"à atteindre -45
    def update(self):
        self.velocity += 0.5
        self.angle -= 5
        if(self.velocity >= 8):
            self.velocity = 8
        if(self.rect.bottom < 600):
            self.rect.y += self.velocity
        self.counter += 1 
        events = pygame.event.get()
        if(self.counter > self.couldown):
            self.counter = 0
            self.index += 1
            if(self.index >= 3):
                self.index = 0
        self.image = self.allimages[self.index]
 
