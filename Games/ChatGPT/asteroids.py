import pygame
import sys
import random
import math

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Asteroids Shooting Game")

# Set up colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Set up player
player_size = 50
player = pygame.Rect(width // 2 - player_size // 2, height - player_size * 2, player_size, player_size)
player_speed = 5

# Set up bullets
bullet_size = 5
bullets = []
bullet_speed = 7

# Set up asteroids
asteroid_size = 50
asteroids = []
asteroid_speed = 3
asteroid_spawn_rate = 25

# Set up Score
score = 0
font = pygame.font.SysFont(None, 25)

# Function to create an asteroid
def create_asteroid():
    return pygame.Rect(random.randint(0, width - asteroid_size), 0, asteroid_size, asteroid_size)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append(pygame.Rect(player.centerx - bullet_size // 2, player.y, bullet_size, bullet_size))

    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x - player_speed > 0:
        player.x -= player_speed
    if keys[pygame.K_RIGHT] and player.x + player_speed < width - player_size:
        player.x += player_speed

    # Move the bullets
    for bullet in bullets:
        bullet.y -= bullet_speed
        if bullet.y < 0:
            bullets.remove(bullet)

    # Move the asteroids
    for asteroid in asteroids:
        asteroid.y += asteroid_speed
        if asteroid.y > height:
            asteroids.remove(asteroid)
            score += 1

    # Spawn new asteroids
    if random.randint(1, asteroid_spawn_rate) == 1:
        asteroids.append(create_asteroid())

    # Check for collisions with bullets
    for bullet in bullets:
        for asteroid in asteroids:
            if bullet.colliderect(asteroid):
                bullets.remove(bullet)
                asteroids.remove(asteroid)
                score += 10

    # Check for collisions with player
    for asteroid in asteroids:
        if player.colliderect(asteroid):
            pygame.quit()
            sys.exit()

    # Draw the background
    screen.fill(black)

    # Draw the player
    pygame.draw.rect(screen, white, player)

    # Draw the bullets
    for bullet in bullets:
        pygame.draw.rect(screen, white, bullet)

    # Draw the asteroids
    for asteroid in asteroids:
        pygame.draw.rect(screen, red, asteroid)

    # Draw the Score
    score_text = font.render("Score: {}".format(score), True, white)
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    pygame.time.Clock().tick(60)
