import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BLOCK_SIZE = 30

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BROWN = (139, 69, 19)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Block Builder")

# Player position
player_x = SCREEN_WIDTH // 2
player_y = SCREEN_HEIGHT // 2
player_speed = 5

# Terrain grid
terrain = [[None] * (SCREEN_WIDTH // BLOCK_SIZE) for _ in range(SCREEN_HEIGHT // BLOCK_SIZE)]

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                terrain_x = event.pos[0] // BLOCK_SIZE
                terrain_y = event.pos[1] // BLOCK_SIZE
                if terrain[terrain_y][terrain_x] == None:
                    terrain[terrain_y][terrain_x] = BROWN
                elif terrain[terrain_y][terrain_x] == BROWN:
                    terrain[terrain_y][terrain_x] = GREEN
                else:
                    terrain[terrain_y][terrain_x] = None
            if event.button == 3:  # Right mouse button
                terrain_x = event.pos[0] // BLOCK_SIZE
                terrain_y = event.pos[1] // BLOCK_SIZE
                terrain[terrain_y][terrain_x] = None

    # Check keyboard input for movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # Clear the screen
    screen.fill(WHITE)

    # Draw terrain
    for y, row in enumerate(terrain):
        for x, block_color in enumerate(row):
            if block_color:
                pygame.draw.rect(screen, block_color, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

    # Draw player
    pygame.draw.circle(screen, GREEN, (player_x, player_y), BLOCK_SIZE // 2)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
