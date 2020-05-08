import random

from .basic import Basic


class Ball(Basic):
    def __init__(self, application):
        super().__init__(
            application,
            application.window.width//2-7,
            application.window.height//2-7,
            14, 14,
            (255, 255, 255)
        )
        self.vx = random.choice([-200, 200])
        self.vy = random.randint(-175, 175)

    def update(self, dt):
        collided = False
        if (
            self.aabb[0] < 25 or
            self.aabb[2] > self.application.window.width - 25
        ):
            self.vx *= -1
            collided = True

        if (
            self.aabb[1] < 25 or
            self.aabb[3] > self.application.window.height - 25
        ):
            self.vy *= -1
            collided = True

        if self.aabbCheck(self.application.paddle_1):
            self.vx *= -1
            collided = True
        if self.aabbCheck(self.application.paddle_2):
            self.vx *= -1
            collided = True

        if collided:
            if self.vx < 0:
                self.vx -= 5
            else:
                self.vx += 5

            if self.vy < 0:
                self.vy -= 5
            else:
                self.vy += 5

        super().update(dt)
