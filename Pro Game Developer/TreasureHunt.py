import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
GRID_SIZE = 20
CELL_SIZE = WIDTH // GRID_SIZE
FPS = 30
NUM_OBSTACLES = 10

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Game setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Treasure Hunt Game")
clock = pygame.time.Clock()

# Player and treasures
player_pos = [GRID_SIZE // 2, GRID_SIZE // 2]
treasure_pos = []
obstacle_pos = []
score = 0
high_score = 0
game_over = False

# Fonts for messages
font = pygame.font.SysFont("Arial", 24)

def reset_game():
    global player_pos, treasure_pos, obstacle_pos, score, game_over
    player_pos = [GRID_SIZE // 2, GRID_SIZE // 2]
    treasure_pos = [[random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)] for _ in range(3)]
    obstacle_pos = []
    while len(obstacle_pos) < NUM_OBSTACLES:
        pos = [random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)]
        if pos != player_pos and pos not in treasure_pos and pos not in obstacle_pos:
            obstacle_pos.append(pos)
    score = 0
    game_over = False

def draw_grid():
    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(screen, WHITE, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, WHITE, (0, y), (WIDTH, y))

def draw_player():
    pygame.draw.rect(screen, BLUE, (player_pos[0] * CELL_SIZE, player_pos[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def draw_treasures():
    for pos in treasure_pos:
        pygame.draw.rect(screen, GREEN, (pos[0] * CELL_SIZE, pos[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def draw_obstacles():
    for pos in obstacle_pos:
        pygame.draw.rect(screen, RED, (pos[0] * CELL_SIZE, pos[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def check_collision():
    for treasure in treasure_pos:
        if player_pos == treasure:
            treasure_pos.remove(treasure)
            return True
    return False

def update_high_score():
    global high_score
    if score > high_score:
        high_score = score

def draw_game_over():
    game_over_text = font.render("Game Over! Press SPACE to Restart", True, WHITE)
    screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2))

# Initialize the game
reset_game()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Check if the spacebar is pressed to restart the game after game over
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and game_over:
            reset_game()

    keys = pygame.key.get_pressed()

    if not game_over:
        if keys[pygame.K_LEFT] and player_pos[0] > 0:
            player_pos[0] -= 1
        if keys[pygame.K_RIGHT] and player_pos[0] < GRID_SIZE - 1:
            player_pos[0] += 1
        if keys[pygame.K_UP] and player_pos[1] > 0:
            player_pos[1] -= 1
        if keys[pygame.K_DOWN] and player_pos[1] < GRID_SIZE - 1:
            player_pos[1] += 1

        if check_collision():
            score += 1
            if len(treasure_pos) == 0:
                reset_game()
            print(f"Score: {score}, High Score: {high_score}")

        # Check for collision with obstacles
        if player_pos in obstacle_pos:
            print("Game Over! You hit an obstacle.")
            game_over = True

    # Draw everything
    screen.fill(BLACK)
    draw_grid()
    draw_player()
    draw_treasures()
    draw_obstacles()

    # If the game is over, show the Game Over screen
    if game_over:
        draw_game_over()

    pygame.display.flip()
    clock.tick(FPS)
