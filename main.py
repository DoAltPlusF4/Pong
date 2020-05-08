import pyglet
from pyglet.window import key, mouse

from source.ball import Ball
from source.paddle import Paddle


class Application:
    def __init__(self):
        pyglet.font.add_file("resources/bit5x3.ttf")

        self.window = pyglet.window.Window(
            width=960,
            height=720
        )
        self.window.push_handlers(self)
        self.batch = pyglet.graphics.Batch()

        self.key_handler = key.KeyStateHandler()
        self.window.push_handlers(self.key_handler)

        self.borders = []
        self.borders.append(pyglet.shapes.Rectangle(  # Top
            x=0, y=self.window.height,
            width=self.window.width, height=-25,
            color=(255, 255, 255),
            batch=self.batch
        ))
        self.borders.append(pyglet.shapes.Rectangle(  # Right
            x=0, y=0,
            width=25, height=self.window.height,
            color=(255, 255, 255),
            batch=self.batch
        ))
        self.borders.append(pyglet.shapes.Rectangle(  # Bottom
            x=0, y=0,
            width=self.window.width, height=25,
            color=(255, 255, 255),
            batch=self.batch
        ))
        self.borders.append(pyglet.shapes.Rectangle(  # Left
            x=self.window.width, y=0,
            width=-25, height=self.window.height,
            color=(255, 255, 255),
            batch=self.batch
        ))

        self.win_text_raw = None
        self.win_text = None
        self.win_timer = 0

        self.paddle_1 = Paddle(self, 1)
        self.paddle_2 = Paddle(self, 2)

        self.score_1 = 0
        self.score_2 = 0

        self.ball = Ball(self)

        self.score_label_1 = pyglet.text.Label(
            text=str(self.score_1),
            font_name="Bit5x3",
            font_size=90,
            batch=self.batch,
            anchor_x="right",
            x=self.window.width//2-50,
            y=self.window.height-110
        )
        self.score_label_2 = pyglet.text.Label(
            text=str(self.score_2),
            font_name="Bit5x3",
            font_size=90,
            batch=self.batch,
            anchor_x="left",
            x=self.window.width//2+50,
            y=self.window.height-110
        )

    def on_draw(self):
        self.window.clear()
        self.batch.draw()

    def update(self, dt):
        if self.win_text_raw is None:
            self.paddle_1.update(dt)
            self.paddle_2.update(dt)
            self.ball.update(dt)
        else:
            if self.win_timer < 1:
                self.win_timer += dt
            else:
                self.win_timer = 0
                if self.win_text.text == "":
                    self.win_text.text = self.win_text_raw
                else:
                    self.win_text.text = ""

    def run(self):
        pyglet.clock.schedule_interval(self.update, 1/144)
        pyglet.app.run()


if __name__ == "__main__":
    application = Application()
    application.run()
