# basic snake game code is from : https://codereview.stackexchange.com/questions/161377/python-snake-game-with-pygame
from Snake import Snake
from Board import Board
from SnakeBody import SnakeBody
from Food import Food
import pygame
import time
import random
import csv
import numpy as np


def UpdtDataSet(data_set, mov, snake, food):
    # initDataSet('DataSets.csv')
    new_row = np.array([0] * 258)
    new_row[int(food.food_y / 10) * 16 + int(food.food_x / 10)] = 1
    for i in range(1, (len(snake) - 1)):
        new_row[int(snake[i].y / 10) * 16 + int(snake[i].x / 10)] = 2
    new_row[int(snake[0].y / 10) * 16 + int(snake[0].x / 10)] = 3
    new_row[257] = mov

    data_set = np.vstack([data_set, new_row])
    return data_set


def main():
    clock = pygame.time.Clock()
    display_width = 160
    display_height = 160

    # no idea how does the score works.
    score = 60

    game_display = Board(display_width, display_height)
    snake = Snake(20, 20, 3)
    food = Food(0, display_width, display_height, 10)
    # x = 0
    # y = 0
    x_change = 0
    y_change = 0
    first_time = True
    eat = True
    mov = 0

    datsts = np.arange(258)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                break
            if event.type == pygame.KEYDOWN:
                first_time = False
                if event.key == pygame.K_LEFT:
                    if x_change != 10:
                        x_change = -10
                        y_change = 0
                        mov = 4
                elif event.key == pygame.K_RIGHT:
                    if x_change != -10:
                        x_change = 10
                        y_change = 0
                        mov = 6
                elif event.key == pygame.K_UP:
                    if y_change != 10:
                        x_change = 0
                        y_change = -10
                        mov = 8
                elif event.key == pygame.K_DOWN:
                    if y_change != -10:
                        x_change = 0
                        y_change = 10
                        mov = 2

        datsts = UpdtDataSet(datsts, mov, snake, food)

        if not first_time:
            snake.update(score)
        if score % 10 == 0 and eat:
            snake.append(SnakeBody(snake[len(snake) - 1].x, snake[len(snake) - 1].y))
            print(len(snake))
            eat = False
        snake.move_head(x_change, y_change)

        if (snake[0].x < food.food_x + 10 and snake[0].x >= food.food_x
                and snake[0].y < food.food_y + 10 and snake[0].y >= food.food_y):
            score += 10
            food = Food(0, display_width, display_height, 10)
            eat = True

        if snake.check_death(display_width, display_height):
            game_display.pop_exit_window(datsts)

        game_display.GAME_display.fill(Board.white)

        pygame.draw.rect(game_display.GAME_display, Board.red, (food.food_x, food.food_y, Snake.factor, Snake.factor))
        snake.draw(game_display.GAME_display)

        pygame.display.flip()
        time.sleep(0.045)
        clock.tick(60)


if __name__ == "__main__":
    main()

