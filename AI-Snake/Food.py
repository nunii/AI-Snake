import random


class Food:

    def __init__(self, start, width_stop, height_stop, step, snake):

        Food.draw(self, start, width_stop, height_stop, step)
        check = True

        while check:
            for i in range(0, len(snake) - 1):
                if not (self.food_x == snake[i].x and self.food_y == snake[i].y):
                    check = False
                else:
                    Food.draw(self, start, width_stop, height_stop, step)

    def draw(self, start, width_stop, height_stop, step):
        rand_x = random.randrange(start, width_stop - step)
        if rand_x % 10 != 0:
            rand_x = (rand_x - rand_x % 10)
        self.food_x = rand_x

        rand_y = random.randrange(start, height_stop - step)
        if rand_y % 10 != 0:
            rand_y = (rand_y - rand_y % 10)
        self.food_y = rand_y