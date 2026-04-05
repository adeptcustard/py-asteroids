import pygame
import random
from logger import log_event
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if ASTEROID_MIN_RADIUS == self.radius:
            return
        else:
            log_event("asteroid_split")
            split_angle = random.uniform(20, 50)

            new_direction = self.velocity.rotate(split_angle)

            new_radius = self.radius - ASTEROID_MIN_RADIUS

            first = Asteroid(self.position.x, self.position.y, new_radius)
            second = Asteroid(self.position.x, self.position.y, new_radius)

            first.velocity = new_direction * 1.2
            second.velocity = -new_direction * 1.2
