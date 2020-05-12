import pyglet
import pymunk
from pyglet.window import key, mouse

from .basic import Basic


class Paddle(Basic):
    """A player's paddle, derived from Basic."""

    def __init__(self, application, player):
        """ Initialise the paddle.

        :type application: Application
        :param application: The application itself.

        :type player: int
        :param player: The ID of the player, 1 or 2.
        """
        self.player = player
        if self.player == 1:
            super().__init__(
                application,
                50, (application.window.height//2)-50,
                25, 100,
                (255, 255, 255),
                physics_type=pymunk.Body.DYNAMIC,
                collision_type=2
            )
            self.groove = pymunk.GrooveJoint(
                self.application.space.static_body,
                self,
                (50, 25),
                (50, application.window.height-25),
                (0, 0)
            )
        elif self.player == 2:
            super().__init__(
                application,
                application.window.width-75, (application.window.height//2)-50,
                25, 100,
                (255, 255, 255),
                physics_type=pymunk.Body.DYNAMIC,
                collision_type=2
            )
            self.groove = pymunk.GrooveJoint(
                self.application.space.static_body,
                self,
                (application.window.width-75, 25),
                (application.window.width-75, application.window.height-25),
                (0, 0)
            )
        self.application.space.add(self.groove)

    def update(self, dt):
        """ Update the paddle.

        :type dt: float
        :param dt: Time passed since the last update.
        """
        if self.player == 1:
            controls = {
                "up": self.application.key_handler[key.W],
                "down": self.application.key_handler[key.S],
            }
        elif self.player == 2:
            controls = {
                "up": self.application.key_handler[key.UP],
                "down": self.application.key_handler[key.DOWN],
            }

        vy = 0

        if controls["up"] and self.position.y < self.application.window.height-125:
            vy += 750
        if controls["down"] and self.position.y > 25:
            vy -= 750

        self.velocity = (0, vy)

        super().update(dt)
