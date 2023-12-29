import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong Game")

# Set up colors
white = (255, 255, 255)
black = (0, 0, 0)

# Set up paddles
paddle_width, paddle_height = 15, 100
left_paddle = pygame.Rect(50, height // 2 - paddle_height // 2, paddle_width, paddle_height)
right_paddle = pygame.Rect(width - 50 - paddle_width, height // 2 - paddle_height // 2, paddle_width, paddle_height)
paddle_speed = 5

# Set up the ball
ball_size = 15
ball = pygame.Rect(width // 2 - ball_size // 2, height // 2 - ball_size // 2, ball_size, ball_size)
ball_speed = [5, 5]

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and left_paddle.y - paddle_speed > 0:
        left_paddle.y -= paddle_speed
    if keys[pygame.K_s] and left_paddle.y + paddle_speed < height - paddle_height:
        left_paddle.y += paddle_speed

    if keys[pygame.K_UP] and right_paddle.y - paddle_speed > 0:
        right_paddle.y -= paddle_speed
    if keys[pygame.K_DOWN] and right_paddle.y + paddle_speed < height - paddle_height:
        right_paddle.y += paddle_speed

    # Move the ball
    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

    # Check for collisions with paddles
    if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
        ball_speed[0] = -ball_speed[0]

    # Check for collisions with top and bottom walls
    if ball.y < 0 or ball.y > height - ball_size:
        ball_speed[1] = -ball_speed[1]

    # Check for scoring
    if ball.x < 0 or ball.x > width:
        ball.x = width // 2 - ball_size // 2
        ball.y = height // 2 - ball_size // 2
        ball_speed[0] = -ball_speed[0]

    # Draw the background
    screen.fill(black)

    # Draw the paddles
    pygame.draw.rect(screen, white, left_paddle)
    pygame.draw.rect(screen, white, right_paddle)

    # Draw the ball
    pygame.draw.rect(screen, white, ball)

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    pygame.time.Clock().tick(60)
