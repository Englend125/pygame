# Simple pygame program

# Import and initialize the pygame library
import pygame 
from random import randint
pygame.init()

# Set up the drawing window
WIDTH = 600
HEIGHT = 600
screen = pygame.display.set_mode([WIDTH, HEIGHT ])
s = pygame.mixer.Sound('boom.mp3')
FPS = 60 
A = True
clock = pygame.time.Clock()
Dx = - 1
Dy = 3
run = True
r = 1
g = 1
b = 1
x = 250
y = 250
rad = 30

# Run until the user asks to quit
while run :
    clock.tick(FPS)

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    # motion
    if A == True: 
       x = x + Dx
       y = y + Dy
    else:
       x = x
       y = y

    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
       A = False

    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
       A = True

    if x >= WIDTH - rad - 10:
        s.play()
        Dx = - 1
        print('boom')
        r = randint(0,255)
        g = randint(0,255)
        b = randint(0,255)
        
    if x <= rad + 10: 
        s.play()
        Dx = 1 
        print('boom')
        r = randint(0,255)
        g = randint(0,255)
        b = randint(0,255)

    if y >= HEIGHT - rad - 10:
        s.play()
        Dy = - 3
        print('boom')
        r = randint(0,255)
        g = randint(0,255)
        b = randint(0,255)
        
    if y <= rad + 10:
        s.play()
        Dy =  3  
        print('boom')
        r = randint(0,255)
        g = randint(0,255)
        b = randint(0,255)


    pygame.draw.circle(screen, (r, g, b), (x, y), rad)

    pygame.draw.line( screen, (100, 50, 250), [0, 0], [0, WIDTH], 15)

    pygame.draw.line( screen, (100, 50, 250), [0, WIDTH], [WIDTH, HEIGHT], 15)

    pygame.draw.line( screen, (100, 50, 250), [WIDTH, HEIGHT], [HEIGHT, 0 ], 15)

    pygame.draw.line( screen, (100, 50, 250), [HEIGHT, 0], [0, 0 ], 15)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
