import random 
import sys 
import pygame 
import threading
from pygame.locals import * 
from bird import *
from pip import *

# Initialise screen
pygame.init()

screen = pygame.display.set_mode((1024, 768)) 
pygame.display.set_caption('Flappy Bird')

# Initialise variables
playing = False
gameOver = False
game = True
clock = pygame.time.Clock()
fps = 60
ground_scroll = 0
scrollSpeed = 2
w, h = pygame.display.get_surface().get_size()
pipeFrequency = 1500
last_pipe = pygame.time.get_ticks()
bird = ''

bird_group = pygame.sprite.Group()
bird = Bird(100, 300)
bird_group.add(bird)

# Fill background
bgImage = pygame.image.load("assets/background.webp")
groundImage = pygame.image.load("assets/ground.png")

# text
RED = (255, 0, 0)
font = pygame.font.SysFont(None, 60)
text = font.render('GAME OVER', True, RED)

#instanciate Pip class
pip_group = pygame.sprite.Group()

#instanciate Button class
def button(screen, position, text):
    font = pygame.font.SysFont("Arial", 50)
    text_render = font.render(text, 1, (255, 0, 0))
    x, y, w , h = text_render.get_rect()
    x, y = position
    pygame.draw.line(screen, (150, 150, 150), (x, y), (x + w , y), 5)
    pygame.draw.line(screen, (150, 150, 150), (x, y - 2), (x, y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x, y + h), (x + w , y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x + w , y+h), [x + w , y], 5)
    pygame.draw.rect(screen, (100, 100, 100), (x, y, w , h))
    return screen.blit(text_render, (x, y))



# Event loop
while game:
    clock.tick(fps)
    screen.blit(bgImage, (0, 0))
    screen.blit(groundImage, (ground_scroll, 0))

    # If game menu 
    if playing == False and gameOver == False:
        b1 = button(screen, (500, 300), "Start")

    # Click events
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == pygame.K_ESCAPE):
            game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird.jump()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if b1.collidepoint(pygame.mouse.get_pos()):
               playing = True
         

    if playing == True:
        gameOver = False

        #draw bird
        bird_group.draw(screen)
        bird_group.update()

        #infinite pipes
        timeNow = pygame.time.get_ticks()
        if(timeNow - last_pipe > pipeFrequency):
            bottom_pip = Pip(w, int(h / 2), 1, scrollSpeed)
            top_pip = Pip(w, int(h / 2), -1, scrollSpeed)
            pip_group.add(bottom_pip, top_pip)
            last_pipe = timeNow
        pip_group.draw(screen)
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
        b1 = button(screen, (500, 300), "Re Start")
        
    pygame.display.update()
    pygame.display.flip()


        

                    

  





