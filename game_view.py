import pygame

class GameView:
    def __init__(self):
        self.width = 500
        self.height = 500
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Snake Game")

    def draw(self, snake):
        self.screen.fill((0, 0, 0))
        snake.draw(self.screen)
        pygame.display.update()
