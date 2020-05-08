import pyglet
from pyglet.window import key, mouse

from source.ball import Ball


class Application:
    def __init__(self):
        self.window = pyglet.window.Window(
            width=960,
            height=720
        )
        self.window.push_handlers(self)
        self.batch = pyglet.graphics.Batch()

        self.key_handler = key.KeyStateHandler()
        self.window.push_handlers(self.key_handler)

        self.bottom_border = pyglet.shapes.Rectangle(
            0, 0,
            self.window.width, 30,
            color=(255, 255, 255),
            batch=self.batch
        )
        self.top_border = pyglet.shapes.Rectangle(
            0, self.window.height,
            self.window.width, -30,
            color=(255, 255, 255),
            batch=self.batch
        )

        self.ball = Ball(self)

    def on_draw(self):
        self.window.clear()
        self.batch.draw()

    def update(self, dt):
        self.ball.update(dt)

    def run(self):
        pyglet.clock.schedule_interval(self.update, 1/144)
        pyglet.app.run()


if __name__ == "__main__":
    application = Application()
    application.run()
