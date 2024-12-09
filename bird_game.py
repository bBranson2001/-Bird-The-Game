import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen dimensions (Larger window)
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Bird")

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
GREEN = (34, 177, 76)  # Lighter green for pipes
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)  # Bird color
ORANGE = (255, 165, 0)  # Bird color

# Font for score and game over
font = pygame.font.Font(None, 48)
game_over_font = pygame.font.Font(None, 72)
info_font = pygame.font.Font(None, 30)  # Smaller font for additional info

# Bird settings
BIRD_WIDTH = 40
BIRD_HEIGHT = 40
bird_x = SCREEN_WIDTH // 4
bird_y = SCREEN_HEIGHT // 2
bird_velocity = 0
gravity = 0.5
jump_strength = -10

# Pipe settings
PIPE_WIDTH = 60
PIPE_HEIGHT = 200
pipe_x = SCREEN_WIDTH
pipe_gap = 200
pipe_speed = 4

# Score
score = 0

# Example for scaling images
# Load and scale the background image
background_img = pygame.image.load("C:/Users/brans/OneDrive/Documents/bird game thing/sky.png")  # Replace with your image path
background_img = pygame.transform.scale(background_img, (SCREEN_WIDTH, SCREEN_HEIGHT))  # Scale to screen size

# Load and scale the bird image
bird_img = pygame.image.load("C:/Users/brans/OneDrive/Documents/bird game thing/bird.png")  # Replace with your image path
bird_img = pygame.transform.scale(bird_img, (40, 40))  # Scale bird to 40x40 pixels

def draw_bird():
    """Draw the bird."""
    screen.blit(bird_img, (bird_x, bird_y))

def draw_pipes(pipe_x, pipe_height, pipe_gap):
    """Draw the pipes."""
    pygame.draw.rect(screen, GREEN, (pipe_x, 0, PIPE_WIDTH, pipe_height))
    pygame.draw.rect(screen, GREEN, (pipe_x, pipe_height + pipe_gap, PIPE_WIDTH, SCREEN_HEIGHT))

def check_collision(pipe_x, pipe_height, pipe_gap):
    """Check for collisions with pipes or the ground."""
    bird_rect = pygame.Rect(bird_x, bird_y, BIRD_WIDTH, BIRD_HEIGHT)
    pipe_top = pygame.Rect(pipe_x, 0, PIPE_WIDTH, pipe_height)
    pipe_bottom = pygame.Rect(pipe_x, pipe_height + pipe_gap, PIPE_WIDTH, SCREEN_HEIGHT)

    if bird_rect.colliderect(pipe_top) or bird_rect.colliderect(pipe_bottom) or bird_y > SCREEN_HEIGHT or bird_y < 0:
        return True
    return False

def display_score(score):
    """Display the score on the screen."""
    score_surface = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_surface, (10, 10))

def display_game_over():
    """Display the game over screen."""
    game_over_text = game_over_font.render("GAME OVER", True, BLACK)
    screen.blit(game_over_text, (SCREEN_WIDTH // 4, SCREEN_HEIGHT // 3))
    
    # Additional information text
    thanks_text = info_font.render("THANKS FOR PLAYING", True, BLACK)
    screen.blit(thanks_text, (SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2))

    branson_text = info_font.render("ANOTHER BIRD CLONE BY BRANSON", True, BLACK)
    screen.blit(branson_text, (SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2 + 40))  # Slightly below "THANKS FOR PLAYING"

def main():
    global bird_y, bird_velocity, pipe_x, score

    # Game loop
    while True:
        # Reset the game state when restarting
        bird_y = SCREEN_HEIGHT // 2
        bird_velocity = 0
        score = 0
        pipe_x = SCREEN_WIDTH
        pipe_height = random.randint(100, SCREEN_HEIGHT - pipe_gap - 100)

        game_running = True
        while game_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        bird_velocity = jump_strength

            # Update bird position
            bird_velocity += gravity
            bird_y += bird_velocity

            # Update pipe position
            pipe_x -= pipe_speed
            if pipe_x < -PIPE_WIDTH:
                pipe_x = SCREEN_WIDTH
                pipe_height = random.randint(100, SCREEN_HEIGHT - pipe_gap - 100)
                score += 1  # Increment score for passing a pipe

            # Check for collisions
            if check_collision(pipe_x, pipe_height, pipe_gap):
                game_running = False

            # Draw everything
            screen.blit(background_img, (0, 0))  # Draw background
            draw_bird()
            draw_pipes(pipe_x, pipe_height, pipe_gap)
            display_score(score)

            # Update display
            pygame.display.flip()
            clock.tick(60)

        # Game over screen
        screen.fill(WHITE)
        display_game_over()
        pygame.display.flip()

        # Wait for the player to press space to restart
        waiting_for_restart = True
        while waiting_for_restart:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        waiting_for_restart = False

if __name__ == "__main__":
    main()
