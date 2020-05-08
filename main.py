import pyglet
from pyglet.window import key, mouse


class Application:
    def __init__(self):
        self.window = pyglet.window.Window(
            width=1280,
            height=720
        )
        self.window.push_handlers(self)

        self.key_handler = key.KeyStateHandler()
        self.window.push_handlers(self.key_handler)

        self.sprite = pyglet.shapes.Rectangle(
            x=self.window.width//2-15,
            y=self.window.height//2-15,
            width=30, height=30
        )

    def on_draw(self):
        self.window.clear()
        self.sprite.draw()

    def update(self, dt):
        movement_speed = 60

        if self.key_handler[key.LSHIFT]:
            movement_speed *= 20

        if (
            (self.key_handler[key.A] or
             self.key_handler[key.D]) and
            (self.key_handler[key.W] or
             self.key_handler[key.S])
        ):
            movement_speed /= 2 ** 0.5

        if self.key_handler[key.W]:
            self.sprite.y += movement_speed * dt
        if self.key_handler[key.A]:
            self.sprite.x -= movement_speed * dt
        if self.key_handler[key.S]:
            self.sprite.y -= movement_speed * dt
        if self.key_handler[key.D]:
            self.sprite.x += movement_speed * dt

    def run(self):
        pyglet.clock.schedule_interval(self.update, 1/60)
        pyglet.app.run()


if __name__ == "__main__":
    application = Application()
    application.run()
