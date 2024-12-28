import pygame
import random

pygame.init()

# Game constants
SCREEN_WIDTH, SCREEN_HEIGHT = 300, 600
GRID_SIZE = 30
GRID_WIDTH, GRID_HEIGHT = SCREEN_WIDTH // GRID_SIZE, SCREEN_HEIGHT // GRID_SIZE
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [
    (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), 
    (128, 0, 128), (0, 255, 0), (255, 0, 0)
]

# Tetrimino shapes
SHAPES = [
    [[1, 1, 1, 1]],
    [[1, 1], [1, 1]],
    [[0, 1, 1], [1, 1, 0]],
    [[1, 1, 0], [0, 1, 1]],
    [[1, 0, 0], [1, 1, 1]],
    [[0, 0, 1], [1, 1, 1]],
    [[0, 1, 0], [1, 1, 1]]
]

class Tetrimino:
    def __init__(self):
        self.shape = random.choice(SHAPES)
        self.color = random.choice(COLORS)
        self.x = GRID_WIDTH // 2 - len(self.shape[0]) // 2
        self.y = 0

    def rotate(self):
        self.shape = [list(row) for row in zip(*self.shape[::-1])]

def create_grid(locked_positions={}):
    grid = [[BLACK for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            if (x, y) in locked_positions:
                grid[y][x] = locked_positions[(x, y)]
    return grid

def draw_grid(surface, grid):
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            pygame.draw.rect(surface, grid[y][x], (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE), 0)
    for x in range(GRID_WIDTH):
        pygame.draw.line(surface, WHITE, (x * GRID_SIZE, 0), (x * GRID_SIZE, SCREEN_HEIGHT))
    for y in range(GRID_HEIGHT):
        pygame.draw.line(surface, WHITE, (0, y * GRID_SIZE), (SCREEN_WIDTH, y * GRID_SIZE))

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    locked_positions = {}
    grid = create_grid(locked_positions)
    current_piece = Tetrimino()
    run = True

    while run:
        grid = create_grid(locked_positions)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_piece.x -= 1
                if event.key == pygame.K_RIGHT:
                    current_piece.x += 1
                if event.key == pygame.K_DOWN:
                    current_piece.y += 1
                if event.key == pygame.K_UP:
                    current_piece.rotate()

        current_piece.y += 1
        screen.fill(BLACK)
        draw_grid(screen, grid)
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
