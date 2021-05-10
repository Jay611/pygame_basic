import pygame
import random
import os
#####################################################################
# Initialization
pygame.init()

# Screen size
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# Screen title
pygame.display.set_caption("Pang Pang")

# FPS
clock = pygame.time.Clock()
#####################################################################

# Load background image
current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, 'images')

background = pygame.image.load(os.path.join(image_path, 'background.png'))

# Create stage
stage = pygame.image.load(os.path.join(image_path, 'stage.png'))
stage_size = stage.get_rect().size
stage_height = stage_size[1]

# Create character
character = pygame.image.load(os.path.join(image_path, 'character.png'))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width - character_width) / 2
character_y_pos = screen_height - character_height - stage_height

# Character movement
character_to_x = 0

# Character speed
character_speed = 0.5

# Create weapon
weapon = pygame.image.load(os.path.join(image_path, 'weapon.png'))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]

weapons = []
weapon_speed = 1

# Create balloon
ball_images = [
    pygame.image.load(os.path.join(image_path, 'balloon1.png')),
    pygame.image.load(os.path.join(image_path, 'balloon2.png')),
    pygame.image.load(os.path.join(image_path, 'balloon3.png')),
    pygame.image.load(os.path.join(image_path, 'balloon4.png'))
]

# Ball speed
ball_speed_y = [-18, -15, -12, -9]

balls = []

balls.append({
    'pos_x': 50,
    'pos_y': 50,
    'img_idx': 0,
    'to_x': 3,
    'to_y': -6,
    'init_spd_y': ball_speed_y[0]
})



# Event loop
running = True
while running:
    dt = clock.tick(60) # The number of frames per second
    
    for event in pygame.event.get():  # Check event
        if event.type == pygame.QUIT: # Close window?
            running = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                character_to_x += character_speed
            elif event.key == pygame.K_SPACE:
                weapon_x_pos = character_x_pos + character_width / 2 - weapon_width / 2
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos])
        
        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                character_to_x = 0
                
    # Character location
    character_x_pos += character_to_x * dt
    
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
        
    # Weapon location
    weapons = [[w[0], w[1] - weapon_speed * dt] for w in weapons if w[1] - weapon_speed * dt > 0]
  
    # Ball location
    for ball_idx, ball_val in enumerate(balls):
        ball_x_pos = ball_val['pos_x']          
        ball_y_pos = ball_val['pos_y']
        ball_img_idx = ball_val['img_idx']
        
        ball_size = ball_images[ball_img_idx].get_rect().size
        ball_width, ball_height = ball_size[0], ball_size[1]
        
        if ball_x_pos < 0 or ball_x_pos > screen_width - ball_width:
            ball_val['to_x'] *= -1
        
        if ball_y_pos >= screen_height - stage_height - ball_height:
            ball_val['to_y'] = ball_val['init_spd_y']
        else:
            ball_val['to_y'] += 0.5
            
        ball_val['pos_x'] += ball_val['to_x']
        ball_val['pos_y'] += ball_val['to_y']

    screen.blit(background, (0, 0)) # Draw background
    
    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))
        
    for idx, ball in enumerate(balls):
        ball_x_pos = ball['pos_x']
        ball_y_pos = ball['pos_y']
        ball_img_idx = ball['img_idx']
        screen.blit(ball_images[ball_img_idx], (ball_x_pos, ball_y_pos))
    
    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update() # Draw game screen again 


# Quit pygame
pygame.quit()