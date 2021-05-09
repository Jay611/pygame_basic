import pygame

pygame.init()

# Screen size
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# Screen title
pygame.display.set_caption("Nado Game")

# Load background image
background = pygame.image.load("C:\\Users\\user\\source\\repos\\pygame_basic\\background.png")

# Load game character
character = pygame.image.load("C:\\Users\\user\\source\\repos\\pygame_basic\\character.png")
character_size = character.get_rect().size  # image size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width - character_width) / 2
character_y_pos = screen_height - character_height

# Event loop
running = True
while running:
    for event in pygame.event.get():  # Check event
        if event.type == pygame.QUIT: # Close window?
            running = False

    screen.blit(background, (0, 0))
    screen.blit(character,(character_x_pos, character_y_pos))
    
    pygame.display.update() # Draw game screen again 

# Quit pygame
pygame.quit()