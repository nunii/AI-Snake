
# basic snake game code is from : https://codereview.stackexchange.com/questions/161377/python-snake-game-with-pygame
from Snake import Snake
from Board import Board
from SnakeBody import SnakeBody
from Food import Food
import pygame
import time
import random


def main():

    clock = pygame.time.Clock()
    display_width = 600
    display_height = 800


    # no idea how does the score works.
    score = 60

    game_display = Board(display_width, display_height)
    snake = Snake(20, 20, 3)
    food = Food(5, display_width, display_height, 5)
    # x = 0
    # y = 0
    x_change = 0
    y_change = 0
    first_time = True
    eat = True

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                first_time = False
                if event.key == pygame.K_LEFT:
                    if x_change != 10:
                        x_change = -10
                        y_change = 0
                elif event.key == pygame.K_RIGHT:
                    if x_change != -10:
                        x_change = 10
                        y_change = 0
                elif event.key == pygame.K_UP:
                    if y_change != 10:
                        x_change = 0
                        y_change = -10
                elif event.key == pygame.K_DOWN:
                    if y_change != -10:
                        x_change = 0
                        y_change = 10

        if not first_time:
            snake.update(score)
        if score % 10 == 0 and eat:
            snake.append(SnakeBody(
                snake[len(snake) - 1].x, snake[len(snake) - 1].y))
            print(len(snake))
            eat = False
        snake.move_head(x_change, y_change)

        if (snake[0].x < food.food_x + 10 and snake[0].x > food.food_x - 10
                and snake[0].y < food.food_y + 10 and snake[0].y > food.food_y - 10):
            score += 10
            food.food_x = random.randrange(5, display_width - 5)
            food.food_y = random.randrange(5, display_height - 5)
            eat = True

        if snake.check_death(display_width, display_height):
            game_display.pop_exit_window()

        game_display.GAME_display.fill(Board.white)

        pygame.draw.rect(game_display.GAME_display, Board.black, (food.food_x, food.food_y, Snake.factor, Snake.factor))
        snake.draw(game_display.GAME_display)

        pygame.display.flip()
        time.sleep(0.045)
        clock.tick(60)


if __name__ == "__main__":
    main()