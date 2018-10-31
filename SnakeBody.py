
class SnakeBody:

    def __init__(self, x, y):
        self.x, self.y = x, y

    def __repr__(self):
        return "SnakeBody({self.x}, {self.y})".format(self=self)
