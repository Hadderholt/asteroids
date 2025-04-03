import pygame
from constants import *
from player import Player  # Add this import
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0

    # Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        
        dt = clock.tick(60) / 1000
        updatable.update(dt)
        
        screen.fill((0, 0, 0))
        for sprite in drawable:
            # Assuming each sprite in the drawable group has a draw() method
            sprite.draw(screen)

        pygame.display.flip()
        


if __name__ == "__main__":
    main()
