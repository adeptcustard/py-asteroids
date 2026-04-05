import pygame
from logger import log_state
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print("Screen width: 1280")
    print("Screen height: 720")

    pygame.init()

    game_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()

    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    player = Player((SCREEN_WIDTH / 2),(SCREEN_HEIGHT / 2))
    asteroidfield = AsteroidField()

    while True:
        log_state()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        dt = game_clock.tick(60) / 1000
        
        updatable.update(dt)

        game_screen.fill("black")
        for sprite in drawable:
            sprite.draw(game_screen)

        pygame.display.flip()


if __name__ == "__main__":
    main()
