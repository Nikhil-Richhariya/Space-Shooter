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

#player Position => the values are tweaked considering the size of image
playerX = 370 #near 400 for middle of window
playerY = 480 #near 500 for lower side in the window

def player() : 
    screen.blit(playerImg, (playerX,playerY))


running = True; 
#Game Loop 
while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            running = False
    
    #RGB
    screen.fill( (0,0,0) )

    #should be called after fill method other wise, player would be below the 
    player()

    pygame.display.update()
