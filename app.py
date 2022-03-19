import pygame 
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
pipeFrequency = 2000

# FlappyBird class to handle start start and stop 
class FlappyBird():
        def __init__(self):

            # Initialise variables
            self.playing = False
            self.gameOver = False
            self.game = True
            self.groundScroll = 0
            self.scrollSpeed = 2
            self.lastPipe = pygame.time.get_ticks()

            # Fill background
            self.bgImage = pygame.image.load("assets/background.webp")
            self.groundImage = pygame.image.load("assets/ground.png")

            # text
            RED = (255, 0, 0)
            self.font = pygame.font.SysFont(None, 60)
            self.text = self.font.render('GAME OVER', True, RED)

            # Create Start and restart button
        def button(self,screen, position, text):
            textRender = self.font.render(text, 1, (255, 255, 255))
            textWidth, textHeight = self.font.size(text)
            x, y = position
            pygame.draw.rect(screen, (0, 0, 0), (x/2-textWidth, y/2-textHeight, textWidth*2 , textHeight*2))
            return screen.blit(textRender, ((x-textWidth)/2, (y-textHeight)/2))
    
        def start(self):
            # instanciate Bird and Pip classes
            self.birdGroup = pygame.sprite.Group()
            self.bird = Bird(100, 300)
            self.birdGroup.add(self.bird)
            self.pipGroup = pygame.sprite.Group()
            self.playing = True

flappyBird=FlappyBird()

# Game loop
while flappyBird.game:
    clock.tick(fps)
    screen.blit(flappyBird.bgImage, (0, 0))
    screen.blit(flappyBird.groundImage, (flappyBird.groundScroll, 0))

    # Menu before clicking on start 
    if flappyBird.playing == False and flappyBird.gameOver == False:
        b1 = flappyBird.button(screen, (w, h), "Start")

    # Click events
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == pygame.K_ESCAPE):
            flappyBird.game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if flappyBird.playing == True:
                    flappyBird.bird.jump()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if b1.collidepoint(pygame.mouse.get_pos()):
               flappyBird.start()
         
    if flappyBird.playing == True:
        flappyBird.gameOver = False

        # Draw bird
        flappyBird.birdGroup.draw(screen)
        flappyBird.birdGroup.update()

        # Generate Infinite pipes
        timeNow = pygame.time.get_ticks()
        if(timeNow - flappyBird.lastPipe > pipeFrequency):
            bottom_pip = Pip(w, int(h / 2), 1, flappyBird.scrollSpeed)
            top_pip = Pip(w, int(h / 2), -1, flappyBird.scrollSpeed)
            flappyBird.pipGroup.add(bottom_pip, top_pip)
            flappyBird.lastPipe = timeNow
        flappyBird.pipGroup.draw(screen)
        flappyBird.pipGroup.update()

        # Handle Collisions
        if pygame.sprite.groupcollide(flappyBird.birdGroup, flappyBird.pipGroup, False, False) or flappyBird.bird.rect.top > 650:
            flappyBird.playing = False
            flappyBird.gameOver = True

        flappyBird.groundScroll -= flappyBird.scrollSpeed
        if abs(flappyBird.groundScroll) > 35:
            flappyBird.groundScroll = 0

    # Game Over       
    if flappyBird.gameOver == True:
        b1 = flappyBird.button(screen, (w, h), "Restart")
        
    pygame.display.update()
    pygame.display.flip()


        

                    







