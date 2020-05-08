import pyglet
from pyglet.window import key, mouse

from .basic import Basic


class Paddle(Basic):
    def __init__(self, application, player):
        self.player = player
        if self.player == 1:
            super().__init__(
                application,
                50, (application.window.height//2)-50,
                25, 100,
                (255, 255, 255)
            )
        elif self.player == 2:
            super().__init__(
                application,
                application.window.width-75, (application.window.height//2)-50,
                25, 100,
                (255, 255, 255)
            )

    def update(self, dt):
        self.vx = 0
        self.vy = 0
        if self.player == 1:
            if self.application.key_handler[key.W]:
                self.vy += 600
            if self.application.key_handler[key.S]:
                self.vy -= 600
        elif self.player == 2:
            if self.application.key_handler[key.UP]:
                self.vy += 600
            if self.application.key_handler[key.DOWN]:
                self.vy -= 600

        if self.aabb[3] > self.application.window.height-25:
            if self.vy > 0:
                self.vy = 0
        if self.aabb[1] < 25:
            if self.vy < 0:
                self.vy = 0

        super().update(dt)
