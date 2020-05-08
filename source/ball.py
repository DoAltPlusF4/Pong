from .basic import Basic


class Ball(Basic):
    def __init__(self, application):
        super().__init__(
            application,
            application.window.width//2-10,
            application.window.height//2-10,
            20, 20,
            (255, 255, 255)
        )
