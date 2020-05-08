import pyglet


class Basic:
    def __init__(self, application, x, y, width, height, colour):
        self.application = application

        self.x, self.y = x, y
        self.w, self.h = width, height
        self.colour = colour

        self.vx, self.vy = 0, 0

        self.shape = pyglet.shapes.Rectangle(
            self.x, self.y,
            self.w, self.h,
            color=self.colour,
            batch=self.application.batch
        )

    def update(self, dt):
        self.x += self.vx*dt
        self.y += self.vy*dt
        self.shape.position = self.x, self.y

    def aabbCheck(self, other):
        return (
            self.aabb[0] < other.aabb[2] and
            self.aabb[2] > other.aabb[0] and
            self.aabb[1] < other.aabb[3] and
            self.aabb[3] > other.aabb[1]
        )

    @property
    def aabb(self):
        return (
            self.x,
            self.y,
            self.x + self.w,
            self.y + self.h
        )
