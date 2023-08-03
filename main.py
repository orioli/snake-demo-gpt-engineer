import pygame
from game_controller import GameController
from game_view import GameView

def main():
    pygame.init()
    clock = pygame.time.Clock()
    game_controller = GameController()
    game_view = GameView()

    while True:
        game_controller.handle_events()
        game_controller.update()
        game_view.draw(game_controller.snake)
        clock.tick(10)

if __name__ == "__main__":
    main()
