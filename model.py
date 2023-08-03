from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

class Snake:
    def __init__(self, head: Point):
        self.head = head
        self.body = [head]

    def move(self, direction: str):
        # Update the snake's position based on the direction
        pass

class Food:
    def __init__(self, position: Point):
        self.position = position
