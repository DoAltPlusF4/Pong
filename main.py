import random

import pyglet
import pymunk
import pymunk.pyglet_util
from pyglet.window import key, mouse

from source.ball import Ball
from source.basic import Basic
from source.paddle import Paddle


class Application:
    def __init__(self):
        self.loadResources()
        self.window = pyglet.window.Window(
            width=960,
            height=720
        )
        self.window.push_handlers(self)
        self.batch = pyglet.graphics.Batch()

        self.key_handler = key.KeyStateHandler()
        self.window.push_handlers(self.key_handler)

        self.win_text_raw = None
        self.win_text = None
        self.win_timer = 0

        self.score_1 = 0
        self.score_2 = 0

        self.wait = 0

        self.space = pymunk.Space()
        self.createCollisionHandlers()

        self.borders = {
            "top": Basic(
                self,
                x=0, y=self.window.height-25,
                width=self.window.width, height=25,
                colour=(255, 255, 255),
                collision_type=0
            ),
            "right": Basic(
                self,
                x=self.window.width-25, y=0,
                width=25, height=self.window.height,
                colour=(255, 255, 255),
                collision_type=0
            ),
            "bottom": Basic(
                self,
                x=0, y=0,
                width=self.window.width, height=25,
                colour=(255, 255, 255),
                collision_type=0
            ),
            "left": Basic(
                self,
                x=0, y=0,
                width=25, height=self.window.height,
                colour=(255, 255, 255),
                collision_type=0
            )
        }

        self.paddle_1 = Paddle(self, 1)
        self.paddle_2 = Paddle(self, 2)

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

    def loadResources(self):
        pyglet.font.add_file("resources/bit5x3.ttf")
        self.paddle = pyglet.media.load(
            "resources/paddle.wav", streaming=False
        )
        self.border = pyglet.media.load(
            "resources/border.wav", streaming=False
        )
        self.win = pyglet.media.load(
            "resources/win.wav", streaming=False
        )
        self.paddle.play()
        self.border.play()
        self.win.play()

    def createCollisionHandlers(self):
        def pre_solve(arbiter, space, data):
            border = arbiter.shapes[1].body
            if border == self.borders["right"]:
                self.score_1 += 1
                self.score_label_1.text = str(self.score_1)
                if self.score_1 >= 10:
                    self.win_text_raw = "Player 1 Wins!"
                    self.win_text = pyglet.text.Label(
                        text=self.win_text_raw,
                        font_name="Bit5x3",
                        font_size=70,
                        batch=self.batch,
                        anchor_x="center",
                        x=self.window.width//2,
                        y=self.window.height//2
                    )
            elif border == self.borders["left"]:
                self.score_2 += 1
                self.score_label_2.text = str(self.score_2)
                if self.score_2 >= 10:
                    self.win_text_raw = "Player 2 Wins!"
                    self.win_text = pyglet.text.Label(
                        text=self.win_text_raw,
                        font_name="Bit5x3",
                        font_size=70,
                        batch=self.batch,
                        anchor_x="center",
                        x=self.window.width//2,
                        y=self.window.height//2
                    )
            else:
                self.border.play()
                return True

            self.wait = 0
            self.win.play()
            self.ball.reset = True
            self.paddle_1.position = (
                50,
                (application.window.height//2)-50
            )
            self.paddle_2.position = (
                application.window.width - 75,
                (application.window.height//2)-50
            )
            return False
        ball_border = self.space.add_collision_handler(1, 0)
        ball_border.pre_solve = pre_solve

        def post_solve(arbiter, space, data):
            self.paddle.play()
            self.ball.velocity = (
                self.ball.velocity.x,
                self.ball.velocity.y+random.randint(-50, 50)
            )
        ball_paddle = self.space.add_collision_handler(1, 2)
        ball_paddle.post_solve = post_solve

    def on_draw(self):
        self.window.clear()
        self.batch.draw()
        # debug_draw_options = pymunk.pyglet_util.DrawOptions()
        # self.space.debug_draw(debug_draw_options)

    def update(self, dt):
        if self.wait < 0.25:
            self.wait += dt
            return
        if self.win_text_raw is not None:
            if self.win_timer < 1:
                self.win_timer += dt
            else:
                self.win_timer = 0
                if self.win_text.text == "":
                    self.win_text.text = self.win_text_raw
                else:
                    self.win_text.text = ""
            return
        self.space.step(dt)
        self.paddle_1.update(dt)
        self.paddle_2.update(dt)
        self.ball.update(dt)

    def run(self):
        pyglet.clock.schedule_interval(self.update, 1/144)
        pyglet.app.run()


if __name__ == "__main__":
    application = Application()
    application.run()
