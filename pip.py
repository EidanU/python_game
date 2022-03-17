import pygame
import random
from pygame.locals import * 

# bird class
class Pip(pygame.sprite.Sprite):
    def __init__(self, x, y, position, scrollSpeed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("assets/pip.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = [x, y]
        self.pipGap = random.randrange(65, 120)
        self.scrollSpeed = scrollSpeed
        if position == 1:
            self.rect.topleft = [x, y + int(self.pipGap)]
        if position == -1:
                self.image = pygame.transform.flip(self.image, False, True)
                self.rect.bottomleft = [x, y - int(self.pipGap)]

    def update(self):
        self.rect.x -= self.scrollSpeed
        if self.rect.right < 0:
            self.kill()

     
 

