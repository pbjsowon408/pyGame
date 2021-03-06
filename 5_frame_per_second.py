import pygame

pygame.init()  # initiation

# Setting Screen size
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# Screen Title Setting
pygame.display.set_caption("Python Game")  # Game title

# FPS
clock = pygame.time.Clock()

# get background img
background = pygame.image.load("C:/Programmings/pyGame/background.png")

# get character img
character = pygame.image.load("C:/Programmings/pyGame/character.png")
character_size = character.get_rect().size  # get image size
character_width = character_size[0]  # character width size
character_height = character_size[1]  # character height size
# set character width location in the middle of the screen
character_x_pos = (screen_width / 2) - (character_width / 2)
# set character height location in the botton of the screen
character_y_pos = screen_height - character_height

# coordinates to move
to_x = 0
to_y = 0

# speed rate
character_speed = 0.6

# event Loop
running = True  # Check if the game is running
while running:
    dt = clock.tick(60)  # set frame per second in game screen
    for event in pygame.event.get():  # Which event has been occured
        if event.type == pygame.QUIT:  # Close Screen event is occured
            running = False  # Game not running

        if event.type == pygame.KEYDOWN:  # check if the key is pushed
            if event.key == pygame.K_LEFT:  # move character left
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:  # move character right
                to_x += character_speed
            elif event.key == pygame.K_UP:  # move character up
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:  # move character down
                to_y += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    # weight limit
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # height limit
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    screen.blit(background, (0, 0))  # paint background

    # create character
    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update()  # game background paint again
# pygame quit
pygame.quit()
