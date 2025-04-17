import circleshape
import pygame
import random
from constants import *

class Asteroid(circleshape.CircleShape):    
    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
         self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20, 50)
            first_split = self.velocity.rotate(angle)
            second_split = self.velocity.rotate(-angle)

            new_asteroid_1 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            new_asteroid_2 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            
            new_asteroid_1.velocity = first_split * 1.2
            new_asteroid_2.velocity = second_split * 1.2