# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from constants import *

def main():
    pygame.init()
    dt = 0
    delta_clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player_ship = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")

        for item in drawable:
            item.draw(screen)
        
        updatable.update(dt)

        for item in asteroids:
            if player_ship.colided(item):
                print("GAME OVER!")
                sys.exit()

        for asteroid in asteroids:
            for shot in shots:
                if shot.colided(asteroid):
                    asteroid.split()
                    shot.kill()
                


        pygame.display.flip()
        dt = delta_clock.tick(60) / 1000


if __name__ == "__main__":
    main()