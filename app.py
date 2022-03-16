import random 
import sys 
import pygame 
from pygame.locals import * 
from bird import *

# Initialise screen
pygame.init()

screen = pygame.display.set_mode((1024, 768)) 
pygame.display.set_caption('Flappy Bird')

# Initialise variables
start = False
end = False
game = True
clock = pygame.time.Clock()
fps = 60
ground_scroll = 0
scrollSpeed = 2


# Fill background
bgImage = pygame.image.load("assets/background.webp")
groundImage = pygame.image.load("assets/ground.png")

# text
RED = (255, 0, 0)
font = pygame.font.SysFont(None, 60)
text = font.render('FLAPPY FUCKING BIRD', True, RED)

# instanciate Bird class
bird_group = pygame.sprite.Group()
bird = Bird(100, 300)
bird_group.add(bird)

# Event loop
while game:
    clock.tick(fps)
    screen.blit(bgImage, (0, 0))
    screen.blit(text, (200, 200))
    # if(start == True):
    bird_group.draw(screen)
    bird_group.update()
    screen.blit(groundImage, (ground_scroll, 0))
    ground_scroll -= scrollSpeed
    if abs(ground_scroll) > 35:
        ground_scroll = 0
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == pygame.K_ESCAPE):
            game = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                bird.jump()
                
    pygame.display.update()
    pygame.display.flip()
    # elif(end == True):
    screen.blit(text, (200, 200))

        

                    

  





