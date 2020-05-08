import random
import time

import pyglet

from .basic import Basic


class Ball(Basic):
    def __init__(self, application):
        super().__init__(
            application,
            application.window.width//2-7,
            application.window.height//2-7,
            14, 14,
            (255, 255, 255)
        )
        self.vx = random.choice([-200, 200])
        self.vy = random.randint(-175, 175)
        self.wait_time = 0

    def update(self, dt):
        if self.wait_time < 0.25:
            self.wait_time += dt
            return

        collided = False
        if (
            self.aabb[0] < 25
        ):
            self.application.score_2 += 1
            self.application.score_label_2.text = str(self.application.score_2)
            self.application.win.play()
            self.__init__(self.application)
            if self.application.score_2 >= 10:
                self.application.win_text_raw = "Player 2 Wins!"
                self.application.win_text = pyglet.text.Label(
                    text=self.application.win_text_raw,
                    font_name="Bit5x3",
                    font_size=70,
                    batch=self.application.batch,
                    anchor_x="center",
                    x=self.application.window.width//2,
                    y=self.application.window.height//2
                )
        elif (
            self.aabb[2] > self.application.window.width - 25
        ):
            self.application.score_1 += 1
            self.application.score_label_1.text = str(self.application.score_1)
            self.application.win.play()
            self.__init__(self.application)
            if self.application.score_1 >= 10:
                self.application.win_text_raw = "Player 1 Wins!"
                self.application.win_text = pyglet.text.Label(
                    text=self.application.win_text_raw,
                    font_name="Bit5x3",
                    font_size=70,
                    batch=self.application.batch,
                    anchor_x="center",
                    x=self.application.window.width//2,
                    y=self.application.window.height//2
                )

        if (
            self.aabb[1] < 25 or
            self.aabb[3] > self.application.window.height - 25
        ):
            self.vy *= -1
            collided = True

        if self.aabbCheck(self.application.paddle_1):
            self.vx *= -1
            collided = True
        if self.aabbCheck(self.application.paddle_2):
            self.vx *= -1
            collided = True

        if collided:
            self.application.bounce.play()
            if self.vx < 0:
                self.vx -= 5
                self.vx = max(-600, self.vx)
            else:
                self.vx += 5
                self.vx = min(600, self.vx)

            if self.vy < 0:
                self.vy -= 5
                self.vy = max(-600, self.vy)
            else:
                self.vy += 5
                self.vy = min(600, self.vy)

        super().update(dt)
