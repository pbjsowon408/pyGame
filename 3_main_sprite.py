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

# get character img
character = pygame.image.load("C:/Programmings/pyGame/background.png")
character_size = character.get_rect().size  # get image size
character_width = character_size[0]  # character width size
character_height = character_size[1]  # character height size
# set character width location in the middle of the screen
character_x_pos = (screen_width / 2) - (character_width / 2)
# set character height location in the botton of the screen
character_y_pos = screen_height - character_height


# event Loop
running = True  # Check if the game is running
while running:
    for event in pygame.event.get():  # Which event has been occured
        if event.type == pygame.QUIT:  # Close Screen event is occured
            running = False  # Game not running

    screen.blit(background, (0, 0))  # paint background

    # create character
    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update()  # game background paint again
# pygame quit
pygame.quit()
