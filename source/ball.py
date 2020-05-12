import random
import time

import pyglet
import pymunk

from .basic import Basic


class Ball(Basic):
    """A ball, derived from Basic."""

    def __init__(self, application):
        """ Initialise the ball with a random direction.

        :type application: Application
        :param application: The application itself.
        """
        self.reset = False

        super().__init__(
            application,
            application.window.width//2-7,
            application.window.height//2-7,
            14, 14,
            (255, 255, 255),
            physics_type=pymunk.Body.DYNAMIC,
            collision_type=1
        )
        self.apply_impulse_at_local_point((
            random.choice([-200, 200]),
            random.randint(-175, 175)
        ))

    def update(self, dt):
        """ Update the ball.

        :type dt: float
        :param dt: Time passed since last update call.
        """
        if self.reset:
            self.position = (
                self.application.window.width//2-7,
                self.application.window.height//2-7
            )
            self.velocity = (0, 0)
            self.apply_impulse_at_local_point((
                random.choice([-200, 200]),
                random.randint(-175, 175)
            ))
            self.reset = False

        super().update(dt)
