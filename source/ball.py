import random

from .basic import Basic


class Ball(Basic):
    def __init__(self, application):
        super().__init__(
            application,
            application.window.width//2-10,
            application.window.height//2-10,
            20, 20,
            (255, 255, 255)
        )
        self.vx = random.choice([-250, 250])
        self.vy = random.randint(-175, 175)

    def update(self, dt):
        if (
            self.aabb[0] < 0 or
            self.aabb[2] > self.application.window.width
        ):
            self.vx *= -1

            if self.vx < 0:
                self.vx -= 10
            else:
                self.vx += 10
            if self.vy < 0:
                self.vy -= 10
            else:
                self.vy += 10

        if (
            self.aabb[1] < 0 or
            self.aabb[3] > self.application.window.height
        ):
            self.vy *= -1

            if self.vx < 0:
                self.vx -= 10
            else:
                self.vx += 10
            if self.vy < 0:
                self.vy -= 10
            else:
                self.vy += 10

        super().update(dt)
