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

# Run until the user asks to quit
running = True
while running:
    clock.tick(FPS)

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    #rad moviment 
    
    if radcontrol == True:
        rad = rad + 1
    else: 
        rad = rad - 1

    if rad > 50: 
        radcontrol = False 

    if rad < 10: 
        radcontrol = True 

    # motion
    if forward == True:
        x = x + 1
        y = y + 1
    else:
        x = x - 1 
        y = y - 1

    if x >= WIDTH - rad: 
        forward = False 

    if x <= rad: 
        forward = True  

    if y >= HEIGHT - rad:
        forward = False

    if y <= rad:
        forward = True     

    # if keystate [pygame.K_SPACE]: 
    #     rad = rad + 1 
    # else: 
    #     rad =rad - 1    


    pygame.draw.circle(screen, (0, 25, 0), (x, y), rad)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()