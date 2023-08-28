import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Game constants
WIDTH, HEIGHT = 400, 600
FPS = 60
GRAVITY = 1
JUMP_STRENGTH = -20
PIPE_VELOCITY = -3
PIPE_SPACING = 200
PIPE_HEIGHTS = [200, 250, 300, 350]

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Fish")

# Load fish image
fish_image = pygame.image.load("fish.jfif")  # Replace with your fish image file
fish_rect = fish_image.get_rect()
fish_rect.center = (100, HEIGHT // 2)

# Load pipe images
pipe_image = pygame.image.load("pipe.png")  # Replace with your pipe image file

# Create a list to store pipes
pipes = []

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            fish_rect.y += JUMP_STRENGTH

    # Apply gravity
    fish_rect.y += GRAVITY

    # Generate pipes
    if len(pipes) == 0 or pipes[-1][0] < WIDTH - PIPE_SPACING:
        pipe_height = random.choice(PIPE_HEIGHTS)
        pipes.append([WIDTH, pipe_height])

    # Update pipe positions
    for pipe in pipes:
        pipe[0] += PIPE_VELOCITY

    # Remove off-screen pipes
    if pipes[0][0] < -pipe_image.get_width():
        pipes.pop(0)

    # Clear the screen
    screen.fill(WHITE)

    # Draw pipes
    for pipe in pipes:
        pipe_rect = pipe_image.get_rect(topleft=(pipe[0], pipe[1]))
        screen.blit(pipe_image, pipe_rect)

    # Draw fish
    screen.blit(fish_image, fish_rect)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)
