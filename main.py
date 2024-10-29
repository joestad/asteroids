#imports pygame
import pygame

import sys

#imports constants
from constants import *

#imports player
from player import Player

#imports asteroids
from asteroid import Asteroid

from asteroidfield import AsteroidField

from shot import Shot


def main():
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0,0,0))

        for object in updatable:
            object.update(dt)

        for object in asteroids:
            if object.collision_check(player):
                print ("Game over!")
                sys.exit()

            for bullet in shots:
                if object.collision_check(bullet):
                    object.split()
                    bullet.kill()

        
        for object in drawable:
            object.draw(screen)

        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()
