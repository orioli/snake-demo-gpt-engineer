import pygame

class Snake:
    def __init__(self):
        self.position = [(100, 50), (90, 50), (80, 50)]
        self.direction = "RIGHT"

    def move(self, direction):
        if direction == "UP":
            self.position[0] = (self.position[0][0], self.position[0][1] - 10)
        elif direction == "DOWN":
            self.position[0] = (self.position[0][0], self.position[0][1] + 10)
        elif direction == "LEFT":
            self.position[0] = (self.position[0][0] - 10, self.position[0][1])
        elif direction == "RIGHT":
            self.position[0] = (self.position[0][0] + 10, self.position[0][1])

    def draw(self, screen):
        for pos in self.position:
            pygame.draw.rect(screen, (0, 255, 0), (pos[0], pos[1], 10, 10))
