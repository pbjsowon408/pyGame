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

# Enemy character
enemy = pygame.image.load("C:/Programmings/pyGame/enemy.png")
enemy_size = enemy.get_rect().size  # get image size
enemy_width = enemy_size[0]  # enemy width size
enemy_height = enemy_size[1]  # enemy height size
# set enemy width location in the middle of the screen
enemy_x_pos = (screen_width / 2) - (enemy_width / 2)
# set enemy height location in the botton of the screen
enemy_y_pos = (screen_height / 2) - (enemy_height / 2)

# Font Definition
game_font = pygame.font.Font(None, 40)  # Create Font object (Font, Size)

# Total time
total_time = 10

# Calculate start time
start_ticks = pygame.time.get_ticks()  # get start time

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

    # update rect info to deal with collision
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # Check collision
    if character_rect.colliderect(enemy_rect):
        print("Collide!!")
        running = False

    screen.blit(background, (0, 0))  # paint background
    # create character
    screen.blit(character, (character_x_pos, character_y_pos))
    # create enemy
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))
    # Timer
    # Calculate running time
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    # divide elapsed time (ms) into 1000 to show as second (s)

    timer = game_font.render(
        str(int(total_time - elapsed_time)), True, (255, 255, 255))
    # render( Output word, Antialias = True , Color)
    screen.blit(timer, (240, 20))

    # If the Timer is lower than 0, Close the screen
    if total_time - elapsed_time <= 0:
        print("Time Over")
        running = False

    pygame.display.update()  # game background paint again

# Standby
pygame.time.delay(1000)  # 2seconds delay


# pygame quit
pygame.quit()
