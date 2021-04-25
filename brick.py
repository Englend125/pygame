# Simple pygame program

# Import and initialize the pygame library
import pygame
pygame.init()

# Set up the drawing window
WIDTH = 500
HEIGHT = 500
screen = pygame.display.set_mode([WIDTH, HEIGHT ])

FPS=60 
clock = pygame.time.Clock()

forward = True
x = 250
y = 250

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
    # Draw a solid blue circle in the center

    # motion
    if forward == True:
        x = x + 5
    else:
        x = x - 5

    if x > WIDTH - 35: 
        forward = False 

    if x < 35: 
        forward = True     

    pygame.draw.circle(screen, (119, 25, 25), (x, y), 35)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()