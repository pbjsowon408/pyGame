import pygame
import random
##############################################################

# Basic initiallize part (Must)
pygame.init()  # initiation

# Setting Screen size
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# Screen Title Setting
pygame.display.set_caption("Python Game")  # Game title

# FPS
clock = pygame.time.Clock()
##############################################################

# 1. Initaillize User Game (Background, Image, Coordinates, Speed, Font, etc.)
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
enemy_x_pos = random.randint(0, (screen_width - enemy_width))
# set enemy height location in the botton of the screen
enemy_y_pos = 0
enemy_speed = 12

# 3. Define Game Character location
running = True
while running:
    dt = clock.tick(90)
    # 2. Deal with Event (Keyboard, Mouse, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:  # check if the key is pushed
            if event.key == pygame.K_LEFT:  # move character left
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:  # move character right
                to_x += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    # weight limit
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    enemy_y_pos += enemy_speed

    if enemy_y_pos > screen_height:
        enemy_y_pos = 0
        enemy_x_pos = random.randint(0, (screen_width - enemy_width))
        # height limit
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height
    # 4. Deal with Collision
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
# 5. Draw on a Screen
    screen.blit(background, (0, 0))  # paint background
    # create character
    screen.blit(character, (character_x_pos, character_y_pos))
    # create enemy
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))


##############################################################
    pygame.display.update()

pygame.quit()
