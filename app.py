import random 
import sys 
import pygame 
import threading
from pygame.locals import * 
from bird import *
from pip import *


# Initialise screen
pygame.init()

clock = pygame.time.Clock()
fps = 60
screen = pygame.display.set_mode((1024, 768)) 
pygame.display.set_caption('Flappy Bird')
w, h = pygame.display.get_surface().get_size()
pipeFrequency = 1500

class FlappyBird():
        def __init__(self):

            # Initialise variables
            self.playing = False
            self.gameOver = False
            self.game = True
            self.ground_scroll = 0
            self.scrollSpeed = 2
            self.last_pipe = pygame.time.get_ticks()

            # Fill background
            self.bgImage = pygame.image.load("assets/background.webp")
            self.groundImage = pygame.image.load("assets/ground.png")

            # text
            RED = (255, 0, 0)
            self.font = pygame.font.SysFont(None, 60)
            self.text = self.font.render('GAME OVER', True, RED)

            #Create Start and restart button
        def button(self,screen, position, text):
            text_render = self.font.render(text, 1, (0, 0, 0))
            x, y, w , h = text_render.get_rect()
            x, y = position
            # pygame.draw.line(screen, (150, 150, 150), (x, y), (x + w , y), 5)
            # pygame.draw.line(screen, (150, 150, 150), (x, y - 2), (x, y + h), 5)
            # pygame.draw.line(screen, (50, 50, 50), (x, y + h), (x + w , y + h), 5)
            # pygame.draw.line(screen, (50, 50, 50), (x + w , y+h), [x + w , y], 5)
            pygame.draw.rect(screen, (100, 100, 100), (x, y, w , h))
            return screen.blit(text_render, (x, y))
    
        def start(self):
            # instanciate Bird
            self.bird_group = pygame.sprite.Group()
            self.bird = Bird(100, 300)
            self.bird_group.add(self.bird)

            # instanciate Pip 
            self.pip_group = pygame.sprite.Group()

            self.playing = True

        # def gameOver(self):


flappyBird=FlappyBird()
# Event loop
while flappyBird.game:
    clock.tick(fps)
    screen.blit(flappyBird.bgImage, (0, 0))
    screen.blit(flappyBird.groundImage, (flappyBird.ground_scroll, 0))

    # If game menu 
    if flappyBird.playing == False and flappyBird.gameOver == False:
        b1 = flappyBird.button(screen, (500, 300), "Start")

    # Click events
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == pygame.K_ESCAPE):
            flappyBird.game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                flappyBird.bird.jump()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if b1.collidepoint(pygame.mouse.get_pos()):
               flappyBird.start()
         

    if flappyBird.playing == True:
        flappyBird.gameOver = False

        # Draw bird
        flappyBird.bird_group.draw(screen)
        flappyBird.bird_group.update()

        # Infinite pipes
        timeNow = pygame.time.get_ticks()
        if(timeNow - flappyBird.last_pipe > pipeFrequency):
            bottom_pip = Pip(w, int(h / 2), 1, flappyBird.scrollSpeed)
            top_pip = Pip(w, int(h / 2), -1, flappyBird.scrollSpeed)
            flappyBird.pip_group.add(bottom_pip, top_pip)
            flappyBird.last_pipe = timeNow
        flappyBird.pip_group.draw(screen)
        flappyBird.pip_group.update()

        # Collisions
        if pygame.sprite.groupcollide(flappyBird.bird_group, flappyBird.pip_group, False, False) or flappyBird.bird.rect.top > 650:
            flappyBird.playing = False
            flappyBird.gameOver = True

        flappyBird.ground_scroll -= flappyBird.scrollSpeed
        if abs(flappyBird.ground_scroll) > 35:
            flappyBird.ground_scroll = 0

    # Game Over       
    if flappyBird.gameOver == True:
        screen.blit(flappyBird.text,(w/2, h/2))
        b1 = flappyBird.button(screen, (500, 300), "Re Start")
        
    pygame.display.update()
    pygame.display.flip()


        

                    







