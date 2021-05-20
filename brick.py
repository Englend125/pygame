# Simple pygame program

# Import and initialize the pygame library
import pygame
pygame.init()

# Set up the drawing window
WIDTH = 600
HEIGHT = 600
screen = pygame.display.set_mode([WIDTH, HEIGHT ])

FPS=60 
clock = pygame.time.Clock()
calor = True
forward = True 

x = 250
y = 250
rad = 30
radcontrol = True

running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    #rad moviment 
    
   

    if rad > 50: 
        rad-- 

    elif rad < 10: 
        rad++

    # motion
    if forward == True:
        x = x + 1
        y = y + 1
    else:
        x = x - 1 
        y = y - 1

    if x >= WIDTH - rad: 
        forward = False 

    elif x <= rad: 
        forward = True  

    if y >= HEIGHT - rad:
        forward = False

    elif y <= rad:
        forward = True     


    pygame.draw.circle(screen, (25, 25, 25), (x, y), rad)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
