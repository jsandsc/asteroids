import pygame.draw
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y , radius)

    def draw(self, screen):
        pygame.draw.circle(
            surface=screen,
            color=(255,255,255),
            center=self.position,
            radius=self.radius,
            width=2
        )

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        angle = random.uniform(20, 50)

        split_1 = self.velocity.rotate(angle)
        split_2 = self.velocity.rotate(-angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)

        asteroid_1.velocity = split_1 * 1.2
        asteroid_2.velocity = split_2 * 1.2


