import random 
import sys 
import pygame 
from pygame.locals import * 


# bird class
class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.allimages = []
        self.index = 0
        self.counter = 0
        self.couldown = 15
        for i in range(1,4):
            img = pygame.image.load(f"assets/bird{i}.png")
            self.allimages.append(img)
        self.image = self.allimages[self.index]
        self.rect = self.image.get_rect() 
        self.rect.center = [x,y]
    def update(self):
        self.counter += 1
        if(self.counter > self.couldown):
            self.counter = 0
            self.index += 1
            if(self.index >= 3):
                self.index = 0
        self.image = self.allimages[self.index]

        



bird_group = pygame.sprite.Group()
bird = Bird(100, 300)
bird_group.add(bird)

    
#         self.image = pygame.Surface([width, height]) 
#         self.image.fill(color) 
#         # self.image.set_colorkey() 
#         pygame.draw.rect(self.image, color, [0, 0, width, height]) 


    # color = (255,255,255) 
    # birdPosition = (300, 500) 
    # bird.fill(color)
    # bird = pygame.image.load('assets/bird.png')
    # bird = pygame.display.set_mode((30,30))

# Initialise screen
pygame.init()

screen = pygame.display.set_mode((1024, 768)) 
pygame.display.set_caption('Flappy Bird')

clock = pygame.time.Clock()
fps = 30
ground_scroll = 0
scrollSpeed = 2

# Fill background
bgImage = pygame.image.load("assets/background.webp")
groundImage = pygame.image.load("assets/ground.png")

# background = pygame.Surface(screen.get_size())

#bird sprite
# bird = Bird((255,255,255), 30, 30 )
# bird.rect.x = 200
# bird.rect.y = 300

#All sprite
# all_sprites = pygame.sprite.Group()
# all_sprites.add(bird)
# all_sprites.add(background)

# Blit everything to the screen
# for entity in all_sprites:
#     screen.blit(entity.player, entity.background)
# pygame.display.flip()

# Event loop
continuer = True
while continuer:
    clock.tick(fps)
    screen.blit(bgImage, (0, 0))
    bird_group.draw(screen)
    bird_group.update()
    screen.blit(groundImage, (ground_scroll, 0))
    ground_scroll -= scrollSpeed
    
    if abs(ground_scroll) > 35:
        ground_scroll = 0
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == pygame.K_ESCAPE):
            continuer = 0
    pygame.display.update()
    pygame.display.flip()
                    

  





