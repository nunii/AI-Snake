import random


class Food:

    def __init__(self, start, width_stop, height_stop, step):
        self.food_x = random.randrange(5, width_stop - 5)
        self.food_y = random.randrange(5, height_stop - 5)