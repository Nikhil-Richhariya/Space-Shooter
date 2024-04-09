import pygame

#initialized the pygame 
pygame.init()

#creating the screen 
screen = pygame.display.set_mode( (800,600) )

#Title 
pygame.display.set_caption("Space Invaders")

#Icon
icon = pygame.image.load("Resources/spaceship.png")
pygame.display.set_icon(icon)

#player
playerImg = pygame.image.load("Resources/player.png")

#player Position
playerX = 400
playerY = 500

running = True; 
#Game Loop 
while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            running = False
    
    #RGB
    screen.fill( (255,5,255) )
    pygame.display.update()
