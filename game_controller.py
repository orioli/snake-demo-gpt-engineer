import pygame
from pygame.locals import *
from snake import Snake

class GameController:
    def __init__(self):
        self.snake = Snake()
        self.direction = "RIGHT"

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_UP or event.key == K_w:
                    self.direction = "UP"
                elif event.key == K_DOWN or event.key == K_s:
                    self.direction = "DOWN"
                elif event.key == K_LEFT or event.key == K_a:
                    self.direction = "LEFT"
                elif event.key == K_RIGHT or event.key == K_d:
                    self.direction = "RIGHT"

    def update(self):
        self.snake.move(self.direction)

    def draw(self, screen):
        self.snake.draw(screen)
