import pygame
from logger import log_state
import constants
from player import Player

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print("Screen width: 1280")
    print("Screen height: 720")

    pygame.init()

    game_screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()

    dt = 0

    player = Player((constants.SCREEN_WIDTH / 2),(constants.SCREEN_HEIGHT / 2))

    while True:
        log_state()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        dt = game_clock.tick(60) / 1000

        game_screen.fill("black")
        player.draw(game_screen)

        pygame.display.flip()


if __name__ == "__main__":
    main()
