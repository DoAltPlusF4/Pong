import pyglet
import pymunk


class Basic(pymunk.Body):
    """A basic object class, derived from pymunk.Body."""

    def __init__(self, application, x, y, width, height, colour, physics_type=None, collision_type=None):
        """ Initialise the class with collider and sprite.

        :type application: Application
        :param application: The application itself.

        :type x: float
        :param x: The X position of the object

        :type y: float
        :param y: The Y position of the object

        :type width: float
        :param width: The width of the object

        :type height: float
        :param height: The height of the object

        :type colour: tuple
        :param colour: The RGB colour tuple for the sprite.

        :type physics_type: int
        :param physics_type: The physics type, pymunk.Body.<TYPE>.

        :type collision_type: int
        :param collision_type: The collision type ID.
        """
        self.application = application

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
            color=colour,
            batch=self.application.batch
        )

    def update(self, dt):
        """ Update the position of the sprite.

        :type dt: float
        :param dt: Time passed since last update.=
        """
        self.shape_sprite.position = self.position.x, self.position.y
