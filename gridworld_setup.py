import random
import pygame
import sys

# ---------------- GRID GENERATION (YOUR CODE) ----------------
SIZE = 6
grid = [["U" for _ in range(SIZE)] for _ in range(SIZE)]

# Generate blocks
for r in range(SIZE):
    for c in range(SIZE):
        if random.random() < 0.30:
            grid[r][c] = "B"
        else:
            grid[r][c] = "0"

# Place Start (S)
while True:
    sr = random.randint(0, SIZE - 1)
    sc = random.randint(0, SIZE - 1)
    if grid[sr][sc] == "0":
        grid[sr][sc] = "S"
        break

# Place Goal (G)
while True:
    gr = random.randint(0, SIZE - 1)
    gc = random.randint(0, SIZE - 1)
    if grid[gr][gc] == "0":
        grid[gr][gc] = "G"
        break

# ---------------- PYGAME DRAWING ----------------
CELL = 80
LEFT_PAD = 70
TOP_PAD = 70
WIN_W = LEFT_PAD + SIZE * CELL + 40
WIN_H = TOP_PAD + SIZE * CELL + 40

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FREE  = (240, 240, 240)

pygame.init()
screen = pygame.display.set_mode((WIN_W, WIN_H))
pygame.display.set_caption("Gridworld")

font_label = pygame.font.SysFont(None, 36)
font_cell = pygame.font.SysFont(None, 42)

def cell_rect(r, c):
    return pygame.Rect(
        LEFT_PAD + c * CELL,
        TOP_PAD + r * CELL,
        CELL,
        CELL
    )

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(WHITE)

    # Draw cells
    for r in range(SIZE):
        for c in range(SIZE):
            rect = cell_rect(r, c)

            if grid[r][c] == "B":
                pygame.draw.rect(screen, BLACK, rect)
            else:
                pygame.draw.rect(screen, FREE, rect)

            if grid[r][c] in ("S", "G"):
                text = font_cell.render(grid[r][c], True, BLACK)
                screen.blit(text, text.get_rect(center=rect.center))

    # Draw grid lines
    for i in range(SIZE + 1):
        pygame.draw.line(
            screen, BLACK,
            (LEFT_PAD + i * CELL, TOP_PAD),
            (LEFT_PAD + i * CELL, TOP_PAD + SIZE * CELL),
            2
        )
        pygame.draw.line(
            screen, BLACK,
            (LEFT_PAD, TOP_PAD + i * CELL),
            (LEFT_PAD + SIZE * CELL, TOP_PAD + i * CELL),
            2
        )

    # Thick outer border
    pygame.draw.rect(
        screen, BLACK,
        (LEFT_PAD, TOP_PAD, SIZE * CELL, SIZE * CELL),
        6
    )

    # Column labels (1–6)
    for c in range(SIZE):
        label = font_label.render(str(c + 1), True, BLACK)
        x = LEFT_PAD + c * CELL + CELL // 2
        y = TOP_PAD - 30
        screen.blit(label, label.get_rect(center=(x, y)))

    # Row labels (A–F)
    for r in range(SIZE):
        label = font_label.render(chr(ord('A') + r), True, BLACK)
        x = LEFT_PAD - 30
        y = TOP_PAD + r * CELL + CELL // 2
        screen.blit(label, label.get_rect(center=(x, y)))

    pygame.display.flip()