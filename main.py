import pygame

pygame.init()

# Screen size
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# Screen title
pygame.display.set_caption("Nado Game")

# FPS
clock = pygame.time.Clock()

# Load background image
background = pygame.image.load("C:\\Users\\user\\source\\repos\\pygame_basic\\background.png")

# Load game character
character = pygame.image.load("C:\\Users\\user\\source\\repos\\pygame_basic\\character.png")
character_size = character.get_rect().size  # image size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width - character_width) / 2
character_y_pos = screen_height - character_height

to_x = to_y = 0

# Event loop
running = True
character_speed = 0.5
while running:
    dt = clock.tick(60) # The number of frames per second
    
    for event in pygame.event.get():  # Check event
        if event.type == pygame.QUIT: # Close window?
            running = False
        
        if event.type == pygame.KEYDOWN:    # Check key event
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt
    
    # Horizontal boundary
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    # Vertical boundary
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height
                  

    screen.blit(background, (0, 0))
    screen.blit(character,(character_x_pos, character_y_pos))
    
    pygame.display.update() # Draw game screen again 

# Quit pygame
pygame.quit()