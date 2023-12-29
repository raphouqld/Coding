import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up display
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Set up colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# Set up Snake
snake_size = 20
snake_speed = 5
snake = [(width // 2, height // 2)]
snake_direction = (1, 0)

# Set up Food
food_size = 20
food = (random.randrange(0, width - food_size, food_size),
        random.randrange(0, height - food_size, food_size))

# Set up Score
score = 0
font = pygame.font.SysFont(None, 25)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != (0, 1):
                snake_direction = (0, -1)
            elif event.key == pygame.K_DOWN and snake_direction != (0, -1):
                snake_direction = (0, 1)
            elif event.key == pygame.K_LEFT and snake_direction != (1, 0):
                snake_direction = (-1, 0)
            elif event.key == pygame.K_RIGHT and snake_direction != (-1, 0):
                snake_direction = (1, 0)

    # Move the Snake
    x, y = snake[0]
    x += snake_direction[0] * snake_size
    y += snake_direction[1] * snake_size

    # Check for collisions with the edges
    if x < 0 or x >= width or y < 0 or y >= height:
        pygame.quit()
        sys.exit()

    # Check for collisions with the food
    if x == food[0] and y == food[1]:
        score += 1
        food = (random.randrange(0, width - food_size, food_size),
                random.randrange(0, height - food_size, food_size))
    else:
        # Remove the tail
        snake.pop()

    # Check for collisions with itself
    if (x, y) in snake:
        pygame.quit()
        sys.exit()

    # Update the snake
    snake.insert(0, (x, y))

    # Draw the background
    screen.fill(black)

    # Draw the Snake
    for segment in snake:
        pygame.draw.rect(screen, green, (segment[0], segment[1], snake_size, snake_size))

    # Draw the Food
    pygame.draw.rect(screen, red, (food[0], food[1], food_size, food_size))

    # Draw the Score
    score_text = font.render("Score: {}".format(score), True, white)
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Control the snake's speed
    pygame.time.Clock().tick(snake_speed)
