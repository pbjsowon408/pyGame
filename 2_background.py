import pygame

pygame.init()  # initiation

# Setting Screen size
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# Screen Title Setting
pygame.display.set_caption("Python Game")  # Game title

# get background img
background = pygame.image.load("file location")

# event Loop
running = True  # Check if the game is running
while running:
    for event in pygame.event.get():  # Which event has been occured
        if event.type == pygame.QUIT:  # Close Screen event is occured
            running = False  # Game not running

    screen.blit(background, (0, 0))  # paint background

    pygame.display.update()  # game background paint again
# pygame quit
pygame.quit()
