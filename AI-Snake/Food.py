import random


class Food:

    def __init__(self, start, width_stop, height_stop, step):

        rand_x = random.randrange(0, width_stop - 10)
        if rand_x % 10 != 0:
            rand_x = (rand_x - rand_x % 10)
        self.food_x = rand_x

        rand_y = random.randrange(0, width_stop - 10)
        if rand_y % 10 != 0:
            rand_y = (rand_y - rand_y % 10)
        self.food_y = rand_y