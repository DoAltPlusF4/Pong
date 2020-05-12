import pyglet
import pymunk


class Basic(pymunk.Body):
    def __init__(self, application, x, y, width, height, colour, physics_type=None, collision_type=None):
        self.application = application

        self.colour = colour

        if physics_type is None:
            physics_type = pymunk.Body.STATIC

        super().__init__(mass=1, moment=float("inf"), body_type=physics_type)
        self.position = (x, y)
        self.collider = pymunk.Poly(
            body=self,
            vertices=[
                (0, 0),
                (width, 0),
                (width, height),
                (0, height)
            ]
        )
        self.collider.elasticity = 1.01
        if collision_type is not None:
            self.collider.collision_type = collision_type

        self.application.space.add(self, self.collider)

        self.shape_sprite = pyglet.shapes.Rectangle(
            self.position.x, self.position.y,
            width, height,
            color=self.colour,
            batch=self.application.batch
        )

    def update(self, dt):
        self.shape_sprite.position = self.position.x, self.position.y
