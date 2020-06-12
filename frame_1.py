import pygame

pygame.init()  # initiation

# Setting Screen size
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# Screen Title Setting
pygame.display.set_caption("Python Game")  # Game title

# event Loop
running = True  # Check if the game is running
while running:
    for event in pygame.event.get():  # Which event has been occured
        if event.type == pygame.QUIT:  # Close Screen event is occured
            running = False  # Game not

# pygame quit
pygame.quit()
