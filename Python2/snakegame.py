import pygame
import sys
import random
import datetime

# Init
pygame.init()
SCREEN_W, SCREEN_H = 800, 800
BLOCK_SIZE = 50
FONT = pygame.font.SysFont("Arial", 36)
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
pygame.display.set_caption("Python Game with Python")

clock = pygame.time.Clock()

# Load and scale images
snake_head_img = pygame.image.load("head.png")
snake_head_img = pygame.transform.scale(snake_head_img, (BLOCK_SIZE, BLOCK_SIZE))
snake_body_img = pygame.image.load("body.png")
snake_body_img = pygame.transform.scale(snake_body_img, (BLOCK_SIZE, BLOCK_SIZE))
apple_img = pygame.image.load("apple.png")
apple_img = pygame.transform.scale(apple_img, (BLOCK_SIZE, BLOCK_SIZE))

# Functions to handle history
def read_history():
    try:
        with open("history.txt", "r") as file:
            lines = file.readlines()
            return [line.strip() for line in lines][-5:]  # Return the last 5 lines
    except FileNotFoundError:
        return []

def write_history(score):
    with open("history.txt", "a") as file:
        file.write(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Score: {score}\n")

# Classes
class Snake:
    def __init__(self) -> None:
        self.x, self.y = BLOCK_SIZE, BLOCK_SIZE
        self.xdir = 1
        self.ydir = 0
        self.head = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)
        self.body = [pygame.Rect(self.x - BLOCK_SIZE, self.y, BLOCK_SIZE, BLOCK_SIZE)]
        self.dead = False

    def update(self):
        if self.dead:
            return

        # Move the body
        self.body.insert(0, pygame.Rect(self.head.x, self.head.y, BLOCK_SIZE, BLOCK_SIZE))
        self.body.pop()  # Remove last tail segment unless an apple was eaten

        # Update the head position
        self.head.x += self.xdir * BLOCK_SIZE
        self.head.y += self.ydir * BLOCK_SIZE

        # Wrap around screen edges
        if self.head.x >= SCREEN_W:
            self.head.x = 0
        elif self.head.x < 0:
            self.head.x = SCREEN_W - BLOCK_SIZE
        if self.head.y >= SCREEN_H:
            self.head.y = 0
        elif self.head.y < 0:
            self.head.y = SCREEN_H - BLOCK_SIZE

        # Check for self-collision
        for square in self.body:
            if self.head.colliderect(square):
                self.dead = True

    def grow(self):
        self.body.insert(0, pygame.Rect(self.head.x, self.head.y, BLOCK_SIZE, BLOCK_SIZE))

class Apple:
    def __init__(self) -> None:
        self.spawn()

    def spawn(self):
        self.x = random.randint(0, (SCREEN_W // BLOCK_SIZE) - 1) * BLOCK_SIZE
        self.y = random.randint(0, (SCREEN_H // BLOCK_SIZE) - 1) * BLOCK_SIZE
        self.rect = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)

    def draw(self):
        screen.blit(apple_img, (self.rect.x, self.rect.y))

# Functions
def drawGrid():
    for x in range(0, SCREEN_W, BLOCK_SIZE):
        for y in range(0, SCREEN_H, BLOCK_SIZE):
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(screen, '#3c3c3b', rect, 1)

def restart_game():
    global snake, apple, game_over, game_started
    snake = Snake()
    apple = Apple()
    game_over = False
    game_started = False

def start_screen():
    screen.fill("#000000")
    title_text = FONT.render("Python Game with Python", True, "white")
    title_rect = title_text.get_rect(center=(SCREEN_W / 2, SCREEN_H / 2 - 100))
    screen.blit(title_text, title_rect)

    start_text = FONT.render("Press any key to start", True, "white")
    start_rect = start_text.get_rect(center=(SCREEN_W / 2, SCREEN_H / 2))
    screen.blit(start_text, start_rect)

    history = read_history()
    if history:
        history_text = FONT.render("History", True, "white")
        history_rect = history_text.get_rect(center=(SCREEN_W / 2, SCREEN_H / 2 + 100))
        screen.blit(history_text, history_rect)

        for i, line in enumerate(history):
            record_text = FONT.render(line, True, "white")
            record_rect = record_text.get_rect(center=(SCREEN_W / 2, SCREEN_H / 2 + 150 + i * 30))
            screen.blit(record_text, record_rect)

    pygame.display.update()

# Game Initialization
snake = Snake()
apple = Apple()
game_over = False
game_started = False

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if not game_started:
                game_started = True
            elif game_over:
                write_history(len(snake.body))
                restart_game()
            elif event.key == pygame.K_q:
                restart_game()
            else:
                if event.key == pygame.K_DOWN and snake.ydir == 0:
                    snake.ydir = 1
                    snake.xdir = 0
                elif event.key == pygame.K_UP and snake.ydir == 0:
                    snake.ydir = -1
                    snake.xdir = 0
                elif event.key == pygame.K_LEFT and snake.xdir == 0:
                    snake.ydir = 0
                    snake.xdir = -1
                elif event.key == pygame.K_RIGHT and snake.xdir == 0:
                    snake.ydir = 0
                    snake.xdir = 1

    if not game_started:
        start_screen()
        continue

    if not game_over:
        snake.update()
        if snake.dead:
            game_over = True

    # Check if snake eats the apple
    if snake.head.colliderect(apple.rect):
        snake.grow()
        apple.spawn()

    # Draw everything
    screen.fill("#000000")
    drawGrid()
    apple.draw()

    # Draw the snake head image at the head's position
    screen.blit(snake_head_img, (snake.head.x, snake.head.y))
    for square in snake.body:
        screen.blit(snake_body_img, (square.x, square.y))

    # Display score
    score_text = FONT.render(f"Score: {len(snake.body)}", True, "white")
    screen.blit(score_text, (10, 10))

    # Display quit instruction
    quit_text = FONT.render("Press Q to quit", True, "white")
    screen.blit(quit_text, (SCREEN_W - 500, 10))

    # Game Over display
    if game_over:
        game_over_text = FONT.render("Game Over! Press any key to restart.", True, "white")
        game_over_rect = game_over_text.get_rect(center=(SCREEN_W / 2, SCREEN_H / 2))
        screen.blit(game_over_text, game_over_rect)

    pygame.display.update()
    clock.tick(10)
