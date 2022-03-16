import random 
import sys 
import pygame 
import threading
from pygame.locals import * 
from bird import *
from pip import *
from button import *

# Initialise screen
pygame.init()

screen = pygame.display.set_mode((1024, 768)) 
pygame.display.set_caption('Flappy Bird')

# Initialise variables
playing = True
gameOver = False
game = True
clock = pygame.time.Clock()
fps = 60
ground_scroll = 0
scrollSpeed = 2
w, h = pygame.display.get_surface().get_size()
pipeFrequency = 1500
last_pipe = pygame.time.get_ticks()

# Fill background
bgImage = pygame.image.load("assets/background.webp")
groundImage = pygame.image.load("assets/ground.png")

# text
RED = (255, 0, 0)
font = pygame.font.SysFont(None, 60)
text = font.render('GAME OVER', True, RED)

# instanciate Bird class
bird_group = pygame.sprite.Group()
bird = Bird(100, 300)
bird_group.add(bird)

#instanciate Pip class
pip_group = pygame.sprite.Group()

#instanciate Button class
button1 = Button(
    "Click here",
    (100, 100),
    bg="navy",
    feedback="You clicked me")

# Event loop
while game:
    clock.tick(fps)
    screen.blit(bgImage, (0, 0))
    screen.blit(groundImage, (ground_scroll, 0))
    bird_group.draw(screen)
    pip_group.draw(screen)
    screen.blit(button1.surface, (200, 200))
    # Click events
    for event in pygame.event.get():
        button1.click(event)
        if event.type == QUIT or (event.type == KEYDOWN and event.key == pygame.K_ESCAPE):
            game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird.jump()

    # if playing == False and gameOver == False:

    if playing == True:
        #draw bird
        bird_group.update()
        #infinite pipes
        timeNow = pygame.time.get_ticks()
        if(timeNow - last_pipe > pipeFrequency):
            bottom_pip = Pip(w, int(h / 2), 1, scrollSpeed)
            top_pip = Pip(w, int(h / 2), -1, scrollSpeed)
            pip_group.add(bottom_pip, top_pip)
            last_pipe = timeNow
        pip_group.update()

        # collisions
        if pygame.sprite.groupcollide(bird_group, pip_group, False, False) or bird.rect.top > 650:
            playing = False
            gameOver = True

        ground_scroll -= scrollSpeed
        if abs(ground_scroll) > 35:
            ground_scroll = 0
                    
    if gameOver == True:
        screen.blit(text,(w/2, h/2))
        
    pygame.display.update()
    pygame.display.flip()


        

                    

  





