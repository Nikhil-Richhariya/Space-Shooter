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

changeInX = 0

speed = 0.1 # => control speed of movement

def player(x,y): 
    screen.blit(playerImg, (x,y))

def movePlayerLeft():
    global playerX
    playerX = ( playerX - 0.1 ) % 800
def movePlayerRight():
    global playerX
    playerX = ( playerX + 0.1 ) % 800




running = True; 
#Game Loop 

while running: 

    #RGB
    screen.fill( (0,0,0) )
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            running = False
    
        # if keystroke is pressed check wheater its right or left
        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_a or event.key == pygame.K_LEFT ):
                changeInX = -speed #decrement the value of x  
            elif (event.key == pygame.K_d or event.key == pygame.K_RIGHT) :
                changeInX = speed #increment the value of Y
        
        #if keystroke is released 
        if event.type == pygame.KEYUP:
            if(event.key == pygame.K_a or event.key == pygame.K_LEFT or
               event.key == pygame.K_d or event.key == pygame.K_RIGHT ):
                changeInX = 0


    #updating the value of playerX 
    playerX += changeInX
    playerX %= 800

    #should be called after fill method other wise, player would be below the 
    player(playerX,playerY)

    pygame.display.update()
