# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys

import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from shot import Shot
from asteroidfield import AsteroidField

def main():
    # Initialize pygame
    pygame.init()

    # Print out the start-up text
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Create groups for updatable and drawable objects
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Add the Player class to both of the groups
    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = updateable
    Shot.containers = (shots, updateable, drawable)

    # Create the instances of player and clock
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    clock = pygame.time.Clock()
    dt = 0

    # Specify window dimensions for game display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0,0,0))

        for entity in updateable:
            entity.update(dt)

        for entity in asteroids:
            if entity.check_for_collisions(player):
                print("Game over!")
                sys.exit()
            for shot in shots:
                if shot.check_for_collisions(entity):
                    shot.kill()
                    entity.split()

        for entity in drawable:
            entity.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000





if __name__ == "__main__":
    main()
